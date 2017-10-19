---
title: Sanskrit features
feat: false
---

# Introduction
This is the key to the meaning of the features of the
[dcs dataset](/text-fabric-data/features/sanskrit/dcs/0_home).

We organize the features in several groups, roughly analagous to the
[types of objects](otype)
we have:

* [grid](#grid-features)
* [sectional](#sectional-features)
* [letter](#letter-features)
* [word](#word-features)
* [statistics](#statistic-features)

# Grid features

---|---|---
[otype](otype) | node type | `book` `verse` `clause` `phrase` `word` `letter`
[oslots](oslots) | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext) | textapi | *no data, only specifications*  

# Sectional features

---|---|---
[book](book) | name of source file| `Abhidharmakośa` `Bhāgavatapurāṇa`
[chapter](chapter) | number of chapter within book | `65`
[verse](verse) | number of verse within chapter | `1`


# Letter features

---|---|---|---
[char](Unicode) | letter | the unicode character at that point | `a`
[trailer](Unicode) | letter | a space if the letter is followed by a space else empty | ` `

# Word features

---|---|---|---
[word](Unicode) | word | the unicode represention of the word| `a`

## Statistic features

---|---
[freq](freq) | frequency of word occurrence
[rank](rank) | rank of word occurrence

