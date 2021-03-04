#!/usr/bin/env python3
from sys import exit
from os import environ, path, popen
from configparser import ConfigParser

def check_env():
    """
    check if config env variable was overwritten
    """
    if "OSC_CONFIG" in environ:
        #make nicer variable name
        return environ["OSC_CONFIG"]
    else:
        #default value
        return path.join(path.dirname(path.abspath(__file__)),
                               "config.ini")

def main():
    """
    has to return a return code
    """
    config_file = check_env()
    # set up ini parser
    config = ConfigParser()
    config.read(config_file)

    try:
        # get userinput and find out which command to run
        user_input = input()
        command = config["commands"][user_input]
        """
        note to self. For notifications (with notify-send) it would be useful to send a string with the command.
        But that invites the danger to misuse the string to run arbitrary config.
        Best solution for now is to use --. example mv -v -- '-r'. Move is not able to use any other parameter then -v
        ATTENTION: the -- notation is not a shell builtin. every command has to support it individually
        """
    except KeyError as err:
        print("command not available, please check your config:", config_file)
        return 1

    # get output, print and return returncode
    output = popen(command)
    print(output.read(), end="")
    return output._proc.wait(timeout=int(config["global"]["command_timeout"]))


if __name__ == "__main__":
    exit(main())

