import re

def read_bib_entries(file_path):
    """
    Reads a .bib file and extracts individual entries.
    """
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        content = file.read()
    
    # Split into individual entries using regex for `@entrytype{...`
    entries = re.split(r'(?=@[a-zA-Z]+{)', content)
    # Strip whitespace and ignore empty entries
    entries = [entry.strip() for entry in entries if entry.strip()]
    
    # Use a dictionary to store entries by their unique keys
    entry_dict = {}
    for entry in entries:
        match = re.match(r'@[a-zA-Z]+{([^,]+)', entry)
        if match:
            key = match.group(1)
            entry_dict[key] = entry.strip()
    return entry_dict

def cross_check_bib(original_file, sorted_file):
    """
    Cross-checks the entries in the original and sorted .bib files.
    """
    # Read entries from both files
    original_entries = read_bib_entries(original_file)
    sorted_entries = read_bib_entries(sorted_file)
    
    # Check for missing or extra entries
    original_keys = set(original_entries.keys())
    sorted_keys = set(sorted_entries.keys())
    
    missing_in_sorted = original_keys - sorted_keys
    extra_in_sorted = sorted_keys - original_keys
    
    # Check for content mismatches
    mismatched_content = []
    for key in original_keys & sorted_keys:
        if original_entries[key] != sorted_entries[key]:
            mismatched_content.append(key)
    
    # Print results
    if missing_in_sorted:
        print(f"Entries missing in sorted file: {missing_in_sorted}")
    else:
        print("No entries are missing in the sorted file.")
    
    if extra_in_sorted:
        print(f"Extra entries in sorted file: {extra_in_sorted}")
    else:
        print("No extra entries are present in the sorted file.")
    
    if mismatched_content:
        print(f"Entries with mismatched content: {mismatched_content}")
    else:
        print("No content mismatches found between the files.")

# Example usage
original_file = 'references.bib'  # Path to original file
sorted_file = 'sorted_references.bib'  # Path to sorted file
cross_check_bib(original_file, sorted_file)
