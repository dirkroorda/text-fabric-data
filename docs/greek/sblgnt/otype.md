---
title: otype
---

**node type**

Types for text objects.
As text objects are represented by nodes in
[Text-Fabric](https://github.com/annotation/text-fabric),
we shall use both *object* and *node* without much consistency.  

---|---|---
`word`         |slot          |single word, fills a *slot*; sometimes words are not separated by a space
`phrase`       |tree          |phrase, maybe with gaps
`clause`       |tree          |clause, maybe with gaps
`clause_atom`  |tree          |maximal consecutive part of a clause
`sentence`     |tree          |clause, maybe with gaps
`wordx`        |??            |conversion artefact, derives from nodes categorized as words, but having child nodes
`verse`        |section       |numbered unit of a chapter
`chapter`      |section       |numbered unit of a book
`book`         |section       |named and numbered part of the Bible

All objects have a type, which is just a label.
Objects and their slots are represented in Text-Fabric as *nodes*.
The information which object occupies which slot is stored in the edge feature [oslots](oslots).

---|---
[Section types](#section-types)        |division in books, chapters, etc
[Word type](#word-type)                |all about the individual words
[Linguistic types](#linguistic-types)  |phrases, clauses, etc

# Section types

The section types correspond to the various divisional units in the Bible.
The Greek New Testament is divided in books, books are divided in chapters, chapters are divided in verses.
The sectional types
`book`, `chapter`, and `verse`
specify features which indicate which book, chapter, and verse their objects refer to.

A `book` object carries the [book](book) and [book](booknum) features, which contain the name and number of the book.
A `chapter` object carries the [chapter](chapter) feature, which contains the number of the chapter.
A `verse` object carries the [verse](verse) feature, which contains the number of the chapter.

# Word type

There is only one type for words, the `word` type.
Word objects correspond to the smallest divisional units in the SBLGNT dataset.
They are also identified with *slots*, because each slot is filled by a word and each word fills a slot.
Words are not identified with strings, because there are various
string representations of the words, none of which is canonical. All word occurrences are numbered
with a slot number.

The text of a word occurrence is in
[Unicode](Unicode) (full Unicode Greek).
This feature contains punctuation material from in between words, but no spaces.

Word occurrences corresponds to lexemes, i.e. dictionary entries, for which we do not have a separate object type.
For the textual representation of lexemes we have the feature:

---|---
[UnicodeLemma](UnicodeLemma) | full Unicode Greek

# Linguistic types

Linguistic types correspond to syntactical entities such as sentences, clauses and phrases.

During conversion from the original treebanks we have based our object types on the `Cat` attribute of the 
`<node>`-element. This is the translation table we have used

Cat value | otype
---|---
`np` | `phrase`
`CL` | `clause`
`vp` | `phrase`
`noun` | `word`
`verb` | `word`
`V` | `clause_atom`
`det` | `word`
`ADV` | `clause_atom`
`S` | `clause_atom`
`conj` | `conjunction`
`pron` | `word`
`pp` | `phrase`
`prep` | `word`
`O` | `clause_atom`
`adjp` | `phrase`
`adj` | `word`
`advp` | `phrase`
`adv` | `word`
`P` | `clause_atom`
`IO` | `clause_atom`
`VC` | `clause_atom`
`ptcl` | `word`
`nump` | `phrase`
`num` | `word`
`intj` | `word`
`O2` | `clause_atom`

In the SBLGNT, clauses are subtrees of whivh the top node has `Cat=CL`.
Below it are nodes with `Cat` indicating the function of the clause.
We have called these subtrees `clause_atom`s.

The label `S` is special: root nodes of trees carry `Cat=S`, and then `S` means sentence.
These nodes become `sentence` nodes in Text-Fabric.
Otherwise they become `clause_atom` nodes.

Sometimes `<node>`s with a `Cat` that we translate to `word`, still have child nodes.
We give the node type `wordx` to such nodes.
Only terminal nodes get the node type `word`.
