# Repository Structure for DS Lessons

## Lesson Types

There are three main types of Flatiron DS lessons:

- Reading
- Lab
- Codealong

Each **lesson** lives in a separate **GitHub repository**. One repository can only contain one lesson. Repositories are created on the `learn-co-curriculum` organization and should be set to **public**. The sequence of curriculum content is laid out in **Airtable** (not in a public repo).

## Lesson Repositories

Each repository should contain the following files (see template repositories below for the files):

- `.gitignore`
  - Should be a Python gitignore file
- `CONTRIBUTING.md` and `LICENSE.md`
  - Legal boilerplate explaining how our curriculum content can be used and how to contribute
- `README.md`
  - "Home page" of the lesson, written in Markdown
  - The H1 at the top of this file (i.e. the thing following the `# `) becomes the title of the lesson in Canvas

Additionally, most curriculum repositories contain a **Jupyter Notebook file** called `index.ipynb`.

> If the repository has an `index.ipynb`, **always** make edits in that file on the `curriculum` branch and the branch splitter script will automatically update the `README.md` for you. If the repository doesn't have an `index.ipynb` there typically will not be a `curriculum` branch and you can make edits directly to the `README.md` file.

What about the `.canvas` files? You will also see them in some/most repos. The idea is that they connect the repo to all of the places on Canvas where that lesson appears. Right now for DS these files are largely out of date and should not be relied on as a "source of truth" about where the content exists in the curriculum. The Airtable is a better source of truth, and the Canvas blueprints themselves are even better.

We'll discuss specifics for each lesson type below.

### Readings

Readings may or may not include Python code. The general idea that distinguishes a reading from other lesson types is that it should "just work", i.e. that students shouldn't need to take any particular actions other than opening it up in order to get the information they need.

An example reading with an `index.ipynb` and all the necessary files can be found [here](https://github.com/learn-co-curriculum/dsc-curriculum-template-reading).

### Labs

Labs almost always include Python code. (The exception being e.g. Git labs that require some other type of user activity.) The general idea distinguishing a lab from other lesson types is that the student will need to do something in order to get the code to work. Sometimes they start from a blank cell, and other times they start with incomplete/broken code.

Other distinguishing features of labs:

- The title should have a suffix " - Lab"
- There should be a `solution` branch
  - See the `master-solution-branch-splitter` directory of this repository for more information about how this works
- The Markdown should contain instructions for what the student is supposed to do

An example lab with all the necessary files can be found [here](https://github.com/learn-co-curriculum/dsc-curriculum-template-lab).

### Codealongs

Codealongs are fairly rare and fairly quirky within the curriculum. They might be formatted more like a reading or more like a lab.

One technique you can use to hide the solution but keep it reasonably accessible is to use an HTML `<details>` element in a Markdown cell. This element is used in a lot of menus online, and lets you toggle whether content is expanded or collapsed. A general template for this element is:

---

<details>
    <summary style="cursor: pointer"><b>Hint (click to reveal)</b></summary>
    
If you leave a blank space above and below (separating the internal content from the HTML), ***Markdown styling*** will work, including for code blocks. Pretty cool!

```python
int x = 5
```
    
</details>

---

(You can copy the code above by viewing the raw source of this Markdown page.)

You'll also often see a `---` above or below a `<details>` tag. This is a "horizontal rule" (AKA `<hr>` tag in HTML) that is normally used for a "thematic break" in technical writing, but it also can just be a nice way to add some vertical space if the `<details>` tag is looking too crowded.

If you use a `<details>` tag you can ask a student to code something but make the solution very easy to access (not separated off in the `solution` branch).

Using this kind of tag is not limited to codealongs; it can be used in readings and labs, too! It just tends to come up more often in codealongs.

### How to Use Reading and Lab Templates

These are the "template" repos for readings and labs:

* https://github.com/learn-co-curriculum/dsc-curriculum-template-reading
* https://github.com/learn-co-curriculum/dsc-curriculum-template-lab

There is no specific set way to use them. Options include:

1. Cloning them locally so you can copy files from them into a new lesson
2. Using `wget` to pull the raw source into a new lesson
3. Creating a new lesson but not initializing it, then importing all of the template content

Of these options, only the third one will retain the commit history for the template. It depends on the context whether that matters.

One thing we are _not_ planning to do (for now) is make these templates into actual [GitHub template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) repositories and then create new lessons within GitHub based on the template. The reason for this is that the resulting lessons would have a "generated from" link at the top that would make things look inconsistent.

## Lesson Content

### Markdown

Any text that is not code in our curriculum is written in Markdown. The same content will show up in multiple "flavors" of Markdown (Jupyter Notebook, GitHub, VS Code, gem used to add stuff to Canvas) and there will be some things that are slightly different (e.g. images centered in some places and left aligned in others). We therefore generally use pretty plain/basic Markdown formatting in our lessons and are not trying to be web designers writing a bunch of custom HTML. You can add more visualizations or other images if the lesson is getting boring!

Regardless of whether the lesson is written in the `index.ipynb` or `README.md` file, there are some format best practices that the Markdown should follow:

1. Title
   - The lesson title should be at the top, with `# ` in front of it
   - Words in all titles are capitalized, **except** articles (a, an, the), conjunctions (and, but, for,...), short prepositions (at, by, from,...)
   - Avoid using any punctuation or special characters
   - Lesson title in Jupyter Notebook and title on Airtable should **match exactly**
      - If they don't match, this is a problem and should be fixed
2. Introduction
   - This comes immediately after the title, with `## ` in front of it
   - Write in complete sentences, introducing the lesson
   - If possible try to avoid making explicit statements about the sequence of the curriculum, e.g. mentioning that they "just" did a particular lab. It's fine to connect back to something that is a prerequisite for understanding the lesson
3. Objectives
   - This comes immediately after the objectives, with `## ` in front of it
   - Make sure you leave a blank line above and below the list of objectives. This will help the `github-to-canvas` gem parse the lesson header appropriately
   - Each SWBAT in the list should start with a verb and should not be a complete sentence
   - Objectives should also be entered into Airtable. A single objective can be linked to multiple lessons if appropriate
4. Lesson content
   - Each part of the lesson content should have a heading with `## ` in front of it. You can also have smaller headings with `### `. Technically `#### ` also works although those can start to get hard to distinguish
5. Summary
   - This comes immediately after the lesson content, with `## ` in front of it
   - Write in complete sentences, wrapping up the lesson

### Code

Python code should be written so that the `curriculum` or `solution` branch notebook cells can all be executed in order. There should not be any errors produced unless it is intentionally demonstrating a type of error to the students, and in that case should be clearly indicated.

For labs, code cells should be written in pairs:

1. First, a cell for the `master` branch. There is no special indicator for these
2. Second, a cell for the `solution` branch. This cell should start with `# __SOLUTION__`

These cells can otherwise be identical (e.g. you want to have a bunch of imports for the student as well as in the solution) or you can have starter code (or even a blank cell) on the `master` branch and solution code on the `solution` branch.

**All code should be written in the `index.ipynb` on the `curriculum` branch** and then you use the branch splitter described in the `master-solution-branch-splitter` directory of this repository to generate the READMEs and separate out the `master` and `solution` branch content.

## Style

For specific details on the writing and format style for both Markdown and code, see the `style_guide.md` file in this directory.
