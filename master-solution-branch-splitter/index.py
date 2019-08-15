import json
import os
import subprocess
from git import Repo, Git, GitCommandError
import sys

# CONSTANTS
SOLUTION_TAG = "__SOLUTION__"
CURRICULUM_BRANCH = "curriculum"
MASTER_BRANCH = "master"
SOLUTION_BRANCH = "solution"
CUSTOM_COMMIT_MSG_FLAG = "-m"

# FUNCTIONS


def get_notebook_json(filename="index.ipynb"):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def is_markdown_cell(cell):
    return cell["cell_type"] == "markdown"


def contains_tag(line):
    return SOLUTION_TAG in line.strip().split(" ")


def is_solution_cell(cell):
    if cell["cell_type"] != "code":
        return False

    # does any line of the cell have the SOLUTION tag anywhere in it
    found_tag = [True for line in cell["source"] if contains_tag(line)]

    return bool(len(found_tag))


# removes __SOLUTON__ line from tagged code cells
def untag(cell):
    if cell["cell_type"] != "code":
        return cell

    source = [line for line in cell["source"] if not contains_tag(line)]

    cell.update({"source": source})
    return cell


def create_master_notebook(nb):
    cells = [
        cell for cell in nb["cells"] if for_master(cell)
    ]

    nb.update({"cells": cells})
    return nb


def for_master(cell):
    return is_markdown_cell(cell) or not is_solution_cell(cell)


def for_sol(cell):
    return is_markdown_cell(cell) or is_solution_cell(cell)


def create_sol_notebook(nb):
    cells = [
        untag(cell) for cell in nb["cells"] if for_sol(cell)
    ]

    nb.update({"cells": cells})
    return nb


def notebook_to_markdown():
    subprocess.call(["jupyter", "nbconvert", "index.ipynb",  "--to", "markdown"])
    subprocess.call(["mv", "index.md", "README.md"])


def sync_branch(repo, branch, notebook, msg="Curriculum Auto-Sync"):
    # switch to branch, do nothing if does not exist
    try:
        repo.git.checkout(branch)
        branch_exists = True
    except GitCommandError:
        branch_exists = False

    if branch_exists:
        # get all files from curriculum branch and put onto this branch,
        # (the notebook and readme will be overwritten in the subsequent steps)
        # Interesting use of the `checkout` command
        # https://superuser.com/questions/692794/how-can-i-get-all-the-files-from-one-git-branch-and-put-them-into-the-current-b/1431858#1431858
        repo.git.checkout(CURRICULUM_BRANCH, ".")

        # write index.ipynb
        f = open("index.ipynb", "w")
        f.write(json.dumps(notebook))
        f.close()

        # generate markdown
        notebook_to_markdown()

        # add, commit, push
        repo.git.add(".")
        try:
            repo.git.commit("-m", msg)
            print(f"Added Commit: {repo.commit()}")
        except GitCommandError:
            print("Nothing to commit")

        print(f"pushing to remote {branch} branch")
        repo.git.push("origin", branch)


# RUN
# ======================

git_ssh_identity_file = os.path.expanduser('~/.ssh/id_rsa')
git_ssh_cmd = 'ssh -i %s' % git_ssh_identity_file

Git().custom_environment(GIT_SSH_COMMAND=git_ssh_cmd)

repo = Repo(os.getcwd())
git = repo.git


# get commit message from bash or from repo
try:
    sys_args = sys.argv
    i = list(sys_args).index(CUSTOM_COMMIT_MSG_FLAG)
    custom_msg = sys_args[i + 1]
except:
    custom_msg = None

commit_message = custom_msg if custom_msg else repo.head.commit.message

try:
    git.checkout(CURRICULUM_BRANCH)
except GitCommandError:
    raise Exception(f"A branch called {CURRICULUM_BRANCH} must exist")

notebook_to_markdown()

repo.git.add(".")
try:
    repo.git.commit("-m", commit_message)
except GitCommandError:
    print("Nothing to commit")

# should raise if there are local unstaged changes
print(f"pushing to remote {CURRICULUM_BRANCH} branch")
git.push("origin", CURRICULUM_BRANCH)

notebook_json   = dict(get_notebook_json())
master_notebook = create_master_notebook(notebook_json)
sol_notebook    = create_sol_notebook(notebook_json)

sync_branch(repo, MASTER_BRANCH, master_notebook, msg=commit_message)
sync_branch(repo, SOLUTION_BRANCH, sol_notebook, msg=commit_message)

# leave user on curriculum branch
git.checkout(CURRICULUM_BRANCH)
