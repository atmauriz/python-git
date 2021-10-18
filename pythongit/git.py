"""
Git python module to handle Git opearation
"""
import abc
import enum
import logging
import os
import queue

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

    @property
    def commands(self) -> queue.Queue:
        return self.__commands

    def shell(self):
        if self.__mode == Mode.SOFT:
            return self.__commands.get(timeout=5)
        elif self.__mode == Mode.HARD:
            # todo: subprocess.Popen command
            pass

    def _status(self):
        self.__commands.put(self.__command(cmd="status"))

    def status(self):
        self._status()

    def _checkout(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["checkout"] + [*args])))

    def checkout_in_new_branch(self, branch_name: str):
        self._checkout("-b", branch_name)

    def checkout_and_discard_changes(self, where: str = "."):
        self._checkout("--", where)

    def _push(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["push"] + [*args])))

    def push_origin_on_branch(self, branch_name: str):
        self._push(branch_name)

    def push_origin_on_branch_with_force(self, branch_name: str):
        self._push(branch_name, "--force")

    def _branch(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["branch"] + [*args])))

    def branch(self):
        self._branch()

    def branch_verbose(self):
        self._branch("-vv")

    def branch_all(self):
        self._branch("-a")

    def _add(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["add"] + [*args])))

    def add_not_staged_changes(self, where: str = "."):
        self._add(where)

    def _commit(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["commit"] + [*args])))

    def commit(self):
        self._commit()

    def commit_with_message(self, content: str):
        self._commit("-m", content)

    def _stash(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["stash"] + [*args])))

    def stash_and_clear_stashed_changes(self):
        self._stash("clear")

    def stash_and_save_changes(self):
        self._stash("save")

    def stash_and_pop_last_changes(self):
        self._stash("pop")

    def _bundle(self, *args):
        self.__commands.put(self.__command(cmd=" ".join(["bundle"] + [*args])))

    def bundle_create_with_branch(self, branch_name: str):
        self._bundle("create", f"{self.__module__()}.bundle", branch_name)
