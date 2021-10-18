from pythongit import git

vcs = git.Git().hard()
vcs.add_not_staged_changes().commit_with_message(
    content="Commands validation one by one"
).shell()
