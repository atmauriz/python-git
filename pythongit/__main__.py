"""
Entrypoint for the 'pythongit' python module.
"""
import argparse
import logging

from pythongit.core import git

logging.basicConfig(level=logging.DEBUG)


def exit_in_case_no_vcs():
    """
    Terminate the application in case no VCS reached from the command line parser and
    pretty print the parser.help in console.

    :return: None
    """
    if vcs is None:
        print()
        parser.print_help()
        print()
        exit(0)


#############################################################################
# PARSER configuration in order to be ready to execute as a python module  ##
#############################################################################
parser = argparse.ArgumentParser(description="PythonGit command line interface")
parser.add_argument(
    "--hard",
    action="store_true",
    help="Get git instance that perform system command"
)
parser.add_argument(
    "--soft",
    action="store_true",
    help="Get git instance that print command in console"
)
parser.add_argument(
    "commands",
    nargs="+",
    help="Git Commands to execute"
)
arguments = parser.parse_args()

#############################################################################
# BOOTSTRAP initialization of the VCS instance  #############################
#############################################################################
vcs = git.SoftGit() if arguments.soft else git.HardGit() if arguments.hard else None
exit_in_case_no_vcs()

#############################################################################
# PROCESSING command line arguments passed  #################################
#############################################################################
vcs.drill(commands=arguments.commands)
