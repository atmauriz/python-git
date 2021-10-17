"""
Git python module to handle Git opearation
"""
import abc
import enum
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

    def __init__(self) -> None:
        self.__commands = queue.Queue()
        if ".git" not in os.listdir():
            raise exceptions.GitDirectoryNotFound

    def __command(self, cmd: str):
        return f"git {cmd}"

    @property
    def commands(self) -> queue.Queue:
        return self.__commands

    def shell(self, mode: Mode = Mode.SOFT):
        if mode == Mode.SOFT:
            return self.__commands.get()
        elif mode == Mode.HARD:
            # todo: subprocess.Popen command
            pass

    def status(self):
        self.__commands.put(self.__command(cmd="status"))

    def add(self):
        self.__commands.put(self.__command(cmd="add"))

    def commit(self):
        self.__commands.put(self.__command(cmd="commit"))

    def stash(self):
        self.__commands.put(self.__command(cmd="stash"))

    def bundle(self):
        self.__commands.put(self.__command(cmd="bundle"))
