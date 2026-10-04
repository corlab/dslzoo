# Versions and citing

## A live zoo

The Robotics DSL Zoo is a **dynamic, live** DSL and model zoo for robotics:
entries are added, the classification evolves and the site is regenerated.
This holds for `corlab/dslzoo` (<https://corlab.github.io/dslzoo/>) as well as
for the fork `norro/dslzoo` (<https://norro.github.io/dslzoo/>). **What the live
site shows is the zoo as it is today, not a fixed state.**

## The citable state

**The citable truth for the SIMPAR 2014 and JOSER 2016 surveys lies on `corlab`**
(<https://github.com/corlab/dslzoo>), **in pinned states that do not change.**

### JOSER 2016

*A Survey on Domain-Specific Modeling and Languages in Robotics*, Journal of
Software Engineering for Robotics 7(1), 75-99, DOI
10.6092/JOSER_2016_07_01_p75.

| What | Where on corlab | Cited in the article |
|---|---|---|
| Bibliography at the time of the survey (132 entries) | tag [`joser16`](https://github.com/corlab/dslzoo/tree/joser16) | |
| Generated site at that time | tag [`joser16-site`](https://github.com/corlab/dslzoo/tree/joser16-site) | |
| Candidate search of the survey | branch [`query`](https://github.com/corlab/dslzoo/tree/query), tip also tag [`legacy-2015-12-22-query`](https://github.com/corlab/dslzoo/tree/legacy-2015-12-22-query) | footnotes 2 and 16 |
| Live site (the URL stays) | <https://corlab.github.io/dslzoo/> | footnote 19 |

### SIMPAR 2014

*A Survey on Domain-Specific Languages in Robotics*, LNCS 8810, 195-206, DOI
10.1007/978-3-319-11900-7_17.

The chapter prints only the former address
<http://cor-lab.org/robotics-dsl-zoo> (footnotes 6 and 8). It no longer serves
the zoo. The zoo has no pinned state from that time: the repository starts on
2014-11-26 and the bibliography was first committed on 2015-01-08, after the
survey. The closest preserved states are the
[Internet Archive capture of the former address](https://web.archive.org/web/20141009225401/http://cor-lab.org/robotics-dsl-zoo)
of 2014-10-09 and, on `corlab`, the first generated site of 2014-12-10
(commit [`6ffcb65`](https://github.com/corlab/dslzoo/commit/6ffcb65)).

### Later states

| What | Where on corlab |
|---|---|
| Last bibliography before the restructuring (2020-05-08, 144 entries) | tag [`legacy-2020-05-08-bib`](https://github.com/corlab/dslzoo/tree/legacy-2020-05-08-bib) |
| Last hand-generated site | tag [`legacy-2020-05-08-site`](https://github.com/corlab/dslzoo/tree/legacy-2020-05-08-site) |

### How to reach a pinned state

Use the links above, download a tag as an archive, for example
<https://github.com/corlab/dslzoo/archive/refs/tags/joser16.zip>, or:

```
git clone https://github.com/corlab/dslzoo
git checkout joser16        # bibliography of the JOSER 2016 survey
git checkout joser16-site   # generated site of that time
```

## Editions

The website was hand-curated from 2014 to 2020. Its modernization started on
2026-09-28; the hand-curated edition is succeeded by a generated edition that
is curated less by hand but stays current.

## What stays stable

- The branch `query` and the tags above are never moved, deleted or
  re-created in `corlab/dslzoo`. A new state gets a new tag.
- The live URL <https://corlab.github.io/dslzoo/> keeps answering with the
  zoo.
- The bibliography `dslzoo.bib` stays at the repository root. Its entries, its
  history and the manual classification of the entries (made by hand,
  following the process documented in the JOSER 2016 survey) are kept.
- Names of individual site pages are not part of this guarantee, because only
  the root is cited. Earlier pages stay available through the tag
  `legacy-2020-05-08-site`.

## Why, and how it is protected

A published citation has to resolve to exactly the cited state years later. A
reference that is moved or deleted silently changes what a citation points
at, and a reader cannot detect it.

- Two repository rulesets in `corlab/dslzoo` block deletion and force-push for
  the branches `query` and `gh-pages`, and deletion, force-push and update for
  the tags `joser16*` and `legacy-*`. They guard against accidents. A
  repository administrator can switch them off, so the guarantee rests on the
  commitment stated on this page as much as on the settings.
- Public archives hold independent copies: a Software Heritage snapshot of the
  repository (2024-06-27), Wayback Machine captures of the site and the
  Internet Archive capture named above.
