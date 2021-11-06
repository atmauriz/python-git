"""
Entrypoint for the 'pythongit' python module.

Description:
    It is a collection of the commmon command line tool 'git'. It can collect multiple operations at the same time.
    Every single 'git' subcommand is been defined as a Mixin of the generic Git python object that you can find
    in the pythongit/core/git.py module.
    SoftGit and HardGit are the implementation of the generic Git object in order to be able to divide the scope of
    each implementation:
        SoftGit - as a reminder, as a debug tool
        HardGit - as a concrete implementation of the 'git' tool. It will process the command requested.

Example
SOFT USAGE
1) Simple Case
>>> python -m pythongit --soft 'status' # it print out the git status command in the background

2) Complex Case
>>> python -m pythongit --soft 'status' 'reset last commit' 'status' # it print out multiple commands in background

---

HARD USAGE
1) Simple Case
>>> python -m pythongit --hard 'status' # it launches the git status command in the background

2) Complex Case
>>> python -m pythongit --hard 'status' 'reset last commit' 'status' # it launches multiple commands in background

Thanks to 'git' most beautiful VCS.
Thanks to 'python', it makes me feel good while coding as always.
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
