# Master-Solution Branch Splitter

![Garden of Forking Paths](Garden-of-Forking-Paths.jpg)

## Prerequisites
* A repository with a branch called `curriculum` containing a jupyter-notebook `index.ipynb` file
* Code cells containing solution-only code should be "tagged" as such. To do this add the following comment anywhere in the the cell:
```
# __SOLUTION__
```

## Outputs
* A `master` branch that includes a `index.ipynb` notebook file and `README.md` markdown file. The `master` branch will have all markdown cells + all _untagged_ code cells

* A `solution` branch that includes a `index.ipynb` notebook file and `README.md` markdown file. The `solution` branch will have all markdown cells + all `# __SOLUTION__` tagged code cells. (the `__SOLUTION__` tag is removed for the `solution` branch. Students will not see internal tooling.)

## Instructions
* `cd` into the lab you want to edit
* checkout to the `curriculum` branch
* make the desired changes to the notebook file
* commit your changes
* run `dscreate` if you have set up the alias (see below) or `python <path-to-index.py file>`.

To create an alias so you do not need to type the full path to the file every time,
add the following to you `.bash_profile`. (Replace the example path with the path to your local file)

```bash
alias dscreate ='python /Users/alex/Development/DS/dsc-curriculum-guidelines/master-solution-branch-splitter/index.py'
```

#### Commit Messages
By default the script will take the last commit message from `curriculum` and apply it to both `master` & `solution`. If you would like to supply a custom commit message to appear on the new commits on `master` & `solution` use the `-m` flag followed by your message. Wrap your full message in quotes.

Example:
```bash
dscreate -m "My custom commit message"
```

## Troubleshooting
The first time you run this you may need to run
```
pip install gitpython
```

### TODO
* Deprecate the markdown merger when/if we move forward
