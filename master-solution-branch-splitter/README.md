# Master-Solution Branch Splitter

![Garden of Forking Paths](Garden-of-Forking-Paths.jpg)

## Prerequisites
* A repository with a branch called `curriculum` containing a jupyter-notebook `index.ipynb` file
* Code cells containing solution-only code should be "tagged" as such. To do this add the following comment anywhere in the the cell:
```
# __SOLUTION__
```

## What it does
* Commits and pushes to remote `curriculum` branch after generating a `README.md` markdown file from the notebook.

* Commits and pushes to remote `master` branch. Commit will include a `index.ipynb` notebook file & a `README.md` markdown file generated from the notebook. The `master` branch will have all markdown cells + all _untagged_ code cells found on the `curriculum` branch.

* Commits and pushes to remote `solution` branch (if it exists). Commit will include a `index.ipynb` notebook file & a `README.md` markdown file generated from the notebook. The `solution` branch will have all markdown cells + all `# __SOLUTION__` tagged code cells found on the `curriculum` branch (the `__SOLUTION__` tag is removed for the `solution` branch so students will not see internal tooling.)

## Instructions
* `cd` into the repo of the lab you want to edit
* checkout to the `curriculum` branch
* make the desired changes to the notebook file
* commit your changes
* run `dscreate` if you have set up the alias (see below) or `python <path-to-the-index.py-file-in-this-repo>`.

To create an alias so you do not need to type the full path to the file every time,
add the following to you `.bash_profile`. (Replace the example path with the path to your local file)

```bash
alias dscreate="python /Users/alex/Development/DS/dsc-curriculum-guidelines/master-solution-branch-splitter/index.py"
```

After running the command remote `curriculum`, `master`, and `solution` branches will all be synced.

#### Commit Messages
By default the script will take the last commit message from `curriculum` and apply it to both `master` & `solution`. If you would like to supply a custom commit message to appear on the new commits on `master` & `solution` use the `-m` flag followed by your message. Wrap your full message in quotes.

Example commit message:
```bash
$ dscreate -m "My custom commit message"
```

#### Cell Order
The exact order of how you interleave solution code cells and master code cells will not matter.

Both of the following jupyter notebook structures would result in the same output on `master` and on `solution`.
The "tagged" cells will appear in order on `solution`. The untagged cells will appear in order on `master`

```
# Notebook 1
{
  "cells": [
    "Markdown Cell 1",
    "Code Cell 1",
    "__SOLUTION__ Code Cell 1",
    "Code Cell 2",
    "__SOLUTION__ Code Cell 2",
    "Code Cell 3".
    "__SOLUTION__ Code Cell 3",
    "__SOLUTION__ Code Cell 4",
    "Markdown Cell 2"
  ]
}

# Notebook 2
{
  "cells": [
    "Markdown Cell 1",
    "Code Cell 1",
    "Code Cell 2",
    "Code Cell 3",
    "__SOLUTION__ Code Cell 1",
    "__SOLUTION__ Code Cell 2",
    "__SOLUTION__ Code Cell 3",
    "__SOLUTION__ Code Cell 4",
    "Markdown Cell 2"
  ]
}

```

## Troubleshooting
The first time you run this you may need to run
```
pip install gitpython
```

When setting up the alias you may also need to update your `.bash_profile` by closing and reopening terminal or running `source ~/.bash_profile`

## Style Guide
* [Curriculm Branch Style Guide](https://docs.google.com/document/d/1YpJN9S1kzoObMyIE02OszgHdlqhRP6ktgW5S74UzbNk/edit)

### TODO
* Deprecate the markdown merger when/if we move forward
