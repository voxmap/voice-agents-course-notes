import yaml

def generate_prompt():
    # Load the glossary YAML file
    with open('glossary/glossary.yaml', 'r') as file:
        glossary = yaml.safe_load(file)

    entries = []
    # Process each top-level category
    for category, items in glossary.items():
        if category == "People":
            # For people, add nicknames if available, otherwise use full name
            entries.extend(sum([[*item_data.get("nicknames", [])] or [item_name] 
                           for item_name, item_data in items.items()], []))
        else:
            # For all other categories, just add item names
            entries.extend(item_name for item_name in items)

    # Join all entries with commas
    prompt = ", ".join(entries)
    return prompt

if __name__ == "__main__":
    prompt = generate_prompt()
    print("Generated Whisper prompt:")
    print(prompt)
