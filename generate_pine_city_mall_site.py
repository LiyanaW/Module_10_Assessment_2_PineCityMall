import os
import shutil

# -------------------- Configuration --------------------
BASE_DIR = "C:/Users/Liyana/Documents/GitHub/Clients Work/Module-10-Assessment-2"  # Change this to your repo folder
IMAGE_DIR = os.path.join(BASE_DIR, "images")

# Shops and Movies data
shops = [
    {"filename": "shop1.html", "name": "Book Nook", "category": "Books", "logo": "images/book-nook-logo.png", "images": ["images/book1.jpg", "images/book2.jpg"]},
    {"filename": "shop2.html", "name": "FreshMart", "category": "Supermarket", "logo": "images/freshmart-logo.png", "images": ["images/fresh1.jpg", "images/fresh2.jpg"]},
    {"filename": "shop3.html", "name": "Gadget World", "category": "Electronics", "logo": "images/gadget-logo.png", "images": ["images/gadget1.jpg", "images/gadget2.jpg"]},
    {"filename": "shop4.html", "name": "Style Haven", "category": "Clothing", "logo": "images/style-logo.png", "images": ["images/style1.jpg", "images/style2.jpg"]},
    {"filename": "shop5.html", "name": "Tech Hub", "category": "Electronics", "logo": "images/techhub-logo.png", "images": ["images/tech1.jpg", "images/tech2.jpg"]},
    {"filename": "shop6.html", "name": "Food Court", "category": "Restaurants", "logo": "images/foodcourt-logo.png", "images": ["images/food1.jpg", "images/food2.jpg"]},
]

movies = [
    {"filename": "movie1.html", "title": "Galaxy Wars", "poster": "images/galaxy-wars.jpg", "actors": "Chris Nova, Lee Star", "age": "13+", "synopsis": "Across galaxies torn by war, two unlikely heroes must unite to restore peace — but the greatest battle may be within themselves.", "showtimes": "12:00, 15:00, 18:00"},
    {"filename": "movie2.html", "title": "The Escape", "poster": "images/the-escape.jpg", "actors": "Alex Star, Bella Lead", "age": "13+", "synopsis": "When a former agent is trapped in a high-security facility, she must rely on her wits and courage to uncover the truth before time runs out.", "showtimes": "13:00, 16:00, 19:00"},
    {"filename": "movie3.html", "title": "Family Tales", "poster": "images/family-tales.jpg", "actors": "Zara Hope, Liam Fields", "age": "PG", "synopsis": "A heartfelt story of a family who learns that laughter, love, and forgiveness can heal the biggest of rifts — one silly adventure at a time.", "showtimes": "10:00, 13:00, 16:00"},
]

# -------------------- CSS Styling --------------------
css_content = """
body {
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    background: url('images/background.jpg') no-repeat center center fixed;
    background-size: cover;
    color: #333;
}
header, nav, footer {
    background: rgba(0,128,128,0.8);
    color: white;
    padding: 1em;
}
nav a {
    color: white;
    text-decoration: none;
    margin: 0 1em;
    font-weight: bold;
}
nav a:hover {
    text-decoration: underline;
}
.container {
    padding: 2em;
    background: rgba(255,255,255,0.9);
    border-radius: 10px;
    margin: 2em auto;
    max-width: 1200px;
}
h1, h2, h3 {
    color: teal;
}
.shop-card, .movie-card {
    display: flex;
    align-items: center;
    margin-bottom: 1em;
    border: 1px solid #ccc;
    padding: 1em;
    border-radius: 8px;
    background: rgba(255,255,255,0.8);
}
.shop-card img, .movie-card img {
    width: 100px;
    height: 100px;
    object-fit: cover;
    margin-right: 1em;
}
.back-button {
    display: inline-block;
    padding: 0.5em 1em;
    margin-top: 1em;
    background: teal;
    color: white;
    text-decoration: none;
    border-radius: 5px;
}
.contact-form input, .contact-form textarea {
    width: 100%;
    padding: 1em;
    margin-bottom: 1em;
    border-radius: 5px;
    border: 1px solid #ccc;
}
.contact-form button {
    padding: 1em 2em;
    background: teal;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
.contact-form button:hover {
    background: #006666;
}
"""

# -------------------- Helper Functions --------------------
def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def clean_website():
    # Delete all HTML files in BASE_DIR and subfolders (except this script)
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".html") or file.endswith(".css"):
                if file != os.path.basename(__file__):
                    os.remove(os.path.join(root, file))
    # Optional: Clear images folder
    if os.path.exists(IMAGE_DIR):
        shutil.rmtree(IMAGE_DIR)
    os.makedirs(IMAGE_DIR, exist_ok=True)

# -------------------- Generate Website --------------------
def build_website():
    # 1. CSS file
    write_file(os.path.join(BASE_DIR, "styles.css"), css_content)

    # 2. Home Page
    home_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pine City Mall - Home</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>Pine City Mall</h1>
<nav>
<a href="index.html">Home</a>
<a href="shops.html">Shops</a>
<a href="movies.html">Movies</a>
<a href="map.html">Map</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</nav>
</header>
<div class="container">
<h2>Welcome to Pine City Mall!</h2>
<img src="images/cover-placeholder.jpg" alt="Cover Image" style="width:100%; border-radius:10px; margin-bottom:2em;">
<h3>Featured: Food Court</h3>
<p>Visit our Food Court for delicious meals and snacks from a variety of cuisines.</p>
<a href="shop6.html" class="back-button">Explore Food Court</a>
</div>
</body>
</html>
"""
    write_file(os.path.join(BASE_DIR, "index.html"), home_html)

    # 3. Shops List Page
    shop_list_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Shops - Pine City Mall</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>Shops</h1>
<nav>
<a href="index.html">Home</a>
<a href="shops.html">Shops</a>
<a href="movies.html">Movies</a>
<a href="map.html">Map</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</nav>
</header>
<div class="container">
"""
    for shop in shops:
        shop_list_html += f"""
<div class="shop-card">
<img src="{shop['logo']}" alt="{shop['name']}">
<div>
<h3>{shop['name']}</h3>
<p>Category: {shop['category']}</p>
<a href="{shop['filename']}" class="back-button">View Details</a>
</div>
</div>
"""
    shop_list_html += """
</div>
</body>
</html>
"""
    write_file(os.path.join(BASE_DIR, "shops.html"), shop_list_html)

    # 4. Individual Shop Pages
    for shop in shops:
        shop_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{shop['name']} - Pine City Mall</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>{shop['name']}</h1>
<nav>
<a href="index.html">Home</a>
<a href="shops.html">Shops</a>
<a href="movies.html">Movies</a>
<a href="map.html">Map</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</nav>
</header>
<div class="container">
<img src="{shop['logo']}" alt="{shop['name']}" style="width:200px; margin-bottom:1em;">
<p>Category: {shop['category']}</p>
<p>Description: This is a placeholder description for {shop['name']}.</p>
"""
        for img in shop['images']:
            shop_html += f'<img src="{img}" alt="{shop["name"]}" style="width:200px; margin:0.5em;">\n'
        shop_html += f"""
<a href="shops.html" class="back-button">Back to Shops</a>
</div>
</body>
</html>
"""
        write_file(os.path.join(BASE_DIR, shop['filename']), shop_html)

    # 5. Movies List Page
    movie_list_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Movies - Pine City Mall</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>Movies</h1>
<nav>
<a href="index.html">Home</a>
<a href="shops.html">Shops</a>
<a href="movies.html">Movies</a>
<a href="map.html">Map</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</nav>
</header>
<div class="container">
"""
    for movie in movies:
        movie_list_html += f"""
<div class="movie-card">
<img src="{movie['poster']}" alt="{movie['title']}">
<div>
<h3>{movie['title']}</h3>
<p>Actors: {movie['actors']}</p>
<p>Age Restriction: {movie['age']}</p>
<a href="{movie['filename']}" class="back-button">View Details</a>
</div>
</div>
"""
    movie_list_html += """
</div>
</body>
</html>
"""
    write_file(os.path.join(BASE_DIR, "movies.html"), movie_list_html)

    # 6. Individual Movie Pages
    for movie in movies:
        movie_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{movie['title']} - Pine City Mall</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>{movie['title']}</h1>
<nav>
<a href="index.html">Home</a>
<a href="shops.html">Shops</a>
<a href="movies.html">Movies</a>
<a href="map.html">Map</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</nav>
</header>
<div class="container">
<img src="{movie['poster']}" alt="{movie['title']}" style="width:200px; margin-bottom:1em;">
<p>Actors: {movie['actors']}</p>
<p>Age Restriction: {movie['age']}</p>
<p>Showtimes: {movie['showtimes']}</p>
<p>Synopsis: {movie['synopsis']}</p>
<a href="movies.html" class="back-button">Back to Movies</a>
</div>
</body>
</html>
"""
        write_file(os.path.join(BASE_DIR, movie['filename']), movie_html)

    # 7. About Page
    about_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>About - Pine City Mall</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>About Pine City Mall</h1>
<nav>
<a href="index.html">Home</a>
<a href="shops.html">Shops</a>
<a href="movies.html">Movies</a>
<a href="map.html">Map</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</nav>
</header>
<div class="container">
<h2>Our Mission</h2>
<p>To provide a premier shopping experience that combines convenience, variety, and community spirit.</p>
<h2>Our Vision</h2>
<p>To be the go-to destination for shopping, entertainment, and social gatherings in the region.</p>
<img src="images/about-placeholder.jpg" alt="Mall Interior" style="width:100%; border-radius:10px; margin-top:1em;">
</div>
</body>
</html>
"""
    write_file(os.path.join(BASE_DIR, "about.html"), about_html)

    # 8. Map Page
    map_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Map - Pine City Mall</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>Mall Map</h1>
<nav>
<a href="index.html">Home</a>
<a href="shops.html">Shops</a>
<a href="movies.html">Movies</a>
<a href="map.html">Map</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</nav>
</header>
<div class="container">
<h2>Shop Locations</h2>
<img src="images/mall-map-placeholder.jpg" alt="Mall Map" style="width:100%; border-radius:10px;">
<p>Map placeholder showing shop locations within the mall.</p>
</div>
</body>
</html>
"""
    write_file(os.path.join(BASE_DIR, "map.html"), map_html)

    # 9. Contact Page
    contact_html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Contact - Pine City Mall</title>
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header>
<h1>Contact Us</h1>
<nav>
<a href="index.html">Home</a>
<a href="shops.html">Shops</a>
<a href="movies.html">Movies</a>
<a href="map.html">Map</a>
<a href="about.html">About</a>
<a href="contact.html">Contact</a>
</nav>
</header>
<div class="container">
<img src="images/contact-placeholder.jpg" alt="Mall Exterior" style="width:100%; border-radius:10px; margin-bottom:1em;">
<h2>Contact Information</h2>
<p>Address: 123 Pine City Mall Drive, Pine City</p>
<p>Phone: +27 123 456 789</p>
<p>Email: info@pinecitymall.com</p>
<p>Business Hours: Mon-Sun 9:00 - 21:00</p>
<h2>Send us a message</h2>
<form class="contact-form">
<input type="text" placeholder="Your Name" required>
<input type="email" placeholder="Your Email" required>
<textarea placeholder="Your Message" rows="5" required></textarea>
<button type="submit">Send Message</button>
</form>
</div>
</body>
</html>
"""
    write_file(os.path.join(BASE_DIR, "contact.html"), contact_html)

# -------------------- Run Script --------------------
clean_website()
build_website()
print("Website has been cleaned and rebuilt from scratch successfully!")
