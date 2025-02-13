import re

def sort_bib_file(input_file, output_file):
    # Read the input .bib file
    with open(input_file, 'r', encoding='ISO-8859-1') as file:
        content = file.read()
    
    # Split into individual entries using regex for `@entrytype{...`
    entries = re.split(r'(?=@[a-zA-Z]+{)', content)

    # Strip whitespace and ignore empty entries
    entries = [entry.strip() for entry in entries if entry.strip()]
    
    # Define a function to extract the sorting key (first author's last name)
    def extract_first_author(entry):
        match = re.match(r'@[a-zA-Z]+{([^,]+)', entry)
        if match:
            key = match.group(1)  # Extract the key (e.g., "Pinkston1967")
            # Extract the first author's last name from the key
            last_name = key.split('--')[0] if '--' in key else key
            return last_name.lower()  # Return case-insensitive last name
        return ''  # Default fallback if no match

    # Sort entries alphabetically by the extracted last name
    sorted_entries = sorted(entries, key=extract_first_author)
    
    # Write sorted entries back to a new .bib file
    with open(output_file, 'w', encoding='ISO-8859-1') as file:
        file.write('\n\n'.join(sorted_entries))  # Separate entries with double newlines

    print(f"Sorted .bib file has been written to {output_file}")

# Example usage
input_file = 'references.bib'  # Input file path
output_file = 'sorted_references.bib'  # Output file path
sort_bib_file(input_file, output_file)
