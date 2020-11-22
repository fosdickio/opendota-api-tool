# Dota 2 Top Teams Tool
This repository contains a tool and API wrapper for interacting with the [OpenDota API](https://docs.opendota.com/#section/Introduction).  The API is responsible for serving content related to the game [Dota 2](http://www.dota2.com/play/).  The API itself is free to use without an API key, but is limited to 50,000 free calls per month and 60 requests/minute.

`top_teams_to_yaml.py` outputs a list of the top teams and their associated players by total experience to a specified YAML file.  In this case, total experience is pulled from each professional player's `full_history_time`.  This is defined as the the amount of time that has passed since the start of a player's data history.  The following information is returned:

```
* Team Name
* Team ID
* Wins
* Losses
* Rating
* Team Experience
* For each player:
    * Personaname
    * Player Experience
    * Country Code
```

## Requirements
- Python 3.5+

## Instructions
To run the command line tool to output the top teams to a YAML file, use the following commands:
```bash
pip3 install -r requirements.txt
python3 top_teams_to_yaml.py top_teams.yaml
```

If you would like to install the API wrapper as a package for later use, you may do so using the following command:
```bash
python3 setup.py install
```

## Testing
To run tests for the program, you can run the following commands:
```bash
python3 setup.py install
python3 tests/test_api.py
```

## Continuous Integration
A `.travis.yml` file has been included to run tests automatically when integrated with [Travis CI](https://travis-ci.com/).  In runs executes against Python versions 3.4 to 3.8.

## Next Up
I believe the following items are beyond the scope of this initial work, but I'm making a note of things that should be taken care of next here so that they can be expanded upon later.
- Increase test code coverage
- Implement caching mechanism so the same API calls don't need to be repeatedly made
- Implement API rate limiting to help guarantee that the daily limit of 50,000 won't be hit accidentally

## Troubleshooting
When executing the program, if you see the error `ModuleNotFoundError: No module named 'yaml'`, then try installing `pyyaml` using the following command:
```bash
python3 -m pip install pyyaml
```