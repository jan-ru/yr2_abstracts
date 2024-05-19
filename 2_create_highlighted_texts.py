import re
import os

# Function to highlight a specific word, using regex, case-insensitive
def highlight_word(format, text, word):
    if format == 'html':
        highlighted_word = f'<mark>{word}</mark>'
        return re.sub(f'\\b{re.escape(word)}\\b', highlighted_word, text, flags=re.IGNORECASE)
    elif format == 'pdf':
        highlighted_word = f'\\\\hl{{{word}}}'
        return re.sub(f'\\b{re.escape(word)}\\b', highlighted_word, text, flags=re.IGNORECASE)
    else: 
        return

def write_output_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return

word_to_highlight = 'BPM' # change to list of words

input_file = 'corpus.md'
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

output_html = 'abstracts4html.md'
highlighted_content = highlight_word('html', content, word_to_highlight)
write_output_to_file(output_html, highlighted_content)

output_latex = 'abstracts4pdf.md'
highlighted_content = highlight_word('pdf', content, word_to_highlight)
latex_preamble = r"""---
header-includes:
- \usepackage{soul}
---
"""
full_content = latex_preamble + highlighted_content
write_output_to_file(output_latex, full_content)

#os.system(f'pandoc {output_latex} -o output.pdf --pdf-engine=xelatex')