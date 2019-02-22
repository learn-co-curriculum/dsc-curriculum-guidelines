# Style Guide

## Introduction

To ensure that we all write with a common voice, we have adopted the following
style decisions.

Contents:

* Flatiron Concerns
  * [American English Standard](#american_dictionary)
  * [Do Not Mention Dates](#do_not_mention_dates)
* Formatting Markdown
  * [Code Words](#code_words)
  * [Code Blocks](#code_blocks)
  * [Lists and Bullets](#lists_and_bullets)
  * [Tables](#tables)
  * [Quotes](#quotes)
  * [Math](#math)
* Style
  * [Python Style Guide](#python_style)
  * [Python Libraries](#python_libraries)
  * [Abbreviations](#abbreviations)
  * [Capitalization](#capitalization)
  * [Asides](#asides)
  * [Numerology](#numerology)
  * [Disambiguation of "learn"](#disambiguation_of_learn)
* Engaging Writing
  * [Tone](#tone)
  * [Personhood](#personhood)
  * [Non-Gendered Speech](#non-gendered_speech)
  * [Avoid Value Judgements](#avoid_value_judgements)
  * [Prefer Active Voice](#prefer_active_voice)
  * [Write from the Student Perspective](#write_from_the_student_perspective)
  * [Avoid Rhetorical Questions to Drive Material](#avoid_rhetorical_questions_to_drive_material)

---

## Flatiron Concerns

<a name="american_dictionary"></a>

### American English Standard

We draw from the American English dictionary. It's a "hood" not a "bonnet", "modeling" and not "modelling", a "color" not a 
"colour" et al.

<a name="do_not_mention_dates"></a>

### Do Not Mention Dates

Do not specify delivery-specific concerns in the text. The "first Monday of the
module" seems specific, obivious, and routine, but in the US Market, many
holidays fall on Monday such that this won't be appropriate. As Flatiron has an
ever wider presence we will run against cultures that work on Friday, don't
work on Saturday, etc.

## Formatting Markdown

Use [GitHub-flavored markdown][GHMD].

<a name="code_words"></a> 

### Code Words

When discussing a "code word" as part of a regular sentence, wrap the code word
in single back ticks ( \` ). This could be a variable name (`myString`), a
class name (`NSArray`), a method name (`.include?`), an operator (`<=>`), or a
string literal (`"Hi, Grandma."`); in general, any piece of code that does not
constitute a whole line or statement.

Avoid beginning a new sentence with a code word whenever possible

Not: `pwd` means "print working directory".  
Use: The `pwd` command means "print working directory".  

<a name="code_blocks"></a>

### Code Blocks

```python
import pandas as pd
import numpy as np
train = pd.read_csv("C:/desktop/data/titanic.csv")
```

"Code blocks" are declared by wrapping in triple back-ticks ( ``` ). The
opening triple back-tick should be followed with a language declaration
appropriate to the contents of the code block:

* `python`: Python
* `bash` : Bash, CLI output
* `ruby` : Ruby
* `js`   : JavaScript
* (none) : LLDB console output

<a name="lists_and_bullets"></a>

### Lists and Bullets

1. Lists can be automatically numbered,
   * and contain bullet points.

* Or they can be unnumbered (bulleted) lists.

2 — You can also manually number your list if the automatic numbering gets
broken because of a code-snippet.

But, keep a consistent style. Consider using an aside instead of lists with only one point.

If you reference other bullets use numbered list. 

At the end of a sentence on a bullet **do not** add a period. If multiple sentences
are present in the bullet, punctuate as normal but leave the period off the last statement.

<a name="tables"></a>

### Tables

Tables are a great way to organize sets of parallel information, such as
[logical
operators](https://github.com/learn-co-curriculum/reading-ios-looping-and-conditionals#combining-conditionals).

Try to keep the Markdown symbols as table-like as possible, wrap symbols in
code snippets, and use markdown reference notation for icon links inside a
"cell". These will improve future maintainability of the code.

<a name="quotes"></a>

### Quotes

#### Block Quote

>You can employ an HTML-style block quote by starting the first line with an
>`>`. This is better for large excerpts when line breaks don't matter.
>(attribution or link)

More commonly a block quote will be appropriate when quoting a technical work,
programming documents, or a blog.

#### In-Line Quote

When writing an "in-line quote", punctuation should remain outside the phrase
"unless you are making a reference quote that includes it." Punctuation symbols
can have technical importance to the subject matter so explicitly excluding
punctuation from quotes is justifiable.

#### Do Not Use Curly-Quotes or Smartquotes

No: curly quotes: `”` or smart quotes: “Why”
Also no: &raquo; &laquo;. 
Use American quotation formatting: "Why"

<a name="math"></a>

### Math

In markdown, we use LaTeX for mathematical expressions. Some guidelines:
- Every mathematical expression or variable should be denoted in LaTeX-style format, even if what we are trying still makes sense when using the standard format.  
**Do**: "We define $f(x)$ a function of $x$." **Don't**: "We define f(x) a function of x."
- Use $\dfrac{}{}$ instead of $\frac{}{}$ to get fractions that don't look ridiculously small.


## Style

<a name="python_style"></a>

### Python Style Guide

For any Python code, we use Python guru Guido Van Rossem's "PEP 8 -- Style Guide for Python Code", to be found [here](https://www.python.org/dev/peps/pep-0008/)

<a name="python_libraries"></a>

### Python Libraries Naming Conventions

Python code will often start with library imports. Some examples:

```python
import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
```
The libraries stated above are used **very** often. You'll see that `pandas` will almost everywhere be imported as `pd`, `numpy` as `np`, etc. It is important to be consistent, because code like this will break:

```
pd.read_csv("C://anyfolder/anyfile.csv")
```
when you simply use `import pandas` or name it differently. We encourage writers to be very consistent in naming libraries when importing them, and to make sure to do a quick check on what the naming conventions are when importing new (and less common) libraries. 


<a name="abbreviations"></a>

### Abbreviations

Technological writing is full of initialisms, acronyms, and abbreviations. As our
audience is quite likely to be unfamiliar with them, **any
abbreviation may be used _only after it is introduced_**.

Incorrect:

```
You can use AR to access the database...
```

Correct:

```
You can use ActiveRecord ('AR') to access the database...
```

<a name="capitalization"></a>

### Capitalization

Names of languages should be capitalized unless part of a code snippet (e.g.
Ruby or `ruby`, Objective-C, Python or `python`; not: ruby, objective-c,
python).  

Don't capitalize:

* bash — the commonly-used acronym for Bourne-Again SHell.
* boolean — though in specific reference to the fields of Boolean Algebra or Boolean Logic this can be appropriate, just be consistent.

**Do** capitalize:

* *most acronyms:* CLI, URL, HTTP, LLDB.
* *names of programming languages:* Python, Ruby, Objective-C, Swift, JavaScript
* Interface Builder — Xcode's integrated storyboard design tool.
<a name="asides"></a>

In **headers**, capitalize *every* word except: "a," "an," "and," "at," "but," "by," "for," "in,"
"nor," "of," "on," "or," "out," "so," "the," "to," "up," and "yet."

### Asides

Use asides sparingly. Some examples:

**Note:** *The basic aside for "whispering" something minor that doesn't fit
into the flow of exposition.*  Example:

**Note:** You might find that your version differs in its third number versus
what we have in our example. We use 2.7.2, but 2.7.3 would work just fine.

**Advanced:** *A helpful note that is not readily understandable to the present
skill level of the reading and not required to fulfill the objectives.*
Example:

**Advanced:** If you notice that you're repeating yourself a lot in these specs,
you might want to try using a `let` block to DRY out the code. Consult the
documentation...

**Pro-tip:** *A note about style or best-practice, or a friendly reminder about
avoiding a common or simple mistake. Think opinion-piece.* Example: 

**Pro-tip:** Since launching the debugger console is a *very* common task when
writing JavaScript, you might want to learn the shortcut: &#8984; + &#8997; +
j.

**Hint:** (in labs) *A note about avoiding a common mistake not readily
apparent in the given instructions, or direction to a useful method that has
not been previously explained.* Example:

**Hint:** Your first insinct might be to reach for `.each`, but since you're
accumulating the values, there might be a better Enumerable.

**Reminder:** *A reminder of previously learned concepts as we start to build
on them.* Example:

**Reminder:** JavaScript does not have implicit `return` in its functions. If
you pass a closure in, you might be surprised unless you're careful about what
you return!

<a name="numerology"></a>

### Numerology

When discussing numbers in exposition paragraphs, remember the English rule
that numbers from zero to ten should be written out and values over 1,000
should be written with comma separators. Since this can collide with discussing
code, think of the use case to determine what you're talking about. Are you:

* discussing the number only in your exposition? Use the English form. 
* discussing an integer value from your code? Put the digit `10` in a code
  snippet. 
* discussing an abstract count that's relevant to your code? Do both, by
* presenting it as ten (10) or ten (`10`).

<a name="disambiguation_of_learn"></a>

### Disambiguation of "learn"

Because of our appropriation of the word "learn" among our curriculum software,
disambiguating its use is important:

* learn — verb — to gain knowledge or improve a skill. 
* `learn` command, the — noun phrase (as, "the `learn` command") — the bash
  command that runs all tests in labs. This should always be wrapped in
  a code snippet.
* Learn.co — proper noun — the website and address of the curriculum tool
  available to students, faculty, and staff.
* Learn IDE, the — proper noun — the application that students use to work
  through the Learn.co curriculum.

Usage:

"You'll learn that the `learn` command integrates with your profile on Learn.co
by uploading information through the Learn IDE."

## Engaging Writing

<a name="tone"></a>

### Tone

Tone should be conversational. It is appropriate to "break the fourth wall" and
speak to the reader using "you."

Per our "[Brand Book][bb]," here are attributes that our voice should have:

#### Passionate

Optimistic, Positive, Purposeful **over** Apathetic, Sarcastic, Detached

#### Rigorous

Elite, Determined, Eager **over** Elistist, Gentle, Easy

#### Knowledgable

Trustworthy, Useful, Transparent **over** Uninformed, Unhelpful, Overtly Salesy

<a name="personhood"></a>

### Personhood

Curriculum should be writen in first-person plural (We).

<a name="non-gendered_speech"></a>

### Non-Gendered Speech

We do not use "he" or "she" or "ze" or "wir" or "hir."

We use "they" as a third-person singular honoring the descriptivist tendencies
of pre-18<sup>th</sup> century usage.

<a name="avoid_value_judgements"></a>

### Avoid Value Judgements

Learners, especially in technology, will tend to mimic our opinions
about technology. A statement such as: "We'll be using Ruby, because this would
be Hell on Earth in Java" is often humorous for the experienced, but will be
taken and parroted by neophytes in ways that might be dangerous to their
outcomes. Imagine they walk into an interview at a Big Bank and are asked about
what technology to use for online banking and they suggest Ruby because "Java
is Hell on Earth."

Also, be aware imputation or inference of values can set up learners' sense of
impostor syndrome.

> "This is a simple and elegant interface."

If the student reads those value words, they may well feel "stupid" if the
matter doesn't come easily for them. Lacking sufficent taste the Rack
middleware's _elegance_ might be lost on them and they will conclude it is
_them_ who is "stupid" because the elegance of a responder with a single method
is not something that has become native to their mental map of the programming
universe.

<a name="prefer_active_voice"></a>

### Prefer Active Voice

While **it is unnatural to avoid all passive construction**, strive for active
voice as much as possible. Implicit here is that **it's permissible to use the
imperative mood** when warranted since we _are_ experts.

Prefer:

> Start the server.

or:

> You must start the server before attempting to connect.

over:

> The server must be started by you before it can be reached.

<a name="write_from_the_student_perspective"></a>

### Write from the Student Perspective

While this seems to be natural enough, keeping your goals separate from the
students' perspectives can often become muddled.

First, it is **absolutely fine** for Flatiron to indoctrinate Flatiron values.
This guide, in many ways, does exactly that. By expressing an opinion on how
we handle gender and personhood, we are expressing a value. Expressing
the enthusiasm we have in our corporate culture about technology is fine.

That said, both code and text needs to be written for where the _students'_
values and knowledge are, _not the curriculum authors'_. Consider that, as a
developer, we know a `let` block is a great way to DRY up a spec. But is a
student on their 3rd test-driven lab going to be able to handle the attending
questions e.g.:

* Am I **wrong** if I don't use `let`
* Will I not get a job if I don't use `let`
* This test is failing, did someone make a mistake by using `let`?

<a name="avoid_rhetorical_questions_to_drive_material"></a>

### Avoid Rhetorical Questions to Drive Material

It's tempting to "plant" a rhetorical question in order to set up material.
Often, however, this work is not required. They're reading a lesson expecting
to have material presented. Speaking with authority, especially in earlier
courses, creates safety that allows them to learn comfortably.

[80col]: https://www.emacswiki.org/emacs/EightyColumnRule
[GHMD]: https://help.github.com/categories/writing-on-github/
[gitlab-sg]: https://about.gitlab.com/2016/10/11/wrapping-text/
[kernel-style]: https://www.kernel.org/doc/html/v4.10/process/coding-style.html#breaking-long-lines-and-strings
[atom-hard-wrap]: https://atom.io/packages/hard-wrap
[bb]: https://flatiron.atlassian.net/wiki/spaces/ER/pages/330104842/Flatiron+School+Brand+Book
