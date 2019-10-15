# Updating the Conda Environment

Periodically the [conda environment used across the whole curriculum](https://github.com/learn-co-curriculum/dsc-data-science-env) will need to be updated. Before applying the updates it should be confirmed that the updates don't cause break lessons.

## Steps

## Confirm that you have all the packages you need to.
In the [learn environment we ask students to use](https://github.com/learn-co-curriculum/dsc-data-science-env), a handful of packages are specifically left out. This is mostly becuase these can often cause problems when installing and we'd rather not frontload all these issues in the student experience. Also, they are only used in a few labs. [See more info on the specific packages here](https://docs.google.com/document/d/1io_-mqILBstaDNEwyovwrS9TIHvLMP6bEpk_oOb88hc/edit?usp=sharing)

To make sure you have these correctly installed run the `package_check.py` file in this directory and confirm that there are no errors, `pip install` the appropriate packages until everything is installed. _Note:_ This list may not be comprehensive, if things are missing, add to it!

## Update your local conda environment
* Update all packages `conda update --all`
* Export your env to a yaml file `conda env export > new-env-test.yml --no-builds`
  * `--no-builds` specifies not to include build specifications, these specs may conflict when the Engineering team tries to run this script in their environment
* Open up the yml file and update the name of the env to whatever you'd like for this dry run (`new-env-test`)
  * Note, some massageng required: I had to make a few small modifications to this yml file to get everything to work
  * For some reason the `graphviz` package gets listed as `python-graphviz` which pip cannot find. Change the name to `graphviz`
  * May be a one-off thing, but I had to remove the specified version in the yml file from the `pyyaml` package otherwise I encountered errors. Fine to use this strategy if you get small version conflicts on different machines.
* [Remove the problematic packages listed above from the yml file entirely](https://docs.google.com/document/d/1io_-mqILBstaDNEwyovwrS9TIHvLMP6bEpk_oOb88hc/edit?usp=sharing)
* Create the new environment from the yml file with `conda env create -f new_environment_test.yml`
* It will prompt you to activate the new environment with `conda activate new-env-test`

Be sure you are using the new env when you run the script to generate an error log. Note that you can [set a default conda environment by adding the activate command to your .bashrc file](https://stackoverflow.com/questions/35575286/change-default-environment-in-anaconda)

## Create a local directory containing copies of all lessons
You can clone down all the lessons from a track by cloning down the [SE Curriculum Team repo] and following [the instructions here](https://github.com/learn-co-curriculum/curriculum-team/tree/master/scripts)

Some things of note:
* The track's id can be found by visiting `learn.co/curriculum` finding the track, clicking it, and copying the id from the URL.
* Going from the CSV file to downloading all lessons may error as some of the content has titles that include commas. You will have to make slight modifications to the script to get this to work.

## Generate a log of all errors
Running the `error_log.py` file in this directory will go through every single lesson and execute the `index.ipynb` jupyter notebook file. There are a few instructions in the file you will need to follow (things like updating the path to the lessons directory). These are clearly marked with `# ACTION REQUIRED` comments at the top of the file.

*This will take a long time (2+ hours) to run for the entire curriculum.* 

It runs the notebook in each lesson and then creates a log file of whatever was sent to STDOUT and STDERR for each lesson. It then cleans up the files that represent a lesson that was executed successfully and prints the names of the remaining erroring lessons.

## Check against known-to-error lessons
The list you created should be checked against a list of lessons that are known to error. Lessons could legitimately be designed to error for several reasons:
* It's a lesson that is teaching you about when to expect errors
* The lesson requires the student to do something that can't be replicated in the test environment (ie enter user input, paste in an API key, etc)
* The lesson includes cells that take _very_ long to execute and may timeout.

You may still want to spot-check a few of the known-to-error lessons. For example, you could confirm that for a lesson that is known to timeout, the error you received was actually a `TimeoutError: Cell execution timed out`

See the [list of known-erroring labs here](known-to-error.md)

## Update the Environments
The last steps are to update the [student repo](https://github.com/learn-co-curriculum/dsc-data-science-env) with the new yml files. This should be done in conjunction with updating any labs or lessons that need to be updated. Reach out to Engineering to update the environment for the in browser jupyter notebooks.

There may be a handful of packages that will error as "not found" when Engineering tries to create their environment. This is likely because they are running this in a Linux environment and some packages are OS specific. They should just remove the offending packages. 
