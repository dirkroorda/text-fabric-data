---
title: otype
---

**node type**

Types for text objects.
As text objects are represented by nodes in
[Text-Fabric](https://github.com/Dans-labs/text-fabric/wiki),
we shall use both *object* and *node* without much consistency.  

---|---|---
`letter`       |slot          |single letter, fills a *slot*; sometimes letters are followed by a space
`word`         |tree          |word
`verse`        |section       |numbered unit of a chapter
`chapter`      |section       |numbered unit of a book
`book`         |section       |named file in the corpus

All objects have a type, which is just a label.
Objects and their slots are represented in Text-Fabric as *nodes*.
The information which object occupies which slot is stored in the edge feature [oslots](oslots).

# Letter type

The letters in the dataset are the non-white characters.
The white space characters have been stripped away.
However, the position where they have been is remembered in the feature [trailer](trailer).

# Word type

The original words are still available as a separate type.

##### Hint
> In Text-Fabric we have developed a new way of querying.
Read more in
[searchTutorial](/Dans-labs/text-fabric/blob/master/docs/searchTutorial.ipynb).

