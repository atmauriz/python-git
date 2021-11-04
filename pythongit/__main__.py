from pythongit.core import git

vcs = git.Git().hard()
vcs.bundle_create_with_branch(branch_name="develop").shell()

# IT WORKS
# stash current changes, create a patch file into patches directory and clear stash saved changes
# vcs.stash_and_save_changes().stash_and_show_last_changes_and_save_as_patch_file().stash_and_clear_stashed_changes().shell()

# IT WORKS
# apply patch changes
# vcs.apply_patch_file(patch_file="patches/stashchanges.patch").shell()

# IT WORKS
# vcs.add_not_staged_changes().commit_with_message(content="Stash command completed").shell()
