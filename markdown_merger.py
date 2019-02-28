import subprocess
import json
import copy
"""A little script for transcribing markdown changes in IPYTHON Notebooks to alternate branch versions.
Ideally you should alias this script as mm; nicknamed after the author.
For example: Add this to your .bash_profile:
alias mm='python /Users/matthew.mitchell/Documents/Tools/Repo_Tools/markdown_merger.py'
Or wherever your local copy of the script lives.
"""
def run_cmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    printout = output.decode()
    return printout

def merge_markdown(filename='index.ipynb', branch2merge=None):
    """Merges the markdown contents from the alternate branch into the current branch.
    For example, if run on the master branch, the markdown contents from the solution branch will be copied over to the master branch.
    User may also manually specify which branches markdown contents to merge into the current version of index.ipynb using the optional parameter branch2merge.
    """
    #Determine current branch
    printout = run_cmd("git branch")
    # print(printout)
    branches = printout.split('\n')
    for n, line in enumerate(branches):
        if '*' in line:
            cur_branch = line.replace('*','').strip()

    #Determine number of markdown cells
    with open(filename) as f:
        notebook = json.load(f)
    contents = notebook['cells']
    cur_n_md = sum([1 for cell in contents if cell['cell_type']=='markdown'])
    #Checkout other branch
    try:
        if branch2merge:
            printout = run_cmd("git checkout {}".format(branch2merge))

        elif cur_branch == 'master':
            printout = run_cmd("git checkout solution")
        elif cur_branch == 'solution':
            printout = run_cmd("git checkout master")
        else:
            print('Please specify branch and rerun.')
    except:
        print('Could not find other branch.')
        return None
    #Save markdown contents of other branch
    with open(filename) as f:
        notebook = json.load(f)
    contents = notebook['cells']
    md2merge = [cell['source'] for cell in contents if cell['cell_type']=='markdown']
    #Check whether number of markdown cells match
    assert (len(md2merge) == cur_n_md), "Number of markdown cells does not match! Manual intervention required."
    #Revert back to original branch
    printout = run_cmd("git checkout {}".format(cur_branch))
    #Overwrite index.ipynb markdown contents with cached version
    with open(filename, 'rb') as f:
        notebook = json.load(f)
    contents = copy.deepcopy(notebook['cells'])
    md_cell_n = 0
    for n, cell in enumerate(contents):
        if cell['cell_type'] == 'markdown':
            notebook['cells'][n]['source'] = md2merge[md_cell_n]
            md_cell_n += 1
        else:
            continue
    #Save to File
    with open(filename, 'w') as outfile:
        json.dump(notebook, outfile)
    #Copy to Markdown
    printout = run_cmd("jupyter nbconvert --to markdown index.ipynb")
    printout = run_cmd("mv index.md README.md")

merge_markdown()