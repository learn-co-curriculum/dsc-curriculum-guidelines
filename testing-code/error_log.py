import os
import shutil
import subprocess
from contextlib import redirect_stdout
import re
import pandas as pd

# ACTION REQUIRED: Edit these to be the names of the appropriate directories
# LOG_DIR = make an empty directory where the log files will be created
# CURR_DIR = wherever your local copies of all labs live
LOG_DIR = "currlogs_curriculum"
CURR_DIR = "curriculum"

# ACTION REQUIRED: update these paths as appropriate
# the provided default assumes this script will be run from
# a directory containing both the LOG_DIR and CURR_DIR
LESSONS_PATH = os.path.join(os.path.realpath("."), CURR_DIR)
LOGS_PATH = os.path.join(os.path.realpath("."), LOG_DIR)

# ACTION REQUIRED: update this to the jupyter kernel being used
KERNEL="python3"

# SHOULD NOT NEED TO UPDATE THESE
SOLUTION_BRANCH = "solution"
CURRICULUM_BRANCH = "curriculum"
NOTEBOOK_FILE = "index.ipynb"
TIMEOUT = 600
EXECUTE_NB_COMMAND = [
    "jupyter",
    "nbconvert",
    "--to", "notebook",
    "--inplace",
    "--execute",
    f"--ExecutePreprocessor.timeout={TIMEOUT}",
    f"--ExecutePreprocessor.kernel_name={KERNEL}",
    NOTEBOOK_FILE
]


cwd = os.getcwd()

# STEP 1: CREATE LOGS
# Creates a log file for each lesson
# The log file will contain whatever was sent to STDOUT & STDERR
# when the notebook was run

print("Executing lesson code...\n")

lessons = os.listdir(LESSONS_PATH)

for lesson in lessons:
    # ignore directories that start with .
    if lesson.startswith("."):
        continue
    
    print(f"\nLESSON: {lesson}")

    os.chdir(f"{LESSONS_PATH}/{lesson}")

    try:
        # ignore hidden directories (.DS_STORE, etc)
        files = str(subprocess.check_output(["ls"]))
        branches = str(subprocess.check_output(["git", "branch", "-a"]))
    except:
        continue

    # only care about running notebook when notebook exists!
    if NOTEBOOK_FILE in files:

        # does a solution branch exist, if so use that
        if SOLUTION_BRANCH in branches:
            subprocess.call(["git", "checkout", SOLUTION_BRANCH])
        # otherwise try to use the curriculum branch
        elif CURRICULUM_BRANCH in branches:
            subprocess.call(["git", "checkout", CURRICULUM_BRANCH])

        log_file = f"{cwd}/{LOG_DIR}/{lesson}.txt"
        with open(log_file, "w") as f:
            subprocess.call(EXECUTE_NB_COMMAND, stdout=f, stderr=f)

        subprocess.call(["git", "restore", "."])

os.chdir(cwd)

# STEP 2: CLEANUP
# Log-files where the notebook was successfully run can be removed
print("\nCleaning up log files...\n")

SUCCESSFUL_EXECUTION_REGEX = "\[NbConvertApp\] Writing [0-9]+ bytes to index.ipynb"
known_to_error = pd.read_csv("known_to_error.csv")

logs = os.listdir(LOGS_PATH)

for log in logs:
    if log.startswith("."):
        shutil.rmtree(f"{LOGS_PATH}/{log}")
        continue
    
    with open(f"{LOGS_PATH}/{log}") as f:
        last_line = list(f)[-1]
        matches = bool(re.search(SUCCESSFUL_EXECUTION_REGEX, last_line))
        if matches:
            print(f"Removing {log} because it executed successfully")
            os.remove(f"{LOGS_PATH}/{log}")
        # "slug" is the part before the .txt in the log name and after
        # learn-co-curriculum/ in the URL
        elif log[:-4] in known_to_error["slug"].values:
            row = known_to_error[known_to_error["slug"] == log[:-4]].reset_index()
            reason = row.at[0, "reason"]
            notes = row.at[0, "notes"]
            print(f"""Removing {log} because it is known to error
            Reason: {reason}
            Notes: {notes}""")
            os.remove(f"{LOGS_PATH}/{log}")

# STEP 3: PRINT
print("\nPrinting lessons with errors...\n")

logs = os.listdir(LOGS_PATH)

for log in logs:
    print(log[:-4])
