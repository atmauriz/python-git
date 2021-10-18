from pythongit import git

vcs = git.Git().hard()
vcs.add_not_staged_changes().commit_with_message(content="hotfix on push changes").push_origin_on_branch(branch_name="develop").shell()