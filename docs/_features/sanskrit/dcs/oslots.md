---
title: oslots
---

**slot set**


The set of slots associated with an object.

Every object corresponds to exactly one *slot set*,
i.e. the set of *letter occurrences* that form the textual representation of that object.
Every letter fills a slot, and every slot has a unique sequence number.
Earlier letters have lower numbers than later letters.
An object does not have to be consecutive, it may be interrupted at any place.
Different objects may or may not overlap.

The slot set is given as a comma separated list of slot *ranges*, where a range has the form *n* `-` *m*,
where *n* is a number smaller than or equal to *m*. The range *n* `-` *n* may be abbreviated to *n*.

##### Note
> The value of this feature for letter objects is always just one number: the number of the slot the letter occupies.
All letter occurrences are numbered from 1 to *max*, in the order as they occur in the corpus.

##### Note
> There are no gaps in the slot numbering!
