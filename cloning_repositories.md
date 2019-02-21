# How to clone an existing repository using the command line

Before getting started, you must install `hub`, GitHub's extended CLI API.

`$ brew install hub`

Once `hub` is installed, go through the following steps:

1) Create a bare clone of the repository

`$ git clone --bare https://github.com/learn-co-curriculum/old-repo-name.git`

2) `cd` into your cloned repository

`$ cd old-repo-name.git`

3) Using hub, create a new repo with a name of choice (when using this, you will be prompted to sign into GitHub!)

`$ hub create learn-co-curriculum/dsc-new-repo`

You’ll get a message “A git remote named `origin` already exists and is set to push to https://github.com/learn-co-curriculum/old-repo-name.git”. This is expected behavior.

4) Push your files to the new repositry

`$ git push --mirror https://github.com/learn-co-curriculum/dsc-new-repo.git`

5) Then, to make sure your local repository name matches the new github repo name (this is not a mandatory step but will make life easy):

```
$ cd ..
$ rm -rf old-repo-name.git
$ git clone https://github.com/learn-co-curriculum/dsc-new-repo.git
```


In summary, these are all the commands needed:

```
$ git clone --bare https://github.com/learn-co-curriculum/old-repo-name.git
$ cd old-repo-name.git
$ hub create learn-co-curriculum/dsc-new-repo
$ git push --mirror https://github.com/learn-co-curriculum/dsc-new-repo.git
$ cd ..
$ rm -rf old-repo-name.git
$ git clone https://github.com/learn-co-curriculum/dsc-new-repo.git
```