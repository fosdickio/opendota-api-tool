#!/usr/bin/env python


from argparse import ArgumentParser, FileType
import logging
import yaml
from sys import stdout

from dota2_api.api_wrapper import APIWrapper


logger = logging.getLogger('dota2_api')


def parse_args():
    """
    Retrieve args from command line.
    """
    parser = ArgumentParser(
        description="Find the DOTA 2 teams with the most combined player *experience",
        epilog="*Experience is defined as the length of a player's recorded history.",
    )
    parser.add_argument(
        "output", type=FileType("w"), nargs="?", default=stdout
    )
    parser.add_argument(
        "-n",
        "--numteams",
        type=int,
        default=5,
        help="number of teams in output",
    )
    parser.add_argument(
        "-l",
        "--loglevel",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
        default="WARNING",
        help="Only output log messages of this severity or above. Writes to stderr. (default: %(default)s)",
    )
    return parser.parse_args()


def write_top_teams_to_yaml(top_teams, output_file):
    logger.info("Writing top teams to the file {}...".format(output_file))
    yaml.dump(top_teams, output_file)
    logger.info("Finished writing top teams to the file {}.".format(output_file))


def main():
    args = parse_args()
    logger.setLevel(args.loglevel)

    dota_api = APIWrapper()
    top_teams = dota_api.get_top_teams(args.numteams)
    write_top_teams_to_yaml(top_teams, args.output)


if __name__ == "__main__":
    main()
