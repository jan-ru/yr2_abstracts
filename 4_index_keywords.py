import bibtexparser
from collections import Counter
from thefuzz import process

# including tgdm (ref. bibtex_DBLP)

def match_keywords(existing_keywords, new_keyword, threshold=70):
    matches = process.extract(new_keyword, existing_keywords, limit=1)
    if matches and matches[0][1] >= threshold:
        return matches[0][0]
    return new_keyword

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
#                    keyword = keyword.capitalize()
                    keyword = match_keywords(keywords, keyword)
                    keywords.append(keyword)
    
    return keywords

def generate_keyword_html(keywords, output_html='index_keywords.html'):

    keyword_counts = Counter(keywords)
    sorted_keywords = sorted(keyword_counts.items())    
    max_count = max(keyword_counts.values())
    total_count = sum(keyword_counts.values())

    for keyword, count in sorted_keywords:
        print(f'Keyword: {keyword}, Count: {count}')

    print(f'Max Count: {max_count}')
    print(f'Total Count: {total_count}')

    # Generate HTML content
    html_content = ""

    for keyword, count in sorted_keywords:
        font_size = 10 + (count / max_count) * 40  # Example: base size 10px, max size 50px
        html_content += f'<span class="keyword" style="font-size: {font_size}px;">{keyword}</span>\n'

    html_content += """
    """

    # Write the HTML content to a file
    with open(output_html, 'w') as file:
        file.write(html_content)

# Example usage
bib_file_path = 'bib/MySelection.bib'
keywords = parse_bibtex_keywords(bib_file_path)
generate_keyword_html(keywords)
print("index_keywords.html generated")