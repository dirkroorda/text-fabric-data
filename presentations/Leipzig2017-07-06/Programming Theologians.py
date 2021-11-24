# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] slideshow={"slide_type": "slide"}
#
# <img align="right" src="tf-small.png"/>
# # Programming theologians
#
# [Text-Fabric](https://github.com/ETCBC/text-fabric): Ancient texts as fabrics of source and annotations.
#
# [data model](https://github.com/ETCBC/text-fabric/wiki/Data-model): Text objects, relationships, features.
#
# Got it? Get it! 
#
# [home page](https://github.com/ETCBC/text-fabric/wiki)
#
# $$ x \over 1 + 2 $$

# + [markdown] slideshow={"slide_type": "subslide"}
# Join the computing gang
#
# 1. go to [https://shebanq.jove.surfsara.nl](https://shebanq.jove.surfsara.nl) and log in (see paper ticket)
# 1. select assignment `prog_theo`, fetch `leipzig` and click it
# 1. click `Programming theologians.ipynb` and off-you-go
#
# ![shot](jove.png)

# + [markdown] slideshow={"slide_type": "slide"}
# # Before the beginning

# + [markdown] slideshow={"slide_type": "subslide"}
# <img src="https://upload.wikimedia.org/wikipedia/en/6/62/Literate_Programming_book_cover.jpg" align="right"/>
#
# ## 1984 Donald Knuth's utopia
#
# This paradigm moves away from 
#
# writing programs in the manner and order imposed by the computer, 
#
# and instead 
#
# develops programs in the order demanded by the logic and flow of their thoughts

# + slideshow={"slide_type": "subslide"}
import collections

from IPython.display import display

import matplotlib.pyplot as plt
# %matplotlib inline

import pandas
pandas.set_option('display.notebook_repr_html', True)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## API to the Hebrew Text

# + slideshow={"slide_type": "fragment"}
from tf.fabric import Fabric

ETCBC = 'hebrew/etcbc4c'
PHONO = 'hebrew/phono'

TF_H = Fabric( modules=[ETCBC, PHONO], silent=False )

# + slideshow={"slide_type": "subslide"}
apiH = TF_H.load('sp')

# + [markdown] slideshow={"slide_type": "subslide"}
# ## API to the Greek Text

# + slideshow={"slide_type": "fragment"}
TF_G = Fabric(modules='greek/sblgnt')

# + slideshow={"slide_type": "subslide"}
apiG = TF_G.load('psp')


# + [markdown] slideshow={"slide_type": "subslide"}
# ## Easy switching

# + slideshow={"slide_type": "fragment"}
def doGreek():
    global T
    global L
    global F
    global Fs
    T = apiG.T
    L = apiG.L
    F = apiG.F
    Fs = apiG.Fs

def doHebrew():
    global T
    global L
    global F
    global Fs
    T = apiH.T
    L = apiH.L
    F = apiH.F
    Fs = apiH.Fs
 
def doingHebrew(): return F is apiH.F

def doingGreek(): return F is apiG.F


# + [markdown] slideshow={"slide_type": "slide"}
# # In the beginning
#
# The first verse

# + [markdown] slideshow={"slide_type": "subslide"}
# ## In Hebrew

# + slideshow={"slide_type": "fragment"}
doHebrew()

# + slideshow={"slide_type": "fragment"}
T.text(range(1,12))

# + slideshow={"slide_type": "fragment"}
T.text(range(1,12), fmt='text-phono-full')

# + slideshow={"slide_type": "subslide"}
T.formats

# + slideshow={"slide_type": "subslide"}
T.text(range(1,12), fmt='lex-orig-plain')

# + [markdown] slideshow={"slide_type": "subslide"}
# ## In Greek

# + slideshow={"slide_type": "fragment"}
doGreek()

# + slideshow={"slide_type": "fragment"}
firstVerse = T.nodeFromSection(('Matthew', 1, 1))
F.otype.v(firstVerse)

# + slideshow={"slide_type": "fragment"}
words = L.d(firstVerse, otype='word')
words

# + slideshow={"slide_type": "fragment"}
T.text(words)

# + slideshow={"slide_type": "subslide"}
T.formats

# + slideshow={"slide_type": "fragment"}
T.text(words, fmt='text-orig-plain')

# + slideshow={"slide_type": "fragment"}
T.text(words, fmt='lex-orig-full')

# + [markdown] slideshow={"slide_type": "slide"}
# # Man and woman
# God created the genders, we count them.

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Which genders have we?

# + slideshow={"slide_type": "fragment"}
doHebrew()

TF_H.load('gn', add=True)

# + slideshow={"slide_type": "subslide"}
{F.gn.v(w) for w in F.otype.s('word')}

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Genders in Hebrew and Greek

# + slideshow={"slide_type": "subslide"}
doGreek()
TF_G.load('Gender', add=True)


# + slideshow={"slide_type": "fragment"}
def getGenders():
    featureName = 'gn' if doingHebrew() else 'Gender'
    return {Fs(featureName).v(w) for w in F.otype.s('word')}


# + slideshow={"slide_type": "fragment"}
doGreek()
print('Greek: {}'.format(getGenders()))
doHebrew()
print('Hebrew: {}'.format(getGenders()))


# + [markdown] slideshow={"slide_type": "subslide"}
# ### Counting genders

# + slideshow={"slide_type": "fragment"}
def countGenders():
    featureName = 'gn' if doingHebrew() else 'Gender'
    stats = collections.Counter()
    for w in F.otype.s('word'):
        stats[Fs(featureName).v(w)] += 1
    print(stats)
countGenders()


# + [markdown] slideshow={"slide_type": "subslide"}
# ## ... in graphic detail ...

# + slideshow={"slide_type": "subslide"}
def genderBias(book):
    bookNode = T.nodeFromSection((book,))
    chapterNodes = L.d(bookNode, otype='chapter')
    x = [T.sectionFromNode(c)[1] for c in chapterNodes]
    masc = dict((c, 0) for c in x)
    fem = dict((c, 0) for c in x)
    neut = dict((c, 0) for c in x)
    absent = dict((c, 0) for c in x)
    total = dict((c, 0) for c in x)

    genderFeature = 'gn' if doingHebrew() else 'Gender'

    for chapterNode in chapterNodes:
        chapter = T.sectionFromNode(chapterNode)[1]
        words = L.d(chapterNode, otype='word')
        for w in words:
            total[chapter] += 1
            gender = Fs(genderFeature).v(w)
            if gender in {'m', 'Masculine'}: masc[chapter] += 1
            if gender in {'f', 'Feminine'}: fem[chapter] += 1
            if gender in {'Neuter'}: neut[chapter] += 1
            if gender in {'NA', 'unknown', None}: absent[chapter] += 1
    m = [100 * masc[c] / total[c] for c in x]
    f = [100 * fem[c] / total[c] for c in x]
    n = [100 * neut[c] / total[c] for c in x]
    a = [100 * absent[c] / total[c] for c in x]

    fig = plt.figure()
    plt.plot(x, m, 'b-', x, f, 'r-', x, n, 'g-', x, a, '0.5')
    plt.axis([x[0], x[-1], 0, 70])
    plt.xticks(x, x, rotation='vertical')
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.15);
    plt.title('gender in {} {}-{}'.format(book, x[0], x[-1]))


# + slideshow={"slide_type": "subslide"}
print(', '.join(T.sectionFromNode(b)[0] for b in F.otype.s('book')))

# + slideshow={"slide_type": "fragment"}
genderBias('Leviticus')

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Inspect some peaks and dips

# + slideshow={"slide_type": "fragment"}
TF_H.load('gloss', add=True)


# + slideshow={"slide_type": "fragment"}
def atAGlance(book, chapter):
    words = L.d(T.nodeFromSection((book, chapter)), otype='word')
    freqs = collections.Counter()
    for w in words:
        if doingHebrew():
            lexeme = L.u(w, otype='lex')[0]
            freqs[F.gloss.v(lexeme)] += 1
        else:
            freqs[F.UnicodeLemma.v(w)] += 1
    for (gloss, freq) in sorted(freqs.items(), key=lambda x: (-x[1], x[0])):
        print('{:>3} {}'.format(freq, gloss))


# + slideshow={"slide_type": "subslide"}
def inDepth(book, chapter):
    chapterNode = T.nodeFromSection((book, chapter))
    verseNodes = L.d(chapterNode, otype='verse')
    for verseNode in verseNodes:
        words = L.d(verseNode, otype='word')
        print('{}: {}'.format(T.sectionFromNode(verseNode)[2], T.text(words)))  


# + slideshow={"slide_type": "subslide"}
genderBias('Leviticus')

# + slideshow={"slide_type": "subslide"}
atAGlance('Leviticus', 18)

# + slideshow={"slide_type": "subslide"}
genderBias('Leviticus')

# + slideshow={"slide_type": "subslide"}
atAGlance('Leviticus', 26)

# + slideshow={"slide_type": "subslide"}
inDepth('Leviticus', 26)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Man, woman and thing

# + slideshow={"slide_type": "fragment"}
doGreek()

TF_G.load('UnicodeLemma', add=True)

# + [markdown] slideshow={"slide_type": "fragment"}
# ### The Greek genders

# + slideshow={"slide_type": "fragment"}
getGenders()

# + slideshow={"slide_type": "subslide"}
genderBias('Matthew')

# + slideshow={"slide_type": "subslide"}
atAGlance('Matthew', 24)

# + slideshow={"slide_type": "subslide"}
inDepth('Matthew', 24)

# + slideshow={"slide_type": "subslide"}
genderBias('John')

# + slideshow={"slide_type": "subslide"}
atAGlance('John', 16)

# + [markdown] slideshow={"slide_type": "slide"}
# # Six days of work (creating data)
#
# Semantic plurals in the letter of Jude.
#
# Let's get all nominal phrases.

# + slideshow={"slide_type": "subslide"}
doGreek()
TF_G.load('Cat', add=True)

# + slideshow={"slide_type": "fragment"}
bookNode = T.nodeFromSection(('Jude',))
phraseNodes = L.d(bookNode, otype='phrase')
NPs = [p for p in phraseNodes if F.Cat.v(p) == 'np']

print('{} NPs in Jude'.format(len(NPs)))

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Generate a data entry form
#
# Export this data as CSV 
# so that experts can fill in a new feature: *semantically plural*.

# + slideshow={"slide_type": "subslide"}
enrichFile = 'np.csv'
enrichedFile = 'np-enriched.csv'

with open(enrichFile, 'w') as f:
    fieldNames = ['passage', 'node', 'phrase', 'semantic plural', 'sentence']
    f.write('{}\n'.format('\t'.join(fieldNames)))
    for np in NPs:
        sn = L.u(np, otype='sentence')[0]
        sentence = L.d(sn, otype='word')
        phrase = L.d(np, otype='word')
        fields = [
            '{} {}:{}'.format(*T.sectionFromNode(np)),
            str(np),
            T.text(phrase),
            '',
            T.text(sentence),
        ]
        f.write('{}\n'.format('\t'.join(fields)))

# + slideshow={"slide_type": "subslide"}
dataFrame = pandas.read_csv(enrichFile, sep='\t')
dataFrame.head(100)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Read the data enrichments

# + slideshow={"slide_type": "fragment"}
semNumber = dict()

with open(enrichedFile) as f:
    for (i, line) in enumerate(f):
        if i == 0: continue                    # header row

        fields = line.rstrip('\n').split(';')
        value = fields[3]
        if value == '': continue               # no data entered

        node = int(fields[1])
        semNumber[node] = value

# + slideshow={"slide_type": "subslide"}
for p in sorted(semNumber):
    print('{} => {}'.format(p, semNumber[p]))

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Save the new feature as a text-fabric file

# + slideshow={"slide_type": "fragment"}
metaData = dict(
    semNumber=dict(
        valueType='str',
        source='Semantic plurality training set',
        author='J.S. Bach, Leipzig',
    ),
)
TF_G = Fabric(locations='.', modules='semantic')

# + slideshow={"slide_type": "subslide"}
TF_G.save(
    nodeFeatures=dict(semNumber=semNumber),
    metaData=metaData,
)

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Check

# + slideshow={"slide_type": "fragment"}
# !cat semantic/semNumber.tf

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Use the new feature

# + slideshow={"slide_type": "fragment"}
LOCATIONS = [
    '~/Downloads/text-fabric-data',
    '~/text-fabric-data',
    '~/github/text-fabric-data',
    '/mnt/shared/text-fabric-data',
]

TF_G = Fabric(
    locations=LOCATIONS+['.'], 
    modules=['greek/sblgnt', 'semantic'],
)

# + slideshow={"slide_type": "subslide"}
apiG = TF_G.load('Number semNumber')
doGreek()

# + [markdown] slideshow={"slide_type": "subslide"}
# ### Observe it in action

# + slideshow={"slide_type": "fragment"}
for np in NPs:
    semNumber = F.semNumber.v(np)
    if not semNumber: continue
    words = L.d(np, otype='word')
    print('NP {}: semantically "{}", words marked as {}'.format(
        np,
        semNumber,
        ' '.join(F.Number.v(w) for w in words if F.Number.v(w)),
    ))

# + [markdown] slideshow={"slide_type": "slide"}
# # Sabbath
# Have a look at the (un)finished work and see whether it is good.

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Janet Dyk
#
# Verbal valence flowchart.
#
# ![val](valency.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Martijn Naaijer
#
# Won a grassroots price for setting up a theology course based on SHEBANQ, Jupyter, and R.
# See [Python course here](https://shebanq.jove.surfsara.nl/user/dirkr/notebooks/shared/martijn/Python_Course/Introduction_to_text_fabric.ipynb).
#
# ![poster](PosterGrassroots_Naaijer.jpg)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Christiaan Erwich
#
# Tries to track who is who in the Psalms, and is deeply into graph visualization.
# ![doxo](doxology.pdf)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Cody Kingham
#
# Helped to convert the SBL Greek New Testament to the Text-Fabric format.
# Tries to
# [explain to the world](http://www.codykingham.com/etcbc/datacreation)
# how the ETCBC encoded the Hebrew Bible during a 40 year long struggle with computers.
#
# ![schema](ps4.p_description.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Dirk Roorda
#
# Tries to recombine everything.
#
# [Phonetic transcription of Hebrew](https://rawgit.com/ETCBC/text-fabric/master/phono/phonoTf.html)
#
# ![phono](phono_tests.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# [Parallel passages](https://shebanq.ancient-data.org/shebanq/static/docs/tools/parallel/parallels.html)
#
# See it in action on SHEBANQ:
# [etcbc4b Genesis 10:1](https://shebanq.ancient-data.org/hebrew/text?qactive=hlcustom&qsel_one=grey&qpub=x&qget=x&wactive=hlcustom&wsel_one=gray&wpub=x&wget=x&nactive=hlcustom&nsel_one=black&npub=x&nget=v&chapter=10&lang=en&book=Genesis&qw=q&tr=hb&tp=txt_tb1&iid=Mnxjcm9zc3JlZg__&verse=1&version=4b&mr=m&page=1&wd4_statfl=v&ph_arela=v&wd4_statrl=v&sn_an=v&cl=v&wd1_lang=x&wd1_subpos=x&wd2_person=v&sp_rela=v&wd1_pdp=x&sn_n=v&wd3_uvf=x&ph_fun=v&wd1_nmtp=v&gl=v&sp_n=v&pt=v&ph_an=v&ph_typ=x&cl_typ=v&tt=v&wd4_statro=x&wd3_vbs=x&wd1=v&tl=x&wd3=x&wd4=v&wd2_gender=v&ph=v&wd3_vbe=v&wd1_pos=v&ph_det=v&ph_rela=x&wd4_statfo=x&tl_tlv=x&wd2_stem=v&wd2_state=v&ht=v&ph_n=v&tl_tlc=x&cl_tab=v&wd3_nme=x&hl=v&cl_par=v&cl_an=v&cl_n=v&wd3_prs=v&wd3_pfm=x&sp=v&cl_code=v&ht_hk=v&wd2=v&hl_hlc=x&cl_rela=v&wd2_gnumber=v&wd2_tense=v&cl_txt=v&wd1_n=x&sn=v&ht_ht=v&hl_hlv=v&pref=alt)
#
# ![parallel](parallel.png)

# + [markdown] slideshow={"slide_type": "subslide"}
# ## Stand-off markup for changing sources
#
# (it is not a nightmare)
#
# [Versioning](https://github.com/ETCBC/text-fabric/blob/master/Versions/etcbc-versions.ipynb)

# + [markdown] slideshow={"slide_type": "slide"}
# <img align="right" src="tf-small.png"/>
# <p style="float: right;">google <a href="https://github.com/ETCBC/text-fabric/wiki">github text-fabric wiki</a></p>
#
#
# # Thanks
#
# ###  [dirk.roorda@dans.knaw.nl](mailto:dirk.roorda@dans.knaw.nl)
#
# [Linguistic Annotation and Philology Workshop](http://www.dh.uni-leipzig.de/wo/laphw/)
# Leipzig, July 6-7, 2017
#
# [<img align="right" src="DANS-logo.png" width="400"/>](https://dans.knaw.nl/en/front-page?set_language=en)
