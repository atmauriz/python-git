from pythongit import git

vcs = git.Git()
print("##################################################")
print(" Here we have multiple git command by string")
print("##################################################")
print()
vcs.status()
print("GIT STATUS: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 4 + "check your local git changes",
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
vcs.stash_and_clear_stashed_changes()
vcs.stash_and_save_changes()
vcs.stash_and_pop_last_changes()
print("GIT STASH: \n\t", "\n\t ".join([
    vcs.shell() + "\t" * 2 + "clear with stashed changes",
    vcs.shell() + "\t" * 3 + "stash and save changes",
    vcs.shell() + "\t" * 3 + "stash and pop last changes",
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
