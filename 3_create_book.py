import os

# build _quarto.yml file for a project of type book
# each file in the abstracts folder is a chapter

chapters_dir = './abstracts'
files = sorted(os.listdir(chapters_dir))

with open('_quarto.yml', 'w') as f:
    f.write("project:\n")
    f.write("  type: book\n")
    f.write("  output-dir: docs\n\n")
    f.write("format:\n")
    f.write("  pdf:\n")
    f.write("    papersize: a4\n")
    f.write("    documentclass: scrreprt\n")
    f.write("    toc: true\n")
    f.write("    lof: true\n")
    f.write("  html: default\n\n")
    f.write("book:\n  downloads: [pdf]\n")
    f.write("  pdf-url: https://jan-ru.github.io/yr2_abstracts/abstracts/yr2_abstracts.pdf\n")
    f.write("  date: last-modified\n")
    f.write("  date-format: \"DD/MM/YYYY\"\n\n")
    f.write("  chapters:\n    - index.qmd\n")
    for file in files:
        if file.endswith('.md'):
            chapter_name = os.path.splitext(file)[0].title()
            f.write(f"    - text: {chapter_name}\n")
            f.write(f"      file: abstracts/{chapter_name}.md\n")
    f.write("\nbibliography: bib/MyLibrary.bib\n")
    f.write("reference-location: section\n")
    f.write("link-citations: true\n")
    f.write("execute:\n")
    f.write("  echo: false\n")
    f.write("website:\n")
    f.write("  title: Abstracts\n")
    f.write("  page-footer: Copyright 2024\n")

print("_quarto.yml has been generated.")