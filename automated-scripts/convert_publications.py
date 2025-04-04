import json
import os
import shutil
from pathlib import Path

def list_contents(directory):
    print(f"\nListing contents of {directory}:")
    try:
        for item in os.listdir(directory):
            print(item)
    except Exception as e:
        print(f"Error listing contents: {e}")

print("Current working directory:", os.getcwd())

# --- Configuration of paths ---
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONTENT_DIR = BASE_DIR / "content/english/publications"

print("Base directory:", BASE_DIR)
print("Data directory:", DATA_DIR)
print("Content directory:", CONTENT_DIR)

PUBLICATIONS_JSON = DATA_DIR / "publications.json"
if not PUBLICATIONS_JSON.exists():
    print("publications.json not found in:", DATA_DIR)
else:
    print("Found publications.json at:", PUBLICATIONS_JSON)

TAILWIND_COLORS = [
    "bg-blue-500",
    "bg-green-500",
    "bg-yellow-500",
    "bg-purple-500",
    "bg-red-500",
    "bg-teal-500",
    "bg-indigo-500",
    "bg-pink-500",
    "bg-orange-500"
]

def load_publications(json_path):
    print(f"Loading JSON file from: {json_path}")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            publications = json.load(f)
        print(f"Loaded {len(publications)} publications.")
        return publications
    except Exception as e:
        print(f"Error loading JSON: {e}")
        raise

def assign_category_colors(publications):
    categories = sorted({pub.get("Category", "Other") for pub in publications})
    print(f"Found categories: {categories}")
    category_color_map = {}
    for i, category in enumerate(categories):
        category_color_map[category] = TAILWIND_COLORS[i % len(TAILWIND_COLORS)]
    print(f"Assigned colors: {category_color_map}")
    return category_color_map

def write_index_md(category_color_map, output_dir):
    index_md_path = output_dir / "_index.md"
    print(f"Writing _index.md to: {index_md_path}")
    
    categories_yaml_lines = []
    for category, color in category_color_map.items():
        categories_yaml_lines.append(f"  {category}:")
        categories_yaml_lines.append(f"    color: \"{color}\"")
    categories_yaml = "\n".join(categories_yaml_lines)
    
    content_text = f"""---
title: "Publications"
categories:
{categories_yaml}
---

# Publications

Welcome to the publications section! Here you will find research papers and works by our authors, categorized by various academic fields. Each category has a unique color associated with it for easy identification.
"""
    try:
        with open(index_md_path, "w", encoding="utf-8") as f:
            f.write(content_text)
        print(f"Successfully created {index_md_path}")
    except Exception as e:
        print(f"Error writing _index.md: {e}")

def sanitize(text):
    if text is None:
        return ""
    return text.replace('"', '\\"')

def write_publication_md(publication, output_dir):
    oid = publication.get("_id", {}).get("$oid")
    if not oid:
        print("Warning: Publication missing valid _id, skipping.")
        return
    print(f"Processing publication with _id: {oid}")
    pub_dir = output_dir / oid
    try:
        pub_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {pub_dir}")
    except Exception as e:
        print(f"Error creating directory {pub_dir}: {e}")
    
    md_path = pub_dir / "index.md"
    title = sanitize(publication.get("Title", ""))
    authors = sanitize(publication.get("Authors", ""))
    category = sanitize(publication.get("Category", ""))
    year = sanitize(publication.get("Year", ""))
    publication_url = sanitize(publication.get("PublicationURL", ""))
    description = sanitize(publication.get("Description", ""))
    
    front_matter = f"""---
title: "{title}"
authors: "{authors}"
category: "{category}"
year: "{year}"
"""
    if publication_url:
        front_matter += f'publication_url: "{publication_url}"\n'
    front_matter += f'description: "{description}"\n'
    front_matter += "---\n"
    
    try:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(front_matter)
        print(f"Created markdown file: {md_path}")
    except Exception as e:
        print(f"Error writing markdown file {md_path}: {e}")

def clear_publications_folder(output_dir):
    print(f"Clearing folder: {output_dir}")
    if output_dir.exists():
        for item in output_dir.iterdir():
            try:
                if item.is_dir():
                    shutil.rmtree(item)
                    print(f"Removed directory: {item}")
                else:
                    item.unlink()
                    print(f"Removed file: {item}")
            except Exception as e:
                print(f"Error removing {item}: {e}")
    else:
        try:
            output_dir.mkdir(parents=True)
            print(f"Created folder: {output_dir}")
        except Exception as e:
            print(f"Error creating folder {output_dir}: {e}")


print("Script started.")
clear_publications_folder(CONTENT_DIR)

publications = load_publications(PUBLICATIONS_JSON)
print("Number of publications loaded:", len(publications))
category_color_map = assign_category_colors(publications)
write_index_md(category_color_map, CONTENT_DIR)

# Process each publication
for pub in publications:
    write_publication_md(pub, CONTENT_DIR)

# Create a test file to verify file creation
test_file = CONTENT_DIR / "test.txt"
try:
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("This is a test file.")
    print(f"Created test file: {test_file}")
except Exception as e:
    print(f"Error creating test file {test_file}: {e}")

print("Script completed.")
list_contents(CONTENT_DIR)
input("\nPress Enter to exit...")