# Master-Solution Branch Splitter

![Garden of Forking Paths](Garden-of-Forking-Paths.jpg)

## Context

A one-step procedure to update DS Curriculum using a branch named `curriculum` as the sole "working" branch. 

Edit the notebook file on the `curriculum` branch and run this script. That's it. `master` and `solution` will be in sync.

### How It Works

#### Labs

Labs in the DS curriculum have a `solution` branch in addition to `master` and `curriculum` branches.

The `curriculum` branch has two copies of every code cell. The one with no special markup goes to the `master` branch, the one with a `__SOLUTION__` tag goes to the `solution` branch.

Markdown cells have only one copy, and the same content populates both `master` and `solution`.

#### Lessons

Lessons in the DS curriculum do not have `solution` branches. Typically if they are written using Jupyter Notebooks, they have `curriculum` and `master` branches, which are in sync with each other. In order to use this script (which automatically generates README content and includes it in GitHub), you still want to use the `curriculum` branch for development.

If there is not a `curriculum` branch in the repository, this script is not applicable.

### What This Script Does

* Commits and pushes to remote `curriculum` branch after generating a `README.md` markdown file from the notebook.
* Commits and pushes to remote `master` branch. Commit will include a `index.ipynb` notebook file & a `README.md` markdown file generated from the notebook. The `master` branch will have all markdown cells + all _untagged_ code cells found on the `curriculum` branch.
* Commits and pushes to remote `solution` branch (if it exists). Commit will include a `index.ipynb` notebook file & a `README.md` markdown file generated from the notebook. The `solution` branch will have all markdown cells + all `# __SOLUTION__` tagged code cells found on the `curriculum` branch (the `__SOLUTION__` tag is removed for the `solution` branch so students will not see internal tooling.)

## Workflow

### Local Environment Setup

Follow the [same instructions that students use in Phase 1](https://github.com/learn-co-curriculum/dsc-data-science-env-config) to set up `learn-env` locally.

`conda activate learn-env` prior to editing the repo.

### Edit the Repo

(If you are not on the Curriculum team, prior to this step, you should have forked the curriculum repo to your personal GitHub account.)

1. Clone the repo locally and `cd` into it
2. Check out branch(es) locally
   * If this is a lab, run `git checkout solution && git checkout curriculum`
   * If this is a lesson (i.e. no `solution` branch), run `git checkout curriculum` only
3. Run `jupyter notebook` as usual, with `learn-env` activated, and make any required changes to the notebook cells in `index.ipynb`.
   * ***Note:*** If you are editing a code cell, make sure you check both the `master` (no tag) and `solution` (`__SOLUTION__` tag) versions of the cell
4. When you are finished making edits, restart the kernel and clear all cells, then go through and execute only the solution cells if solutions cells are present. If this is a lesson without a separate solution (i.e. not a "lab"), you can just run all cells.
5. Click the save button and terminate the notebook server.

### Branch Splitter Environment Setup

To use the branch splitting script, you will need a different environment than `learn-env`. To create this environment, run:

```bash
conda activate base
conda create -n branchsplit gitpython notebook
```

`conda activate branchsplit` prior to running the branch splitting script.

You also need to have [SSH auth set up for GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) on your local computer.

### Run the Branch Splitter

The general usage is

```
python path/to/script -m "commit message"
```

executed from the root of the repository you are editing.

The script is located within the [dsc-curriculum-guidelines](https://github.com/learn-co-curriculum/dsc-curriculum-guidelines) repository under the `master-solution-branch-splitter` directory, called `index.py`.

So, for example, you might run

```bash
python ~/Desktop/dsc-curriculum-guidelines/master-solution-branch-splitter/index.py -m "fix typo"
```

#### Setting Up an Alias

To create an alias so you do not need to type the full path to the file every time, add the following to you `.bash_profile`. (Replace the example path with the path to your local file)

```bash
alias dscreate="/Users/<username>/.conda/envs/branchsplit/bin/python /Users/<username>/Development/DS/dsc-curriculum-guidelines/master-solution-branch-splitter/index.py"
```

When setting up the alias you may also need to update your `.bash_profile` by closing and reopening terminal or running `source ~/.bash_profile`

After running the command remote `curriculum`, `master`, and `solution` branches will all be synced.

#### Git Details

If you don't specify a **commit message**, the script will pull the most recent one from the commit history.

It does not matter which changes are staged; **the script will `git add` everything currently present in the repo you are editing**. If you need to have some file locally that you don't want committed to GitHub, you will need to modify the `.gitignore`.

#### Note on `jupyter_contrib_nbextensions`

If you run into errors saying `ModuleNotFoundError: No module named 'jupyter_contrib_nbextensions'` double check that you're on the `branchsplit` conda environment. If you continue to have these errors (which will manifest as the README.md file not generating correctly), run `conda install -c conda-forge jupyter_contrib_nbextensions` in the `branchsplit` environment, then try again.

### Note on Additional Files (Not Notebook or README)

Any additional files added to `curriculum` and committed will be transferred to both `master` & `solution` branches when the script is run.  If one specific branch, but not the other, needs (or doesn't need) a file, it will have to be added (or removed) to that specific branch manually. 

_Note: The `index_files` directory of images is deleted and then recreated when the notebook is converted to markdown on both `master` & `solution` branches each time the script runs._
