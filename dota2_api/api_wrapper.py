#!/usr/bin/env python

from datetime import datetime
import json
import logging
import requests

from . import endpoints, errors


logger = logging.getLogger('dota2_api')


class APIWrapper:

    def __init__(self, api_key = None):
        self.api_key = api_key

    def make_api_call(self, url, **kwargs):
        """
        Helper function to perform API requests.

        url : string - the URL being requested
        """
        response = requests.get(url, params=kwargs, timeout=60)
        status = response.status_code

        if status == 200:
            return response.text
        elif status == 400:
            raise errors.APIInsufficientArguments(url, kwargs)
        elif status == 404:
            raise errors.APIMethodUnavailable(url)
        elif status == 503:
            raise errors.APITimeoutError()
        else:
            raise errors.BaseError(msg=response.reason)

    def pro_players(self):
        """
        Retrieves a list of professional players.
        """
        logger.info("Pulling professional players...")
        data = self.make_api_call(endpoints.BASE_URL + endpoints.PRO_PLAYERS)
        logger.info("Finished pulling professional players.")
        return data

    def team(self, team_id):
        """
        Retrieves team data given a team ID.
        """
        logger.info("Pulling top teams...")
        data = self.make_api_call(endpoints.BASE_URL + endpoints.TEAMS.format(str(team_id)))
        logger.info("Finished pulling top teams.")
        return data

    def get_top_teams(self, num_teams):
        """
        Returns a list of the top teams and their associated players by total experience.  In this case, total
        experience is pulled from each professional player's "full_history_time."  This is defined as the the amount of
        time that has passed since the start of a player's data history.  The following information is returned:

            * Team Name
            * Team ID
            * Wins
            * Losses
            * Rating
            * Team Experience
            * For each Player:
                * Personaname
                * Player Experience
                * Country Code

        :param num_teams: list - the number of top teams to return
        :return: top_teams: list - a list of top teams
        """
        logger.info("Pulling top teams...")

        # Load the professional players from the API
        pro_players = json.loads(self.pro_players())

        current_time_in_ms = int(datetime.now().timestamp() * 1000)

        # Retrieve the total team experience for professional players
        team_experience = {}
        for player in pro_players:
            # Ignore professional players that aren't part of a team (team_id == 0)
            if player['team_id'] != 0:
                if player['team_id'] not in team_experience:
                    team_experience[player['team_id']] = [0, []]
                experience_time_in_ms = datetime.strptime(player['last_match_time'],
                                                          "%Y-%m-%dT%H:%M:%S.%fZ").timestamp() * 1000
                player_experience = int(current_time_in_ms - experience_time_in_ms)
                team_experience[player['team_id']][0] += int(current_time_in_ms - experience_time_in_ms)
                team_experience[player['team_id']][1].append({
                    'Personaname': player['personaname'],
                    'Player Experience': player_experience,
                    'Country Code': player['country_code']
                })

        # Sort team experience by descending amount
        desc_team_experience = {key: value for key, value in sorted(team_experience.items(),
                                                                    key=lambda item: item[1][0], reverse=True)}

        # Combine player and top team data
        count = 0
        top_teams = []
        for key, value in desc_team_experience.items():
            if count >= num_teams:
                break
            try:
                team = self.team(key)
                json_team = json.loads(team)
                top_teams.append({
                    'Team Name': json_team['name'],
                    'Team ID': json_team['team_id'],
                    'Wins': json_team['wins'],
                    'Losses': json_team['losses'],
                    'Rating': json_team['rating'],
                    'Team Experience': value[0],
                    'Players': desc_team_experience[json_team['team_id']][1]
                })
                count += 1
            except:
                logger.warning("There was an error retrieving team {}.  Continuing...".format(key))

        logger.info("Finished pulling top teams.")

        return top_teams
