import queue
import unittest
from pythongit import git


class TestGit(unittest.TestCase):
    instance = None

    def setUp(self) -> None:
        super().setUp()
        self.instance = git.Git()

    def test_git_instance(self):
        self.assertIsInstance(obj=self.instance, cls=git.Git)

    def test_git_commands_queue(self):
        self.assertIsInstance(obj=self.instance.commands, cls=queue.Queue)

    def test_git_status_command_in_queue(self):
        self.instance.status()
        self.assertIn(member="git status", container=self.instance.commands.get())

    def test_git_add_command_in_queue(self):
        self.instance.add()
        self.assertIn(member="git add", container=self.instance.commands.get())

    def test_git_commit_command_in_queue(self):
        self.instance.commit()
        self.assertIn(member="git commit", container=self.instance.commands.get())

    def test_git_stash_command_in_queue(self):
        self.instance.stash()
        self.assertIn(member="git stash", container=self.instance.commands.get())

    def test_git_bundle_command_in_queue(self):
        self.instance.bundle()
        self.assertIn(member="git bundle", container=self.instance.commands.get())

    def test_git_has_shell_command(self):
        self.assertTrue(hasattr(self.instance, "shell"))

    def test_git_shell_common_procedure(self):
        self.instance.status()
        self.instance.add()
        self.instance.commit()
        self.assertIn(member="git status", container=self.instance.commands.get())
        self.assertIn(member="git add", container=self.instance.commands.get())
        self.assertIn(member="git commit", container=self.instance.commands.get())

    def test_git_shell_common_procedure_negative(self):
        self.instance.status()
        self.instance.add()
        self.instance.commit()
        self.assertIn(member="git status", container=self.instance.commands.get())
        self.assertNotIn(member="git commit", container=self.instance.commands.get())
        self.assertNotIn(member="git add", container=self.instance.commands.get())

    def test_git_shell_tricky_procedure(self):
        self.instance.status()
        self.instance.stash()
        self.instance.stash()
        self.instance.add()
        self.instance.commit()
        self.instance.bundle()
        self.assertIn(member="git status", container=self.instance.commands.get())
        self.assertIn(member="git stash", container=self.instance.commands.get())
        self.assertIn(member="git stash", container=self.instance.commands.get())
        self.assertIn(member="git add", container=self.instance.commands.get())
        self.assertIn(member="git commit", container=self.instance.commands.get())
        self.assertIn(member="git bundle", container=self.instance.commands.get())

    def test_git_shell_tricky_procedure_negative(self):
        self.instance.status()
        self.instance.stash()
        self.instance.stash()
        self.instance.add()
        self.instance.commit()
        self.instance.bundle()
        self.assertIn(member="git status", container=self.instance.commands.get())
        self.assertNotIn(member="git bundle", container=self.instance.commands.get())
        self.assertNotIn(member="git commit", container=self.instance.commands.get())
        self.assertNotIn(member="git stash", container=self.instance.commands.get())
        self.assertNotIn(member="git add", container=self.instance.commands.get())
        self.assertNotIn(member="git stash", container=self.instance.commands.get())


if __name__ == '__main__':
    unittest.main()
