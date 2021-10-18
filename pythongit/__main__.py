from pythongit import git

vcs = git.Git().hard()
vcs.stash_and_save_changes().shell()
