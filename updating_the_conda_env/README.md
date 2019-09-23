# Updating the Conda Environment

Periodically we will update the conda environment used across the whole curriculum.

In doing this we want to be sure that we are not breaking anything that wasn't already broken.

## Steps

#### Confirm that you have all the packages you need to.
Run the `package_check.py` file in this directory and confirm that there are no errors, `pip install` the appropriate packages until everything is installed. _Note:_ This list is not yet comprehensive, if things are missing, add to it!

#### Update your local conda environment

#### Create a local directory containing copies of all lessons
You can clone down all the lessons from a track using the script [here](https://github.com/learn-co-curriculum/curriculum-team/tree/master/scripts)

Some things of note:
* You'll need to clone down the repo above
* The track's id can be found by visiting `learn.co/curriculum` finding the track, clicking it, and copying the id from the URL.
* Going from the CSV file to downloading all lessons may error as some of the content has titles that include commas. You will have to make slight modifications to the script to get this to work.

#### Generate a log of all errors curriculum-wide
Running the `error_log.py` file in this directory will go through every single lesson and execute the `index.ipynb` jupyter notebook file. There are a few instructions in the file you will need to follow (things like updating the path to the lessons directory). These are clearly marked with `# ACTION REQUIRED` comments at the top of the file.

This will take a long time (2+ hours) to run for the entire curriculum. It runs the notebook in each lesson and then creates a log file of whatever was sent to STDOUT and STDERR for each lesson. It then cleans up the files that represent a lesson that was executed successfully and prints the remaining errors.

#### Check against known-to-error lessons
The list you created should be checked against a list of lessons that are known to error. Lessons could legitimately be designed to error for several reasons:
* It's a lesson that is teaching you about when to expect errors
* The lesson requires the student to do something that can't be replicated in the test environment (ie enter user input, paste in an API key, etc)
* The lesson includes cells that take _very_ long to execute and may timeout.

You may still want to spot-check a few of the known-to-error lessons. For example, you could confirm that for a lesson that is known to timeout, the error you received was actually a `TimeoutError: Cell execution timed out`

See the list of known-erroring labs [here](known-to-error.md)
