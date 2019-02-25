# Repository structure for DS lessons

## Lessons
There are three main types of flatiron lessons:

- Readme
- Lab
- Codealong

A **lesson** lives in a **github repository**. One repository can only contain one lesson. Repositories are created on the learn-co-curriculum organization and should be set to **public**.


## Lesson Repositories


Each repository contains the following files (see template repositories below for the files):

- `.gitignore` 
- `.learn` 
- `CONTRIBUTING.md`
- `LICENSE.md`
- `index.ipynb`
- `README.md`
- `images`-folder containing images (only if images are being used). Image file names should be *fully lower case (extension included)*.

Your main working document will be the `index.ipynb`, which will contain the curriculum you create. You will later [convert the notebook into a markdown file](#generating-readmemd-from-indexipynb), the `README.md`.

We'll discuss specifics for each lesson type below.

### Readme

You can find the correct template repository for Readmes, with all the necessary files, [here](https://github.com/learn-co-curriculum/dsc-template-readme).

Please make sure to change the title to the appropriate topic, add an introduction, objectives (which should be taken from the lesson's outlined SWBATS), the lesson's content, and summary.


### Lab
You can find the correct template repository for Labs, with all the necessary files, [here](https://github.com/learn-co-curriculum/dsc-template-lab).

A lab is different from a readme in three ways:

- the title has a suffix " - Lab"
- There is a "pytests" folder in there containing a  `test_index.py` file
- Has a `master` and a `solution` branch. `master` and `solution` are identical, except for the code cells in the jupyter notebook. `master` doesn't contain the code solution, and `solution` does.

Please make sure to change the title to the appropriate topic and leave the `- Lab` to indicate that this is a lab. Next add an introduction, objectives (which should be taken from the lab's outlined SWBATS), the lab's content, and summary.

Students need to come up with code in Labs. Therefore, all labs should have **Instructions:** that give a stepped flow to the Lab's content. 

* Instructions should be be specific. Students shouldn't have to make assumptions about what to do based on the instructions, they should immediately know.  
* Instructions should be written in order of how to approach the lab. If you need to build a class before you can define any methods, the instructions should lead the student to build the class first.

### CodeAlong

In terms of structure, a CodeAlong is identical to a Readme, but may contain more code examples and is generally more hands-on. All the code must live on `master` and students are not assumed to come up with any code. 

## Generating `README.md` from `index.ipynb`

How to generate `README.md` from `index.ipynb`? Using command line, just make sure you're in the right directory:

`$ cd dsc-correct-directory`

Once you're in the right directory, copy the following command and change the commit message. This command will convert your index.ipynb to markdown, rename it to `readme.md`, and will add and commit at the same time.

`$ jupyter nbconvert --to markdown index.ipynb && mv index.md README.md && git add -A && git commit -m "commit message"` 





