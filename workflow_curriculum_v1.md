# Workflow for Curriculum V1


## Step 1: Looking at the Curriculum Spreadsheet

Once assigned a section or brick to work on, look at the curriculum spreadsheet to

1. See to what extent there are existing lessons
2. Look at the "additional notes" column to look at the comments on what to change. In general, lines highlighted in blue denote that substantial changes are needed.

## Step 2: Creating New Pepositories

Depending on whether a lesson existed for Curriculum V0, you will 

1. Copy the existing repository into a new one following [these steps](https://github.com/learn-co-curriculum/dsc-curriculum-guidelines/blob/master/cloning_repositories.md).
2. Create a new repository according to the right format (repository structure guidelines can be found [here](https://github.com/learn-co-curriculum/dsc-curriculum-guidelines/blob/master/lesson_repository_structure.md))

The new repository has a name starts with "dsc-", then a logical name depending on the lesson title eg, "intro-to-KNN". If a lab, the repo name ends with a suffix "-lab". 

## Step 3: Working on a Lesson

The guidelines in this step are mostly important when working on reworking content (where a github repository pre-existed).


### Step 3.1: Check Existing Comments
Before doing anything make sure to

1. Look at the curriculum spreadsheet and be aware of existing comments
2. Look at the pre-existing repository and see if any github issues were created

### Step 3.2: Does this Lesson Make Sense Here?
Before working on anything, do a quick sanity check: does this lesson make sense here? Do students have enough prerequisite knowledge to work on this? Are we not being repetitive? 

If the answer to any of these questions is "no", bring this up in standup or talk to Lore about (re)moving/completely replacing this lesson.


### Step 3.3: Editing a Lesson

Next, make sure to review the and fix for the following main issues

1. Grammatical errors and typos: quick copy paste in a google doc should do the trick.
2. Plagiarism: we are aware of some of our contents being exact copies of pre-existing websites/blogs. Make sure to do due diligence and check for that. Note: borrowed images can stay for now. Once we have an editor we will replace them. We will track images that need to be changed over in airtable (see [airtable section](https://github.com/learn-co-curriculum/dsc-curriculum-guidelines/blob/master/workflow_curriculum_v1.md#step-4-updating-airtable) below)
3. Writing style: make sure to edit academic-sounding passages. Edit academic-sounding language ("shall"), and keep in mind that we want to write in a way that a high school student can understand our curriculum
4. Check for consistency: if you capitalize certain concepts, make sure to capitalize throughout. Eg. in one lab, we talk about the "Grey's Anatomy Romantic Encounters Dataset". First, it's being referred to as _"Romantic Encounters" Dataset_, next as _"romantic" encounters data_, so using different capitalization and quotes. This should be avoided.
5. "Concise yet complete" principle:
	- Is all the text necessary to explain what we want to explain? If answer is “no”: remove text
	- Is everything we want to explain well explained? If answer is “no”: add text/explanation

### Step 3.4: Editing the SWBATs

Once finished (re)writing a lesson, look at the Learning Objectives at the top of the Jupyter Notebook, and make sure to edit if needed.

Note: We use bloom's taxonomy to define the depth of the content in a specific lesson. For a complete overview of Bloom's Taxonomy verbs, go to [this section of the pedagogy wiki](https://education.flatironschool.com/teacher-training/pedagogy/learning-goals.md/#bloom-s-verbs). Note: for curriculum V0, we've overused the verb "understand", so for V1 we'd like to be more creative and use a wide variety of verbs and higher level, ideally in the universe of "applying" and up.


## Step 4: Updating Airtable

Airtable for curriculum V1 can be found [here](https://airtable.com/tblBxmAzJeLlm7iXV/viwHgTRCOuetiEKwK?blocks=hide).

**IMPORTANT: Airtable is our reporting tool to our management. We want to keep it up-to-date on where we stand, because this is the only way for them to see our progress**

Once a lesson is ready for V1, make sure to update airtable:

- The Lesson name should be an **exact match** with the `index.ipynb` title
- Status should be set to "To Review"
- Make sure to review duration time and adjust if needed
- Add in the new github repo URL
- Select the appropriate *tag* (note: the tag universe is exhaustive, so no new tags can be added unless discussed. Tag wisely! One lesson should have 1-5 tags)
- Copy over SWBATs from your jupyter notebooks: SWBATs in airtable should be **exact matches** of what's in the notebook
- Add in the data set used in your lesson, if any. Check if the data set has been used before and select if it's in airtable already. If not, create a new data set
- Note if there are images that need to be recreated by a designer: add tag "yes" or "no"

## Step 5: Wrapping up a whole Section

(Re)writing the section (or brick) intro and recap should always be the last thing a curriculum writer does when writing a section. 

The naming convention for intro and recap is:

"dsc-section-recap-xxxxx" <br />
"dsc-introduction-xxxxx" 

with xxxxx being some wording related to the section name, eg the for the K Nearest Neighbors section you could write

"dsc-introduction-knn"  <br />
"dsc-section-recap-knn"

