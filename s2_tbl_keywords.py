import bibtexparser
from IPython.display import display, Markdown
from tabulate import tabulate

file_path = './bib/MySelection.bib'


def extract_keys_and_keywords(file_path):
    with open(file_path) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bibtexparser.loads(bibtex_str)
    data = []

    for entry in bib_database.entries:
        citation_key = "@"+entry['ID']
        keywords = entry.get('keywords', 'No keywords')  # Use 'No keywords' if not present
        data.append([citation_key, keywords])
        data.append(["", ""])  # This creates the empty line after each entry

    return data


data = extract_keys_and_keywords(file_path)

# Output the table using tabulate
print(tabulate(data, headers=['Citation Key', 'Keywords'], maxcolwidths=[20, 60]))
#display(Markdown(tabulate(data, headers=['Citation Key', 'Keywords'], maxcolwidths=[20, 60])))