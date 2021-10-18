import queue
import unittest
from pythongit import git


class TestGit(unittest.TestCase):
    vcs = None

    def setUp(self) -> None:
        super().setUp()
        self.vcs = git.Git()

    def test_git_instance(self):
        self.assertIsInstance(obj=self.vcs, cls=git.Git)

    def test_git_commands_queue(self):
        self.assertIsInstance(obj=self.vcs.commands, cls=queue.Queue)

    def test_git_status_command_in_queue(self):
        self.vcs._status()
        self.assertIn(member="git status", container=self.vcs.commands.get())

    def test_git_push_command_in_queue(self):
        self.vcs._push()
        self.assertIn(member="git push", container=self.vcs.commands.get())

    def test_git_branch_command_in_queue(self):
        self.vcs._branch()
        self.assertIn(member="git branch", container=self.vcs.commands.get())

    def test_git_checkout_command_in_queue(self):
        self.vcs._checkout()
        self.assertIn(member="git checkout", container=self.vcs.commands.get())

    def test_git_add_command_in_queue(self):
        self.vcs._add()
        self.assertIn(member="git add", container=self.vcs.commands.get())

    def test_git_commit_command_in_queue(self):
        self.vcs._commit()
        self.assertIn(member="git commit", container=self.vcs.commands.get())

    def test_git_stash_command_in_queue(self):
        self.vcs._stash()
        self.assertIn(member="git stash", container=self.vcs.commands.get())

    def test_git_bundle_command_in_queue(self):
        self.vcs._bundle()
        self.assertIn(member="git bundle", container=self.vcs.commands.get())

    def test_git_has_shell_command(self):
        self.assertTrue(hasattr(self.vcs, "shell"))

    def test_git_shell_common_procedure(self):
        self.vcs._status()
        self.vcs._add()
        self.vcs._commit()
        self.assertIn(member="git status", container=self.vcs.commands.get())
        self.assertIn(member="git add", container=self.vcs.commands.get())
        self.assertIn(member="git commit", container=self.vcs.commands.get())

    def test_git_shell_common_procedure_negative(self):
        self.vcs._status()
        self.vcs._add()
        self.vcs._commit()
        self.assertIn(member="git status", container=self.vcs.commands.get())
        self.assertNotIn(member="git commit", container=self.vcs.commands.get())
        self.assertNotIn(member="git add", container=self.vcs.commands.get())

    def test_git_shell_tricky_procedure(self):
        self.vcs._status()
        self.vcs._stash()
        self.vcs._stash()
        self.vcs._add()
        self.vcs._commit()
        self.vcs._bundle()
        self.assertIn(member="git status", container=self.vcs.commands.get())
        self.assertIn(member="git stash", container=self.vcs.commands.get())
        self.assertIn(member="git stash", container=self.vcs.commands.get())
        self.assertIn(member="git add", container=self.vcs.commands.get())
        self.assertIn(member="git commit", container=self.vcs.commands.get())
        self.assertIn(member="git bundle", container=self.vcs.commands.get())

    def test_git_shell_tricky_procedure_negative(self):
        self.vcs._status()
        self.vcs._stash()
        self.vcs._stash()
        self.vcs._add()
        self.vcs._commit()
        self.vcs._bundle()
        self.assertIn(member="git status", container=self.vcs.commands.get())
        self.assertNotIn(member="git bundle", container=self.vcs.commands.get())
        self.assertNotIn(member="git commit", container=self.vcs.commands.get())
        self.assertNotIn(member="git stash", container=self.vcs.commands.get())
        self.assertNotIn(member="git add", container=self.vcs.commands.get())
        self.assertNotIn(member="git stash", container=self.vcs.commands.get())


if __name__ == '__main__':
    unittest.main()
