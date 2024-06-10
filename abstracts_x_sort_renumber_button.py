import json

def read_json(file_path):
    """Read JSON file and return the data."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    """Write data to JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def sort_and_renumber(data):
    """Sort records alphabetically by Concept and renumber IDs."""
    # Sort the data by the "Concept" attribute
    sorted_data = sorted(data, key=lambda x: x['Concept'].lower())

    # Renumber the IDs
    for index, record in enumerate(sorted_data, start=1):
        record['ID'] = index
    
    return sorted_data

def main():
    input_file = 'abstracts_definitions.json'  # Replace with your input file path
    output_file = 'abstracts_definitions_sorted.json'  # Replace with your output file path
    data = read_json(input_file)
    sorted_data = sort_and_renumber(data)cls
    write_json(output_file, sorted_data)
    print(f'Sorted and renumbered data has been written to {output_file}')

if __name__ == '__main__':
    main()
