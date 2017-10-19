---
title: Dataset dcs
feat: false
---

# About

Sanskrit corpus obtained from [github](https://github.com/cltk/sanskrit_text_dcs).


## Conversion
The conversion of this dataset to
[Text-Fabric](/Dans-labs/text-fabric/wiki)
has been carried out by Dirk Roorda on a suggestion by
[Tyler Neill](http://www.gko.uni-leipzig.de/indologie-zaw/institut/mitarbeiter-in-forschungsprojekten/tyler-graham-neill.html).
The source has been taken on 2017-07-08
(commit [1e5e094daa69521bf6b9916aa5e390b99727b7d9](https://github.com/cltk/sanskrit_text_dcs/commit/1e5e094daa69521bf6b9916aa5e390b99727b7d9))

The conversion has preserved the word boundaries of the original text.
Yet the slot type is `character`, not word, because the word boundaries are somewhat arbitrary at worst, 
and subjective at best, and in any case, they are subject to study and analysis.

We do not impose any segmentation and the default text rendering is without any spacing.

The result has 1161379 letter nodes (*slots*), and 1336710 nodes in total.

There is no syntax and morphology markup.

# Status

This is work in progress.

# License

We do not license this work. Source materials are licensed as in the source repository where we obtained the materials.

# How to use

This data can be processed by 
[Text-Fabric](https://github.com/Dans-labs/text-fabric/wiki).

See also 
[tutorial (Sanskrit)](https://github.com/Dans-labs/text-fabric/blob/master/docs/tutorialSanskrit.ipynb)
and
[tutorial (search)](https://github.com/Dans-labs/text-fabric/blob/master/docs/searchTutorial.ipynb).
