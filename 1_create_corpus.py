import os
import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
from IPython.display import display, Markdown


def extract_bibtex_info(bibfile):
    citekey = entry.get('ID')
    author_field = entry.get('author', "No author available")
    main_author = author_field.split(' and ')[0]
    if 'family=' in main_author:
        last_name = main_author.split('family=')[1].split(',')[0]
    else:
        last_name = main_author.split(',')[0] if ', ' in main_author else main_author    
    last_name = last_name.replace(' ','').replace('}', '').replace('{', '')
    year = entry.get('year')  # Try 'year' field first
    if not year:
        date_field = entry.get('date')
        if date_field:
            year = date_field.split('-')[0]  # Extract the year part from the date string
    if not year:
        year = 'Unknown year'
    title = entry.get('title', "No title available")
    abstract = entry.get('abstract', "No abstract available")
    keywords = entry.get('keywords', "No keywords available")
    return last_name, year, title, citekey, abstract, keywords

def exclude_zotero_tags(keywords, keyword_to_exclude="/unread"):
    keyword_list = keywords.split(',')
    filtered_keywords = [keyword.strip() for keyword in keyword_list if keyword.strip() != keyword_to_exclude]
    return ', '.join(filtered_keywords)
    
def insert_space_after_comma(keywords):
    keyword_list = keywords.split(',')
    keywords_with_spaces = ', '.join(keyword_list)
    return keywords_with_spaces

def process_citekey(citekey):
    if '/' in citekey:
        # Extract the part of the string after the last forward slash
        citekey = citekey.split('/')[-1]
        print(f"De citekey: {citekey}")
    return citekey

bibfile = 'bib/MySelection.bib'
directory = './abstracts'
filename = 'temp'
extension =  '.md'

if os.path.exists(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)  # Remove the file
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
else:
    # If the directory does not exist, create it
    os.makedirs(directory)
    print(f'Directory {directory} created.')

# Open the BibTeX file
with open(bibfile, 'r', encoding='utf-8') as bibtex_file:
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    bib_database = bibtexparser.load(bibtex_file, parser=parser)

sequence = 0
t = '**Title**'
a = '**Abstract**'
k = '**Keywords**'
r = ''
for entry in bib_database.entries:
    sequence += 1
    last_name, year, title, citekey, abstract, keywords = extract_bibtex_info(bibfile)
    filtered_keywords = exclude_zotero_tags(keywords)
    formatted_keywords = insert_space_after_comma(filtered_keywords)
    file_name = last_name + year
    file_path = os.path.join(directory, file_name + extension)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"# {file_name}\n\n{t}\n\n{title} (@{citekey})\n\n{a}\n\n{abstract}\n\n{k}\n\n{formatted_keywords}\n\n{r}")
    display(Markdown(f"{title} (@{citekey})\n\n## Abstract\n\n{abstract}\n\n## Keywords\n\n{formatted_keywords}\n\\newpage"))

display(Markdown(f"***Number of selected bibtex entries {sequence}.***"))

output_file = 'corpus.md'
file_path = os.path.join(directory, output_file)
corpus_content = []

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path) and filename.endswith('.md'):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                corpus_content.append(file.read())
        except Exception as e:
            print(f'Failed to read {file_path}. Reason: {e}')

with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n\n'.join(corpus_content))
