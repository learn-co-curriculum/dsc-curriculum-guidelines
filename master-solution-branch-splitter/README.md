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

## INSTRUCTIONS

From the target repository run `python <path-to-index.py file>`.

To create an alias so you do not need to type the full path to the file every time,
add the following to you `.bash_profile`. (Replace the example path with the path to your local file)

```bash
alias dscreate ='python /Users/alex/Development/DS/dsc-curriculum-guidelines/master-solution-branch-splitter/index.py'
```

### TODO
* Deprecate the markdown merger when/if we move forward
