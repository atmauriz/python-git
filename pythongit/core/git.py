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
from subprocess import check_output

from pythongit import exceptions
from pythongit.core.subcommands import (
    StatusMixin, FetchMixin, PullMixin, RebaseMixin, CheckoutMixin, PushMixin, BranchMixin, AddMixin,
    RestoreMixin, CommitMixin, ApplyMixin, StashMixin, BundleMixin, ResetMixin
)


class Mode(enum.Enum):
    SOFT = 0
    HARD = 1


class Redirection(enum.Enum):
    OUTPUT_WRITE = ">"
    OUTPUT_APPEND = ">>"
    PIPE = "|"
    INPUT_WRITE = "<"


class Shell(metaclass=abc.ABCMeta):
    """
    Generic Shell object
    """

    @abc.abstractmethod
    def shell(self): pass

    @staticmethod
    def handle_redirection(command: str):
        cmd, filename = command.split(Redirection.OUTPUT_WRITE.value)
        with open(filename.strip(), "w") as patch_file:
            subprocess.call(shlex.split(cmd), stdout=patch_file)


class Git(
    Shell,
    StatusMixin, FetchMixin, PullMixin, RebaseMixin, CheckoutMixin, PushMixin, BranchMixin, AddMixin,
    RestoreMixin, CommitMixin, ApplyMixin, StashMixin, BundleMixin, ResetMixin
):
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
                command = self.__commands.get()
                if Redirection.OUTPUT_WRITE.value in command:
                    self.handle_redirection(command=command)
                else:
                    subprocess.Popen(args=shlex.split(command), stdout=sys.stdout).communicate()

    def status(self):
        self._status(_queue=self.__commands)
        return self

    def fetch_all(self):
        self._fetch("-a", _queue=self.__commands)
        return self

    def pull_origin_master(self):
        self._pull("origin", "master", _queue=self.__commands)
        return self

    def rebase_origin_master(self):
        self._rebase("origin/master", _queue=self.__commands)
        return self

    def checkout_in_new_branch(self, branch_name: str):
        self._checkout("-b", branch_name, _queue=self.__commands)
        return self

    def checkout_and_discard_changes(self, where: str = "."):
        self._checkout("--", where, _queue=self.__commands)
        return self

    def push_origin_on_branch(self, branch_name: str):
        self._push("origin", branch_name, _queue=self.__commands)
        return self

    def push_origin_on_branch_with_force(self, branch_name: str):
        self._push("origin", branch_name, "--force", _queue=self.__commands)
        return self

    def branch(self):
        self._branch(_queue=self.__commands)
        return self

    def branch_verbose(self):
        self._branch("-vv", _queue=self.__commands)
        return self

    def branch_all(self):
        self._branch("-a", _queue=self.__commands)
        return self

    def add_not_staged_changes(self, where: str = "."):
        self._add(where, _queue=self.__commands)
        return self

    def restore_staged_changes(self, where: str = "."):
        self._restore("--staged", where, _queue=self.__commands)
        return self

    def commit(self):
        self._commit(_queue=self.__commands)
        return self

    def commit_with_message(self, content: str):
        self._commit("-m", f"\"{content}\"", _queue=self.__commands)
        return self

    def apply_patch_file(self, patch_file: str):
        self._apply(patch_file, _queue=self.__commands)
        return self

    def stash_and_clear_stashed_changes(self):
        self._stash("clear", _queue=self.__commands)
        return self

    def stash_and_save_changes(self):
        self._stash("save", _queue=self.__commands)
        return self

    def stash_and_list_saved_changes(self):
        self._stash("list", _queue=self.__commands)
        return self

    def stash_and_pop_last_changes(self):
        self._stash("pop", _queue=self.__commands)
        return self

    def stash_and_show_last_changes(self):
        self._stash("show", _queue=self.__commands)
        return self

    def stash_and_show_last_changes_as_patch(self):
        self._stash("show", "--patch", _queue=self.__commands)
        return self

    def stash_and_show_last_changes_and_save_as_patch_file(self):
        self._stash("show", "--patch", ">", "patches/stashchanges.patch", _queue=self.__commands)
        return self

    def bundle_create_with_branch(self, branch_name: str):
        self._bundle("create", f"{self.__module__()}.bundle", branch_name, _queue=self.__commands)
        return self

    def reset_last_commit(self):
        self._reset("--soft", "HEAD~1", _queue=self.__commands)
        return self

    def reset_commit(self, how_many: int):
        self._reset("--soft", f"HEAD~{how_many}", _queue=self.__commands)
        return self
