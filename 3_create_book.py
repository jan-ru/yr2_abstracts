import os

# build _quarto.yml file for a project of type book
# each file in the abstracts folder is a chapter

chapters_dir = './abstracts'
files = sorted(os.listdir(chapters_dir))

with open('_quarto.yml', 'w') as f:
    f.write("project:\n  type: book\n")
    f.write("  output-dir: docs\n\n")
    f.write("book:\n  downloads: [pdf,docx]\n\n")
    f.write("  chapters:\n    - index.qmd\n")
    for file in files:
        if file.endswith('.md'):
            chapter_name = os.path.splitext(file)[0].replace('_', ' ').title()
            f.write(f"    - abstracts/{chapter_name}.md\n")
    f.write("\nbibliography: bib/MyLibrary.bib\n")

print("_quarto.yml has been generated.")