---
title: SBLGNT features
feat: false
---

# Introduction
This is the key to the meaning of the features of the
[sblgnt dataset](/text-fabric-data/features/greek/sblgnt/0_home).

By all means consult the
[original documentation](https://github.com/biblicalhumanities/greek-new-testament/blob/master/syntax-trees/sblgnt/doc/SBLGNT%20Treebank%20Documentation.pdf)
by Randall Tan.

We organize the features in several groups, roughly analagous to the
[types of objects](otype)
we have:

* [grid](#grid-features)
* [sectional](#sectional-features)
* [word](#word-features)
* [linguistic](#linguistic-features)
* [generic](#generic-features)

# Grid features

---|---|---
[otype](otype) | node type | `book` `verse` `clause` `phrase` `word`
[oslots](oslots) | slot containment | `1` `1-11` `2010-2015,2020-2030`
[otext](otext) | textapi | *no data, only specifications*  

# Sectional features

---|---|---
[book](book) | name of Bible book | `matthew` `mark` `1john`
[booknum](booknum) | number of book, where `matthew` and `revelation` have | `1` resp `27`
[chapter](chapter) | number of chapter within book | `3`
[verse](verse) | number of verse within chapter | `4`


# Word features

## Orthography

---|---|---|---|---
[Unicode](Unicode) | word | full (with trailer) | greek | `γενέσεως. `
[g_word](g_word) | word | full (without trailer) | greek | `γενέσεως`
[g_plain](g_plain) | word | plain (uppercases without accents) | greek | `ΓΕΝΕΣΕΩΣ`
[trailer](trailer) | word | trailer | greek | `. ` 

## Lexical

---|---|---
[UnicodeLemma](UnicodeLemma) | lexeme full greek | `βίβλος`

[psp](psp) | part of speech | `verb` `noun`
[Type](Type) | subtype within part of speech | `Common` `Proper`

## Morphology

---|---|---
[Gender](Gender) |  gender       | `Masculine` `Feminine` `Neuter`
[Number](Number) |  number       | `Singular` `Plural`
[Person](Person) |  person       | `First` `Second` `Third`
[Case](Case) | case | `Nominative` `Accusative` `Dative` `Genitive`
[Degree](Degree) | degree | `Comparative` `Superlative`
[Voice](Voice) | verbal voice | `Active` `Middle` `Passive`
[Tense](Tense) | verbal tense | `Aorist` `Present` `Imperfect` `Future` `Perfect` `Pluperfect`
[Mood](Mood) | verbal mood | `Indicative` `Participle` `Infinitive` `Subjunctive` `Imperative` `Optative`
[morphId](morphId) | identifier with passage information for words | `40001001001`

## Statistics

---|---
[freq_lex](freq_lex) | frequency of lexeme
[freq_occ](freq_occ) | frequency of word occurrence
[rank_lex](rank_lex) | rank of lexeme
[rank_occ](rank_occ) | rank of word occurrence

# Linguistic features

## Sentence features

Nothing specific, just a generic [Head](Head) feature.

## Clause(-atom) features

---|---|---
[ClType](ClType) | clause type | `VerbElided` `Verbless` `Minor`
[function](function) | clause_atom function | `np` `vp` `V` `ADV` `pp`
[HasDet](function) | modified by determiner | `True`
[Rule](rule) | label of the rule used to derive the non-terminal node (also present on `wordx` nodes | `S-V-O`

## Phrase(-atom) features

---|---|---
[HasDet](function) | modified by determiner | `True`

## Structural features

---|---|---
[child](child) | edge feature from nodes to their children | `13`, `18`, `27`, `38`

# Generic features

---|---|---
[nodeId](nodeId) | identifier with passage information for nodes | `400010010010010`
[Cat](Cat) | original type of node | `verb` `noun` `CL` `ADV`
[Head](Head) | the position of a node among its child nodes| `0` `1` `2`
[Start](Start) | start position of a node in a tree | `1` `81`
[End](End) | end position of a node in a tree | `1` `81`
