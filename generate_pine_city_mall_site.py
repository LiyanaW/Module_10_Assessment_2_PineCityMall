import os
import shutil

# -------------------------------
# CONFIGURATION
# -------------------------------

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_DIR = BASE_DIR
SHOPS = [
    {"name": "Book Nook", "category": "Books", "logo": "images/book-nook.png", "description": "A cozy place for book lovers.", "images": ["images/book1.jpg", "images/book2.jpg"]},
    {"name": "FreshMart", "category": "Supermarket", "logo": "images/freshmart.png", "description": "Fresh groceries and daily essentials.", "images": ["images/fresh1.jpg", "images/fresh2.jpg"]},
    {"name": "Gadget World", "category": "Electronics", "logo": "images/gadget-world.png", "description": "All the latest gadgets under one roof.", "images": ["images/gadget1.jpg", "images/gadget2.jpg"]},
    {"name": "Style Haven", "category": "Clothing", "logo": "images/style-haven.png", "description": "Trendy fashion for every style.", "images": ["images/style1.jpg", "images/style2.jpg"]},
    {"name": "Tech Hub", "category": "Electronics", "logo": "images/tech-hub.png", "description": "Technology solutions and devices.", "images": ["images/tech1.jpg", "images/tech2.jpg"]},
    {"name": "Food Court", "category": "Restaurants", "logo": "images/food-court.png", "description": "A variety of cuisines all in one place.", "images": ["images/food1.jpg", "images/food2.jpg"]},
]

MOVIES = [
    {"title": "Galaxy Wars", "genre": "Sci-Fi / Adventure", "actors": "Chris Nova, Lee Star", "age": "13+", "synopsis": "Across galaxies torn by war, two unlikely heroes must unite to restore peace.", "poster": "images/galaxy-wars.jpg"},
    {"title": "The Escape", "genre": "Action / Thriller", "actors": "Alex Star, Bella Lead", "age": "13+", "synopsis": "A former agent trapped in a high-security facility must uncover the truth before time runs out.", "poster": "images/the-escape.jpg"},
    {"title": "Family Tales", "genre": "Family / Comedy", "actors": "Zara Hope, Liam Fields", "age": "PG", "synopsis": "A family learns that laughter, love, and forgiveness can heal even the biggest rifts.", "poster": "images/family-tales.jpg"},
]

CSS_CONTENT = """
body {
    font-family: 'Poppins', sans-serif;
    margin:0;
    padding:0;
    background-color:#f5f5f5;
    color:#333;
}
header, footer { background-color:#008080; color:white; padding:10px 20px; }
nav a { color:white; text-decoration:none; margin:0 10px; }
nav a:hover { text-decoration:underline; }
.container { max-width:1200px; margin:20px auto; padding:20px; background:white; border-radius:10px; box-shadow:0 0 10px rgba(0,0,0,0.1);}
.shop, .movie { display:flex; align-items:center; margin-bottom:20px; }
.shop img, .movie img { width:120px; height:120px; object-fit:cover; margin-right:20px; border-radius:10px; }
h1,h2,h3 { color:#008080; }
"""

# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def delete_old_html():
    print("Deleting old HTML files...")
    for filename in os.listdir(HTML_DIR):
        if filename.endswith(".html"):
            os.remove(os.path.join(HTML_DIR, filename))
    print("Old HTML files deleted.")

def write_file(filename, content):
    with open(os.path.join(HTML_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {filename}")

def generate_css():
    write_file("styles.css", CSS_CONTENT)

def generate_home():
    shop_links = "".join([f'<li><a href="shop-{i+1}.html">{shop["name"]}</a></li>' for i, shop in enumerate(SHOPS)])
    featured_food = [shop for shop in SHOPS if shop["name"] == "Food Court"][0]
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Pine City Mall</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
    <h1>Pine City Mall</h1>
    <nav><a href="index.html">Home</a> | <a href="shops.html">Shops</a> | <a href="movies.html">Movies</a> | <a href="about.html">About</a> | <a href="contact.html">Contact</a></nav>
</header>
<div class="container">
    <h2>Featured: Food Court</h2>
    <div class="shop">
        <img src="{featured_food['logo']}" alt="{featured_food['name']}">
        <div><h3>{featured_food['name']}</h3><p>{featured_food['description']}</p></div>
    </div>
    <h2>Shop List</h2>
    <ul>{shop_links}</ul>
</div>
<footer>
    <p>&copy; Pine City Mall</p>
</footer>
</body>
</html>
"""
    write_file("index.html", html)

def generate_shops_page():
    shop_list_html = ""
    for i, shop in enumerate(SHOPS):
        shop_list_html += f"""
<div class="shop">
    <img src="{shop['logo']}" alt="{shop['name']}">
    <div>
        <h3><a href="shop-{i+1}.html">{shop['name']}</a></h3>
        <p>{shop['description']}</p>
    </div>
</div>
"""
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Shops - Pine City Mall</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
    <h1>Pine City Mall - Shops</h1>
    <nav><a href="index.html">Home</a> | <a href="shops.html">Shops</a> | <a href="movies.html">Movies</a> | <a href="about.html">About</a> | <a href="contact.html">Contact</a></nav>
</header>
<div class="container">
    {shop_list_html}
</div>
<footer>
    <p>&copy; Pine City Mall</p>
</footer>
</body>
</html>
"""
    write_file("shops.html", html)

def generate_shop_detail_pages():
    for i, shop in enumerate(SHOPS):
        images_html = "".join([f'<img src="{img}" style="width:200px;margin-right:10px;">' for img in shop["images"]])
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{shop['name']} - Pine City Mall</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
    <h1>{shop['name']}</h1>
    <nav><a href="index.html">Home</a> | <a href="shops.html">Shops</a> | <a href="movies.html">Movies</a> | <a href="about.html">About</a> | <a href="contact.html">Contact</a></nav>
</header>
<div class="container">
    <img src="{shop['logo']}" style="width:200px;">
    <p>{shop['description']}</p>
    <div>{images_html}</div>
</div>
<footer>
    <p>&copy; Pine City Mall</p>
</footer>
</body>
</html>
"""
        write_file(f"shop-{i+1}.html", html)

def generate_movies_page():
    movies_html = ""
    for i, movie in enumerate(MOVIES):
        movies_html += f"""
<div class="movie">
    <img src="{movie['poster']}" alt="{movie['title']}">
    <div>
        <h3><a href="movie-{i+1}.html">{movie['title']}</a></h3>
        <p>Genre: {movie['genre']}</p>
        <p>Actors: {movie['actors']}</p>
        <p>Age: {movie['age']}</p>
    </div>
</div>
"""
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Movies - Pine City Mall</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
    <h1>Pine City Mall - Movies</h1>
    <nav><a href="index.html">Home</a> | <a href="shops.html">Shops</a> | <a href="movies.html">Movies</a> | <a href="about.html">About</a> | <a href="contact.html">Contact</a></nav>
</header>
<div class="container">
    {movies_html}
</div>
<footer>
    <p>&copy; Pine City Mall</p>
</footer>
</body>
</html>
"""
    write_file("movies.html", html)

def generate_movie_detail_pages():
    for i, movie in enumerate(MOVIES):
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{movie['title']} - Pine City Mall</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
    <h1>{movie['title']}</h1>
    <nav><a href="index.html">Home</a> | <a href="shops.html">Shops</a> | <a href="movies.html">Movies</a> | <a href="about.html">About</a> | <a href="contact.html">Contact</a></nav>
</header>
<div class="container">
    <img src="{movie['poster']}" style="width:200px;">
    <p><strong>Genre:</strong> {movie['genre']}</p>
    <p><strong>Actors:</strong> {movie['actors']}</p>
    <p><strong>Age Restriction:</strong> {movie['age']}</p>
    <p><strong>Synopsis:</strong> {movie['synopsis']}</p>
</div>
<footer>
    <p>&copy; Pine City Mall</p>
</footer>
</body>
</html>
"""
        write_file(f"movie-{i+1}.html", html)

def generate_static_pages():
    # About page
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>About - Pine City Mall</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>About Pine City Mall</h1>
<nav><a href="index.html">Home</a> | <a href="shops.html">Shops</a> | <a href="movies.html">Movies</a> | <a href="about.html">About</a> | <a href="contact.html">Contact</a></nav>
</header>
<div class="container">
    <p>Images and info about Pine City Mall go here.</p>
</div>
<footer>
<p>&copy; Pine City Mall</p>
</footer>
</body>
</html>
"""
    write_file("about.html", html)

    # Contact page
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Contact - Pine City Mall</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>Contact Pine City Mall</h1>
<nav><a href="index.html">Home</a> | <a href="shops.html">Shops</a> | <a href="movies.html">Movies</a> | <a href="about.html">About</a> | <a href="contact.html">Contact</a></nav>
</header>
<div class="container">
    <p>Address: 123 Pine St, City</p>
    <p>Phone: +27 123 456 7890</p>
    <p>Business Hours: 9am - 9pm</p>
    <form>
        <label>Name:</label><br><input type="text"><br>
        <label>Email:</label><br><input type="email"><br>
        <label>Message:</label><br><textarea></textarea><br>
        <button type="submit">Send</button>
    </form>
</div>
<footer>
<p>&copy; Pine City Mall</p>
</footer>
</body>
</html>
"""
    write_file("contact.html", html)

    # Map page
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Map - Pine City Mall</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>Pine City Mall Map</h1>
<nav><a href="index.html">Home</a> | <a href="shops.html">Shops</a> | <a href="movies.html">Movies</a> | <a href="about.html">About</a> | <a href="contact.html">Contact</a></nav>
</header>
<div class="container">
    <p>Map of the mall goes here.</p>
</div>
<footer>
<p>&copy; Pine City Mall</p>
</footer>
</body>
</html>
"""
    write_file("map.html", html)

# -------------------------------
# MAIN SCRIPT
# -------------------------------

if __name__ == "__main__":
    delete_old_html()
    generate_css()
    generate_home()
    generate_shops_page()
    generate_shop_detail_pages()
    generate_movies_page()
    generate_movie_detail_pages()
    generate_static_pages()
    print("Website generation complete!")
