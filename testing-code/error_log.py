import os
import subprocess
from contextlib import redirect_stdout
import re

# ACTION REQUIRED: Edit these to be the names of the appropriate directories
# LOG_DIR = make an empty directory where the log files will be created
# CURR_DIR = wherever your local copies of all labs live
LOG_DIR = "curriculum_log"
CURR_DIR = "curriculum"

# ACTION REQUIRED: update these paths as appropriate
# the provided default assumes this script will be run from
# a directory containing both the LOG_DIR and CURR_DIR
LESSONS_PATH = os.path.join(os.path.realpath("."), CURR_DIR)
LOGS_PATH = os.path.join(os.path.realpath("."), LOG_DIR)

# SHOULD NOT NEED TO UPDATE THESE
SOLUTION_BRANCH = "solution"
CURRICULUM_BRANCH = "curriculum"
NOTEBOOK_FILE = "index.ipynb"
TIMEOUT = 300
EXECUTE_NB_COMMAND = ["jupyter", "nbconvert", "--to", "notebook", "--inplace", "--execute", f"--ExecutePreprocessor.timeout={TIMEOUT}", NOTEBOOK_FILE]


cwd = os.getcwd()

# STEP 1: CREATE LOGS
# Creates a log file for each lesson
# The log file will contain whatever was sent to STDOUT & STDERR
# when the notebook was run

labs = os.listdir(LESSONS_PATH)

for lab in labs:
    print(f"\nLAB: {lab}")

    os.chdir(f"{LESSONS_PATH}/{lab}")

    # ignore hidden directories (.DS_STORE, etc)
    try:
        files = str(subprocess.check_output(["ls"]))
        branches = str(subprocess.check_output(["git", "branch", "-a"]))
    except:
        continue

    # only care about running notebook when notebook exists!
    if NOTEBOOK_FILE in files:
        subprocess.call(["git", "stash"])

        # does a solution branch exist, if so use that
        if SOLUTION_BRANCH in branches:
            subprocess.call(["git", "checkout", SOLUTION_BRANCH])
        else:
            subprocess.call(["git", "checkout", CURRICULUM_BRANCH])

        subprocess.call(["git", "pull"])
        log_file = f"{cwd}/{LOG_DIR}/{lab}.txt"
        f = open(log_file, "w")
        subprocess.call(EXECUTE_NB_COMMAND, stdout=f, stderr=f)
        f.close()

os.chdir(cwd)

# STEP 2: CLEANUP
# Log-files where the notebook was successfully run can be removed

SUCCESSFUL_EXECUTION_REGEX = "\[NbConvertApp\] Writing [0-9]+ bytes to index.ipynb"
logs = os.listdir(LOGS_PATH)

for log in logs:
    with open(f"{LOGS_PATH}/{log}") as f:
        last_line = list(f)[-1]
        matches = bool(re.search(SUCCESSFUL_EXECUTION_REGEX, last_line))
        if matches:
            os.remove(f"{LOGS_PATH}/{log}")
        else:
            # locally i renamed all labs to start with a number (000-lab-name), so re-rename them here, shouldnt do anything if this is not needed
            filename = re.sub("^[0-9]{3}-", "", log)
            os.rename(f"{LOGS_PATH}/{log}", f"{LOGS_PATH}/{filename}")

# STEP 3: PRINT

logs = os.listdir(LOGS_PATH)

for log in logs:
    print(log[:-4])
