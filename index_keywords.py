import bibtexparser
from collections import Counter

def parse_bibtex_keywords(bib_file):
    with open(bib_file, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    
    keywords = []
    for entry in bib_database.entries:
        if 'keywords' in entry:
            entry_keywords = entry['keywords'].split(',')
            for keyword in entry_keywords:
                keyword = keyword.strip()
                if keyword != "/unread":
                    keyword = keyword.capitalize()
                    keywords.append(keyword)
    
    return keywords

def generate_keyword_html(keywords, output_html='index_keywords.html'):

    keyword_counts = Counter(keywords)
    sorted_keywords = sorted(keyword_counts.items())    
    max_count = max(keyword_counts.values())

    # Generate HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Keyword Cloud</title>
        <style>
            .keyword {
                display: inline-block;
                margin: 5px;
            }
        </style>
    </head>
    <body>
    """

    for keyword, count in sorted_keywords:
        font_size = 10 + (count / max_count) * 40  # Example: base size 10px, max size 50px
        html_content += f'<span class="keyword" style="font-size: {font_size}px;">{keyword}</span>\n'

    html_content += """
    </body>
    </html>
    """

    # Write the HTML content to a file
    with open(output_html, 'w') as file:
        file.write(html_content)

# Example usage
bib_file_path = 'bib/MySelection.bib'
keywords = parse_bibtex_keywords(bib_file_path)
generate_keyword_html(keywords)