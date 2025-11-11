import os
import re
import shutil
from bs4 import BeautifulSoup

# --- Configuration ---
project_root = "./"  # Root folder of your website
backup_folder = "./backup_html"

# Mapping of shops and movies
shops = {
    "Book Nook": "shops/book-nook.html",
    "FreshMart": "shops/freshmart.html",
    "Gadget World": "shops/gadget-world.html",
    "Style Haven": "shops/style-haven.html",
    "Tech Hub": "shops/tech-hub.html",
    "Food Court": "shops/food-court.html"
}

movies = {
    "Galaxy Wars": "movies/movie1.html",
    "The Escape": "movies/movie-the-escape.html",
    "Family Tales": "movies/movie-family-tales.html"
}

# --- Step 1: Backup all HTML files ---
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

for root, _, files in os.walk(project_root):
    for file in files:
        if file.endswith(".html"):
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, project_root)
            dest_path = os.path.join(backup_folder, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(src_path, dest_path)
print("✅ Backup completed.")

# --- Helper: Extract main content from HTML ---
def extract_main_content(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    body = soup.body
    if body:
        return str(body)
    return str(soup)

# --- Accordion template with single-open behavior ---
def accordion_item(title, content):
    safe_id = title.replace(" ", "-")
    return f'''
    <div class="accordion-item">
        <button class="accordion-button" onclick="toggleAccordion('{safe_id}')">{title}</button>
        <div class="accordion-content" id="{safe_id}">{content}</div>
    </div>
    '''

# --- Step 2: Create consolidated shops.html ---
shops_content = '''
<h1>Shops</h1>
<div class="accordion">
'''

for shop_name, file_path in shops.items():
    detail_content = extract_main_content(file_path)
    shops_content += accordion_item(shop_name, detail_content)

shops_content += '''
</div>
<style>
.accordion-button {
    width: 100%;
    text-align: left;
    padding: 12px;
    font-size: 18px;
    cursor: pointer;
    background: #008080;
    color: white;
    border: none;
    outline: none;
    transition: background 0.3s;
    margin-bottom: 2px;
    border-radius: 6px;
}
.accordion-button:hover { background: #006666; }

.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.5s ease;
    padding: 0 12px;
    border-left: 2px solid #008080;
    border-right: 2px solid #008080;
    border-bottom: 2px solid #008080;
    border-radius: 0 0 6px 6px;
    margin-bottom: 10px;
}
</style>
<script>
function toggleAccordion(id){
    // Close all other sections
    var all = document.getElementsByClassName('accordion-content');
    for(var i=0;i<all.length;i++){
        if(all[i].id !== id){
            all[i].style.maxHeight = null;
        }
    }
    // Toggle current section
    var content = document.getElementById(id);
    if(content.style.maxHeight){
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
    }
}
</script>
'''

with open(os.path.join(project_root, "shops.html"), "w", encoding="utf-8") as f:
    f.write(shops_content)
print("✅ shops.html created with single-open animated accordion.")

# --- Step 3: Create consolidated movies.html ---
movies_content = '''
<h1>Movies</h1>
<div class="accordion">
'''

for movie_name, file_path in movies.items():
    detail_content = extract_main_content(file_path)
    movies_content += accordion_item(movie_name, detail_content)

movies_content += '''
</div>
<style>
.accordion-button {
    width: 100%;
    text-align: left;
    padding: 12px;
    font-size: 18px;
    cursor: pointer;
    background: #008080;
    color: white;
    border: none;
    outline: none;
    transition: background 0.3s;
    margin-bottom: 2px;
    border-radius: 6px;
}
.accordion-button:hover { background: #006666; }

.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.5s ease;
    padding: 0 12px;
    border-left: 2px solid #008080;
    border-right: 2px solid #008080;
    border-bottom: 2px solid #008080;
    border-radius: 0 0 6px 6px;
    margin-bottom: 10px;
}
</style>
<script>
function toggleAccordion(id){
    // Close all other sections
    var all = document.getElementsByClassName('accordion-content');
    for(var i=0;i<all.length;i++){
        if(all[i].id !== id){
            all[i].style.maxHeight = null;
        }
    }
    // Toggle current section
    var content = document.getElementById(id);
    if(content.style.maxHeight){
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
    }
}
</script>
'''

with open(os.path.join(project_root, "movies.html"), "w", encoding="utf-8") as f:
    f.write(movies_content)
print("✅ movies.html created with single-open animated accordion.")

# --- Step 4: Update all links in HTML files ---
html_files = []
for root, _, files in os.walk(project_root):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

shop_pattern = re.compile(r'href=".*?shop.*?\.html"', re.IGNORECASE)
movie_pattern = re.compile(r'href=".*?movie.*?\.html"', re.IGNORECASE)

for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    original_content = content
    content = shop_pattern.sub('href="shops.html"', content)
    content = movie_pattern.sub('href="movies.html"', content)

    if content != original_content:
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"🔗 Updated links in {html_file}")

print("✅ All navigation links updated with single-open animated accordions!")
