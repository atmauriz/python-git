import queue


class Command:

    def _command(self, cmd: str):
        return f"git {cmd}"


class StatusMixin(Command):
    """
    git status mixin
    """

    def _status(self, _queue: queue.Queue):
        _queue.put(self._command(cmd="status"))


class FetchMixin(Command):
    """
    git fetch mixin
    """

    def _fetch(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["fetch"] + [*args])))


class PullMixin(Command):
    """
    git pull mixin
    """

    def _pull(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["pull"] + [*args])))


class RebaseMixin(Command):
    """
    git rebase mixin
    """

    def _rebase(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["rebase"] + [*args])))


class CheckoutMixin(Command):
    """
    git checkout mixin
    """

    def _checkout(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["checkout"] + [*args])))


class PushMixin(Command):
    """
    git push mixin
    """

    def _push(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["push"] + [*args])))


class BranchMixin(Command):
    """
    git branch mixin
    """

    def _branch(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["branch"] + [*args])))


class AddMixin(Command):
    """
    git add mixin
    """

    def _add(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["add"] + [*args])))


class RestoreMixin(Command):
    """
    git restore mixin
    """

    def _restore(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["restore"] + [*args])))


class CommitMixin(Command):
    """
    git commit mixin
    """

    def _commit(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["commit"] + [*args])))


class ApplyMixin(Command):
    """
    git apply mixin
    """

    def _apply(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["apply"] + [*args])))


class StashMixin(Command):
    """
    git stash mixin
    """

    def _stash(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["stash"] + [*args])))


class BundleMixin(Command):
    """
    git bundle mixin
    """

    def _bundle(self, *args, _queue: queue.Queue):
        _queue.put(self._command(cmd=" ".join(["apply"] + [*args])))
