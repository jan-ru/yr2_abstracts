import re
import argparse
import shutil

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# still to be implemented
hello_parser = subparsers.add_parser('hello')
goodbye_parser = subparsers.add_parser('goodbye')

if __name__ == '__main__':
    args = parser.parse_args()


# Function to highlight a specific word, using regex, case-insensitive
def highlight_word(format, text, word):
    if format == 'html':
        highlighted_word = f'<mark>{word}</mark>'
        highlighted_text = re.sub(f'\\b{re.escape(word)}\\b', highlighted_word, text, flags=re.IGNORECASE)
    elif format == 'pdf':
        highlighted_word = f'\\\\hl{{{word}}}'
        highlighted_text = re.sub(f'\\b{re.escape(word)}\\b', highlighted_word, text, flags=re.IGNORECASE)
    else: 
        return text, 0

    word_count = len(re.findall(f'\\b{re.escape(word)}\\b', text, flags=re.IGNORECASE))
    return highlighted_text, word_count

def read_input_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_output_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return

# Main program
words_to_highlight = ['workflow', 'BPM', 'compliance']

corpus_file = 'corpus.md'
html_file = 'highlighted_abstracts4html.md'
pdf_file = 'highlighted_abstracts4pdf.md'

shutil.copy(corpus_file, html_file)
shutil.copy(corpus_file, pdf_file)

for word in words_to_highlight:
    content = read_input_from_file(html_file)
    highlighted_content, word_count = highlight_word('html', content, word)
    write_output_to_file(html_file, highlighted_content)

    content = read_input_from_file(pdf_file)
    highlighted_content, word_count = highlight_word('pdf', content, word)
    write_output_to_file(pdf_file, highlighted_content)

    print(f'Term {word} highlighted {word_count} times.')

#latex_preamble = r"""---
#header-includes:
#- \usepackage{soul}
#---
#"""
#full_content = latex_preamble + highlighted_content


