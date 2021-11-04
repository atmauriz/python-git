import queue
import unittest
from pythongit.core import git


class TestGit(unittest.TestCase):
    vcs = None

    def setUp(self) -> None:
        super().setUp()
        self.vcs = git.Git()

    def test_git_instance(self):
        self.assertIsInstance(obj=self.vcs, cls=git.Git)

    def test_git_commands_queue(self):
        self.assertIsInstance(obj=self.vcs.commands, cls=queue.Queue)


if __name__ == '__main__':
    unittest.main()
