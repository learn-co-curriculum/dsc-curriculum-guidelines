import json
import os
import subprocess
from git import Repo, Git, GitCommandError

# CONSTANTS
SOLUTION_TAG = "__SOLUTION__"
CURRICULUM_BRANCH = "curriculum-team"
MASTER_BRANCH = "master"
SOLUTION_BRANCH = "solution"

# FUNCTIONS
def get_notebook_json(filename="index.ipynb"):
    with open(filename, 'r') as f:
        data= json.load(f)
    return data

def is_markdown_cell(cell):
    return cell["cell_type"] == "markdown"

def contains_tag(line):
    return SOLUTION_TAG in line.strip().split(" ")

def is_solution_cell(cell):
    if cell["cell_type"] != "code": return False

    # does any line of the cell have the SOLUTION tag anywhere in it
    found_tag = [True for line in cell["source"] if contains_tag(line)]

    return bool(len(found_tag))

# removes __SOLUTON__ line from tagged code cells
def untag(cell):
    if cell["cell_type"] != "code": return cell

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

def sync_branch(repo, branch, notebook):
    # switch to branch if exists or create new branch
    try:
        repo.git.checkout(branch)
    except GitCommandError:
        repo.git.checkout("HEAD", b=branch)

    # write index.ipynb
    f = open("index.ipynb", "w")
    f.write(json.dumps(notebook))
    f.close()

    # generate markdown
    subprocess.call(["jupyter", "nbconvert", "index.ipynb",  "--to", "markdown"])
    subprocess.call(["mv", "index.md", "README.md"])

    # add, commit, push
    repo.git.add(".")
    try:
        repo.git.commit("-m", "Master-Solution Auto Sync")
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

# should raise if there are local unstaged changes
git.push("origin", CURRICULUM_BRANCH)

try:
    git.checkout(CURRICULUM_BRANCH)
except GitCommandError:
    raise Exception(f"A branch called {CURRICULUM_BRANCH} must exist")

notebook_json   = get_notebook_json()
master_notebook = create_master_notebook(dict(notebook_json))
sol_notebook    = create_sol_notebook(dict(notebook_json))

sync_branch(repo, MASTER_BRANCH, master_notebook)
sync_branch(repo, SOLUTION_BRANCH, sol_notebook)

# clean up
git.checkout(MASTER_BRANCH)
