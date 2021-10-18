"""
Git python module to handle Git opearation
"""
import abc
import enum
import logging
import os
import queue
import shlex
import subprocess
import sys

from abc import ABCMeta

from pythongit import exceptions


class Mode(enum.Enum):
    SOFT = 0
    HARD = 1


class Shell(metaclass=abc.ABCMeta):
    """
    Generic Shell object
    """

    @abc.abstractmethod
    def shell(self): pass


class Git(Shell):
    """
    Git object
    """

    __commands = None
    __mode: Mode = Mode.SOFT
    __module = "pythongit"

    def __init__(self) -> None:
        self.__commands = queue.Queue()
        if ".git" not in os.listdir(path="."):
            raise exceptions.GitDirectoryNotFound

    def __module__(self):
        return self.__module

    def __command(self, cmd: str):
        return f"git {cmd}"

    @property
    def mode(self):
        return self.__mode

    def hard(self):
        self.__mode = Mode.HARD
        return self

    @property
    def commands(self) -> queue.Queue:
        return self.__commands

    def shell(self):
        if self.__mode == Mode.SOFT:
            return self.__commands.get(timeout=5)
        elif self.__mode == Mode.HARD:
            while not self.__commands.empty():
                subprocess.Popen(args=shlex.split(self.__commands.get()), stdout=sys.stdout).communicate()

    def _status(self):
        self.__commands.put(self.__command(cmd="status"))

    def status(self):
        self._status()
        return self

    def _checkout(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["checkout"] + [*args])))

    def checkout_in_new_branch(self, branch_name: str):
        self._checkout("-b", branch_name)
        return self

    def checkout_and_discard_changes(self, where: str = "."):
        self._checkout("--", where)
        return self

    def _push(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["push"] + [*args])))

    def push_origin_on_branch(self, branch_name: str):
        self._push(branch_name)
        return self

    def push_origin_on_branch_with_force(self, branch_name: str):
        self._push(branch_name, "--force")
        return self

    def _branch(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["branch"] + [*args])))

    def branch(self):
        self._branch()
        return self

    def branch_verbose(self):
        self._branch("-vv")
        return self

    def branch_all(self):
        self._branch("-a")
        return self

    def _add(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["add"] + [*args])))

    def add_not_staged_changes(self, where: str = "."):
        self._add(where)
        return self

    def _restore(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["restore"] + [*args])))

    def restore_staged_changes(self, where: str = "."):
        self._restore("--staged", where)
        return self

    def _commit(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["commit"] + [*args])))

    def commit(self):
        self._commit()
        return self

    def commit_with_message(self, content: str):
        self._commit("-m", f"\"{content}\"")
        return self

    def _stash(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["stash"] + [*args])))

    def stash_and_clear_stashed_changes(self):
        self._stash("clear")
        return self

    def stash_and_save_changes(self):
        self._stash("save")
        return self

    def stash_and_list_saved_changes(self):
        self._stash("list")
        return self

    def stash_and_pop_last_changes(self):
        self._stash("pop")
        return self

    def _bundle(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["bundle"] + [*args])))

    def bundle_create_with_branch(self, branch_name: str):
        self._bundle("create", f"{self.__module__()}.bundle", branch_name)
        return self
