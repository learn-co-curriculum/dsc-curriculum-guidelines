# Markdown Merger; mm

## Background Information

Historically, the data science curriculum team at Flatiron School uses two branches for all labs: a master branch and a solution branch. As the names imply, the master branch is the original questions and student prompts for the lab, while the solution branch contains worked solutions. Authors usually have one of two approaches for creating these two seperate branches: some will write the master branch with blank cells for students to complete the lab and then create a solution branch, completing the exercises themselves, and others will create a completed solution branch first, afterwards removing the solutions from the master branch. Regardless, if the prompts within the lab need to be changed for whatever reason such as typos, grammatical errors or what not, editors on the curriculum team must make the same changes to both the master and solution branch. This is inherently tedious, effectively forcing the editor to do the same work twice. As a result, this tool was built to allow an editor to modify either the master or solution branch of a lab and then automatically sync those changes to the other branch.

## Using the Tool

To use the tool, first edit the index.ipynb file on either the master or solution branch. ** Do not create additional markdown cells or change the ordering of markdown cells.** (see further notes under the Warnings and Details header below. Regenerate the readme (as usual), and then add, commit and push these changes to the remote github repository. Afterwards, switch to the unmodified branch using git checkout. From there, simply run `python ~/Filepath/to/markdown_merger.py`. Note, that you must specify the appropriate filepath to the script. To make this easier, it is recommended that you create an alias for this command. See the notes for how to do this under the Advance Usage: Aliasing header below. Once the script is run, index.ipynb will be modified to match the markdown of the other branch and a new README.md file will be generated. You should be able to see these changes with `git status` and then standard processes for adding, commiting and pushing these changes are left to the user.


## Warnings and Details

The tool works by examinging the edited branch (assumed to be the branch you are not on), and saving all of the markdown cells as a list. It then overwrites the markdown cells in the current branch that the tool is run from, overwriting each markdown cell with its corresponding counterpart from the edited branch. The tool does this simply by the order of the markdown cells. If there are a different number of markdown cells in the two branches, you will get an error message to that effective. 

Modifications to code cells will not be synced via this version of the tool. You can edit and add code cells to either branch and still use the tool to sync markdown changes between the two. Again the fundamental rule is that the markdown cells must simply be in the same order, and the modified versions markdown will be used to overwrite the markdown of the current branch.

## Advanced Usage: Aliasing

Ideally you should alias this script as mm; nicknamed after the author.
For example, assuming you are using the standard bash shell as is default on most Unix systems, add this to your .bash_profile:
alias mm='python /Users/matthew.mitchell/Documents/Tools/Repo_Tools/markdown_merger.py'
Or wherever your local copy of the script lives.
To do this, open your .bash_profile with `vim ~/.bash_profile` or whatever your favorite text editor is. Add the alias line shown above to this file. Then open a new terminal or run `source ~/.bash_profile` for the changes to take effect. Afterwards, you should be able to simply run the alias such as `mm` to run the script from any lab repository where you wish to sync markdown changes.