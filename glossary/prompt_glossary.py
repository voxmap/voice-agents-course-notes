import yaml

def generate_prompt():
    # Load the glossary YAML file
    with open('glossary/glossary.yaml', 'r') as file:
        glossary = yaml.safe_load(file)

    entries = []
    # Process each top-level category
    for category, items in glossary.items():
        for item_name, item_data in items.items():
            # For People, use their nicknames
            if category == "People" and "nicknames" in item_data:
                entries.extend(item_data["nicknames"])
            # For all other categories, use the item name
            else:
                entries.append(item_name)

    # Join all entries with commas
    prompt = ", ".join(entries)
    return prompt

if __name__ == "__main__":
    prompt = generate_prompt()
    print("Generated Whisper prompt:")
    print(prompt)
