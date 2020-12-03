#!/usr/bin/env python


import dota2_api
import json
import unittest


class TestAPI:
    test_api_instance = None

    @staticmethod
    def get_instance():
        if TestAPI.test_api_instance is None:
            TestAPI.test_api_instance = dota2_api.APIWrapper()
        return TestAPI.test_api_instance


class ProPlayersTests(unittest.TestCase):
    def setUp(self):
        api = TestAPI.get_instance()
        self.pro_players = json.loads(api.pro_players())

    def test_pro_players_content(self):
        """
        Checks to make sure that the content being returned for pro players is as expected.
        """
        account_id = 88470
        steam_id = '76561197960354198'
        personaname = 'Magma.Tzy丶'
        name = 'Tzy丶'
        country_code = 'cn'

        self.assertEqual(self.pro_players[0]['account_id'], account_id,
                         'account_id = {0} is {1}.'.format(self.pro_players[0]['account_id'], account_id))
        self.assertEqual(self.pro_players[0]['steamid'], steam_id,
                         'steamid {0} is {1}.'.format(self.pro_players[0]['steamid'], steam_id))
        self.assertEqual(self.pro_players[0]['personaname'], personaname,
                         'personaname {0} is {1}.'.format(self.pro_players[0]['personaname'], personaname))
        self.assertEqual(self.pro_players[0]['name'], name,
                         'name {0} is {1}.'.format(self.pro_players[0]['name'], name))
        self.assertEqual(self.pro_players[0]['country_code'], country_code,
                         'country_code {0} is {1}.'.format(self.pro_players[0]['country_code'], country_code))

    def test_check_size(self):
        """
        The number of pro players currently sits at 2,489.  Let's check to make sure that we are getting a number of
        results that is at least in the ball park of that number.  This should account for some pro players leaving and
        some joining.
        """
        self.assertGreater(len(self.pro_players), 2400)


class TeamTests(unittest.TestCase):
    def setUp(self):
        api = TestAPI.get_instance()
        self.team = json.loads(api.team(964214))

    def test_team_content(self):
        """
        Checks to make sure that the content being returned for teams is as expected.
        """
        team_id = 964214
        team_name = 'Cygnvs Gaming'
        team_tag = 'Cygnus'

        self.assertEqual(self.team['team_id'], team_id,
                         'Team with team_id = {0} is {1}.'.format(self.team['team_id'], team_id))
        self.assertEqual(self.team['name'], team_name, 'Team {0} is {1}.'.format(self.team['name'], team_name))
        self.assertEqual(self.team['tag'], team_tag, 'Team tag {0} is {1}.'.format(self.team['tag'], team_tag))


if __name__ == '__main__':
    unittest.main()
