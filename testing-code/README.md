# Testing Curriculum Code

It's a good idea to run through all of the code in the curriculum every once in a while. In particular this is useful if you are updating the `conda` environment and so some of your old code that used to work now might be using deprecated APIs.

The high-level process for doing this is:

1. Clone all of the curriculum repos into a directory
   * It doesn't matter if you already have them cloned onto your computer. This approach clones a fresh copy to avoid any unwanted changes being pushed to GitHub
   * Because all you need is Bash, a file system, and a `conda` environment, you can run this process on a Docker container or other machine that isn't just your laptop
2. Run all of the code and look for errors
   * Specifically the script here uses the `--execute` flag of NBConvert to run all of the code in the appropriate notebook on the appropriate branch of each repo
3. Make note of what errors appear, fix them, and repeat previous steps as appropriate

## Setup

The steps below assume that you have **cloned this repository** (`dsc-curriculum-guidelines`) to the computer where you will be running the scripts. And that you have a `conda` environment prepared that resembles the one you want students to use.

You also need to have a **CSV containing the HTTPS links to all curriculum lessons** that need to be tested. Your original data source for this might be Airtable, Canvas, whatever the current tooling you are using to manage the curriculum.

Each line of the CSV should contain only the repo link. The line of `pandas` code to create this from a larger dataframe of lessons will be something like:

```python
df[["repo"]].to_csv("curriculum.csv", header=False, index=False)
```

Following that example, the rest of these instructions + scripts assume your CSV has the name `curriculum.csv`. You can make edits along the way if you want to use a different name but keep in mind that the part before `.csv` will be used for directory names so it might be confusing if you include spaces or special characters.

## Cloning All Repos Locally

Once you have your CSV, navigate in the terminal to the directory containing `curriculum.csv` and run the script to download all of the repositories.

This step uses the [`cloneCSVtrack.sh`](cloneCSVtrack.sh) Bash script. It is adapted from a version in the [SE Curriculum Team repo](https://github.com/learn-co-curriculum/curriculum-team/tree/master/scripts) that assumes the CSV has 5 columns.

To run `cloneCSVtrack.sh` (in the terminal):

```bash
bash <path to cloneCSVtrack.sh> curriculum
```

For example, if you cloned this repository in `~/Development/DS/` then the full command would be:

```bash
bash ~/Development/DS/testing-code/cloneCSVtrack.sh curriculum
```

This will create a new directory called `curriculum` and clone all of the links in the CSV into that directory. This will take several minutes, possibly longer if your internet connection is slow.

(You can also individually clone repos into the `curriculum` directory with or without using the `cloneCSVtrack.sh`. Just navigate to that directory in the terminal and run `git clone` on whatever repo(s) you want.)

## Running Notebook Code to Look for Errors

When you have finished cloning all of the repositories, stay in the same directory to run the script that checks for errors. That directory should now contain `curriculum.csv` as well as a directory called `curriculum` that contains all of the cloned repos inside of it.

This step uses the [`error_log.py`](error_log.py) Python script. The logic of the script (for each repository<sup>1</sup>) is this:

1. Check out the appropriate branch
   * If there is a `solution` branch, use that
   * If not, if there is a `curriculum` branch, use that
2. Execute all of the code in `index.ipynb` by running `jupyter nbconvert --execute`, and write the output of this code execution to a file named `curriculum_log/<repo name>.txt`
   * If there is an error in the `index.ipynb` code, it will be written to that `.txt` file and should _not_ cause `error_log.py` to crash
3. If there are no problems, delete the log file
   * If the log file content ends with the pattern `\[NbConvertApp\] Writing [0-9]+ bytes to index.ipynb` then that is considered a successful execution and the log file will be deleted. (This means that only errors, not warnings, are considered to be actual problems.)
   * If the lesson is known to error, the log file also will be deleted
     * In some cases the lessons intentionally have errors in order to teach students something
     * In other cases it's more an issue of our testing setup not being sophisticated enough. For example, if there is user input involved, or the lesson requires an API key, that is going to crash every if you run it as-is with `jupyter nbconvert -- execute`. These lessons should probably be spot-checked periodically but for now the script ignores them.
4. Print out the list of lessons that still have a log file (i.e. have a problem)

<sup>1</sup>(More precisely, it actually does one loop for step 2, another for step 3, and another for step 4. So you could easily comment out the later steps without digging into the script logic.)

Before running `error_log.py` be sure to open it up and make any necessary edits (e.g. to the directory name(s) or kernel name). The parts where you are likely to need to edit are marked with `# ACTION REQUIRED`.

To run `error_log.py` (in the terminal):

```bash
python <path to error_log.py>
```

For example, if you cloned this repository in `~/Development/DS/` then the full command would be:

```bash
python ~/Development/DS/testing-code/error_log.py
```

The only package dependency you should need is `pandas`.

***This will take a long time (3+ hours) to run for the entire curriculum.***

## Spot Checking "Known to Error" Lessons

Some lessons will produce errors for some other reason than incompatibility with the environment. These are documented in the `known_to_error.csv` file. The script automatically skips over reporting errors in these lessons.

It is still a good idea to spot check these lessons periodically to make sure that the observed errors are the ones that are expected.

## Appendix: Package Check

If you are updating the `conda` environment and just want to run a quick check rather than downloading all of the curriculum, you can use the `package_check.py` file. This just attempts to **import** a bunch of packages that are used in the curriculum. It does _not_ actually test any of the classes or functions in those packages, so this is not a substitute for testing the actual curriculum code.

Usage:

```bash
python package_check.py
```
