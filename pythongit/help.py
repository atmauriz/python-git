from pythongit import git

vcs = git.Git()
print("##################################################")
print(" Here we have git commands as string in Mode.SOFT ")
print("##################################################")
print()
vcs.status()
print("GIT STATUS: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 4 + "check your local git changes",
]))
print()
vcs.fetch_all()
print("GIT FETCH: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 4 + "fetch changes from remote repository",
]))
print()
vcs.pull_origin_master()
print("GIT PULL: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 4 + "fetch changes from master branch and apply into your current branch",
]))
print()
vcs.rebase_origin_master()
print("GIT REBASE: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 4 + "rebase your changes with remote master branch",
]))
print()
vcs.add_not_staged_changes(where=".")
vcs.add_not_staged_changes(where="yourrelativepath")
vcs.add_not_staged_changes(where="tests")
print("GIT ADD: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 6 + "add current directory",
    vcs.shell() + "\t" * 2 + "add relative path",
    vcs.shell() + "\t" * 5 + "add relative path",
]))
print()
vcs.restore_staged_changes()
vcs.restore_staged_changes(where="yourrelativepath")
print("GIT RESTORE: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 8 + "restore staged changes",
    vcs.shell() + "\t" * 4 + "restore staged changes",
]))
print()
vcs.stash_and_clear_stashed_changes()
vcs.stash_and_save_changes()
vcs.stash_and_list_saved_changes()
vcs.stash_and_pop_last_changes()
vcs.stash_and_show_last_changes()
vcs.stash_and_show_last_changes_as_patch()
vcs.stash_and_show_last_changes_and_save_as_patch_file()
print("GIT STASH: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 11 + "clear with stashed changes",
    vcs.shell() + "\t" * 12 + "stash and save changes",
    vcs.shell() + "\t" * 12 + "stash and list saved changes",
    vcs.shell() + "\t" * 12 + "stash and pop last changes",
    vcs.shell() + "\t" * 12 + "stash and show last changes",
    vcs.shell() + "\t" * 10 + "stash and show last changes as patch",
    vcs.shell() + "\t" * 2 + "stash and show last changes and save as patch file",
]))
print()
vcs.commit()
vcs.commit_with_message(content="first commit")
print("GIT COMMIT: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 6 + "commit standard command",
    vcs.shell() + "\t" * 2 + "commit with message",
]))
print()
vcs.checkout_in_new_branch(branch_name="test-my-new-branch")
vcs.checkout_and_discard_changes()
print("GIT CHECKOUT: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 2 + "checkout in new branch name and move on it",
    vcs.shell() + "\t" * 6 + "discard not staged changes"
]))
print()
vcs.bundle_create_with_branch(branch_name="master")
vcs.bundle_create_with_branch(branch_name="develop")
print("GIT BUNDLE: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 2 + "bundle git repository with specific branch",
    vcs.shell() + "\t" * 2 + "bundle git repository with specific branch",
]))
print()
vcs.branch()
vcs.branch_verbose()
vcs.branch_all()
print("GIT BRANCH: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 2 + "check your local branches",
    vcs.shell() + "\t" * 2 + "check your local branches with verbose details",
    vcs.shell() + "\t" * 2 + "check all branches of your repository",
]))
print()
vcs.push_origin_on_branch(branch_name="master")
vcs.push_origin_on_branch_with_force(branch_name="develop")
print("GIT PUSH: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 2 + "push on origin specific branch",
    vcs.shell() + "\t" * 2 + "push on origin specific branch with force",
]))
print()
vcs.apply_patch_file(patch_file="patches/stashchanges.patch")
print("GIT APPLY: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 2 + "apply patch file changes into your local workspace",
]))
