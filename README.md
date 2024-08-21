README

Create Corpus from Bibliography file.

Motivation:

Using an academic database such as WoS or Scopus a student can use the build-in filters and basic analytics. Features provided with WoS for example include a timeline of selected items. Also, one is able to select the type(s) of publication one is interested in. As soon as a student uses multiple databases to source articles of interest such features are no longer available. The functionalities are available on a specific platform, but are not available accross platforms. The student needs to recreate a database with the selected literature and needs to recreate the filters and basic analytics.

A prior attempt involved various lists of articles in excel. The column count kept expanding with each new publication attribute that seemed worthwhile tracking. Versions of the literature list were kept in different tab sheets. The excel file didn't "feel" like a robust solution. I upgraded to using a proper reference manager.

This second attempt takes as a starting point a bibliography file in biblatex format. The script(s) take the bibliography file as input (MySelection.bib). Certain bibliography data (title, abstract, keywords) is extracted and written to a markdown file. The markdown file is rendered to html and pdf.

(insert workflow image)

For now the scripts are for personal use. No effort has been made to create an installer. Nor is there proper documentation. It's CC4 licensed.

[![Common Changelog](https://common-changelog.org/badge.svg)](https://common-changelog.org)

[![pages-build-deployment](https://github.com/jan-ru/yr2_abstracts/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/jan-ru/yr2_abstracts/actions/workflows/pages/pages-build-deployment)
