import os
import urllib.request

# --- Create folders ---
folders = ["css", "images"]
for f in folders:
    os.makedirs(f, exist_ok=True)

# --- Define images to download (placeholders) ---
images = {
    "mall-front.jpg": "https://placehold.co/800x400?text=Pine+City+Mall",
    "mall-inside1.jpg": "https://placehold.co/600x400?text=Mall+Interior+1",
    "mall-inside2.jpg": "https://placehold.co/600x400?text=Mall+Interior+2",
    "mall-inside3.jpg": "https://placehold.co/600x400?text=Food+Court",
    "mall-map.jpg": "https://placehold.co/600x400?text=Mall+Map",
    "contact-mall.jpg": "https://placehold.co/600x400?text=Contact+Pine+City+Mall",
    # Shop logos
    "style-haven-logo.png": "https://placehold.co/200x200?text=Style+Haven",
    "freshmart-logo.png": "https://placehold.co/200x200?text=FreshMart",
    "tech-hub-logo.png": "https://placehold.co/200x200?text=Tech+Hub",
    "book-nook-logo.png": "https://placehold.co/200x200?text=Book+Nook",
    "gadget-world-logo.png": "https://placehold.co/200x200?text=Gadget+World",
    "food-court-logo.png": "https://placehold.co/200x200?text=Food+Court",
}

# Add gallery images for shops
for i in range(1,7):
    for j in range(1,4):
        images[f"shop{i}-{j}.jpg"] = f"https://placehold.co/200x150?text=Shop{i}+Image{j}"

# Movies: poster + previews
movies_list = ["The Escape","Family Tales","Galaxy Wars"]
for i, movie in enumerate(movies_list,1):
    images[f"movie{i}.jpg"] = f"https://placehold.co/300x450?text={movie.replace(' ', '+')}"
    for j in range(1,3):
        images[f"movie{i}-{j}.jpg"] = f"https://placehold.co/150x100?text={movie.replace(' ', '+')}+Preview{j}"

# Download all images
for name, url in images.items():
    urllib.request.urlretrieve(url, os.path.join("images", name))

# --- CSS styling ---
css = """
body {
  font-family: 'Poppins', sans-serif;
  margin: 0;
  background: #fafafa;
  color: #333;
}
header {
  background: #004d40;
  color: white;
  text-align: center;
  padding: 1rem;
}
nav a {
  color: white;
  margin: 0 10px;
  text-decoration: none;
  font-weight: bold;
}
nav a:hover { text-decoration: underline; }
main {
  padding: 1rem;
}
footer {
  background: #004d40;
  color: white;
  text-align: center;
  padding: 1rem;
  margin-top: 1rem;
}
img {
  width: 100%;
  border-radius: 10px;
  margin: 0.5rem auto;
  display: block;
}
.shop-logo {
  width: 120px;
  margin: 0.5rem auto;
}
.movie-poster {
  width: 200px;
  margin: 0.5rem auto;
}
.shop-item, .movie-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid #ddd;
  padding: 0.5rem;
  margin: 0.5rem 0;
  border-radius: 8px;
  background: #fff;
}
.gallery {
  display: flex;
  gap: 0.5rem;
  margin-top: 0.5rem;
}
.gallery img {
  width: 80px;
  height: 50px;
  border-radius: 5px;
  object-fit: cover;
}
.card {
  border: 1px solid #ddd;
  background: #fff;
  border-radius: 8px;
  margin: 1rem 0;
  padding: 1rem;
}
.card img {
  border-radius: 8px;
}
form {
  display: grid;
  gap: .7rem;
  max-width: 400px;
  margin: 2rem auto;
}
input, textarea, button {
  padding: .6rem;
  font-size: 1rem;
  border-radius: 5px;
  border: 1px solid #ccc;
}
button {
  background: #004d40;
  color: white;
  cursor: pointer;
}
button:hover {
  background: #00695c;
}
@media (min-width: 600px) {
  .shop-item, .movie-item {
    flex-direction: row;
    gap: 1rem;
    align-items: flex-start;
  }
}
"""

with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

# --- Define shop data ---
shops = [
    {"name":"Style Haven","category":"Clothing","logo":"style-haven-logo.png",
     "images":["shop1-1.jpg","shop1-2.jpg","shop1-3.jpg"],
     "desc":"Trendy clothing for men & women."},
    {"name":"FreshMart","category":"Supermarket","logo":"freshmart-logo.png",
     "images":["shop2-1.jpg","shop2-2.jpg","shop2-3.jpg"],
     "desc":"Fresh produce & groceries."},
    {"name":"Tech Hub","category":"Electronics","logo":"tech-hub-logo.png",
     "images":["shop3-1.jpg","shop3-2.jpg","shop3-3.jpg"],
     "desc":"Latest gadgets & accessories."},
    {"name":"Book Nook","category":"Books","logo":"book-nook-logo.png",
     "images":["shop4-1.jpg","shop4-2.jpg","shop4-3.jpg"],
     "desc":"Books, gifts & stationery."},
    {"name":"Gadget World","category":"Electronics","logo":"gadget-world-logo.png",
     "images":["shop5-1.jpg","shop5-2.jpg","shop5-3.jpg"],
     "desc":"Everything tech and gadgets."},
    {"name":"Food Court","category":"Restaurants","logo":"food-court-logo.png",
     "images":["shop6-1.jpg","shop6-2.jpg","shop6-3.jpg"],
     "desc":"Variety of dining options."}
]

# --- Define movie data ---
movies = [
    {"title":"The Escape","actors":"Alex Star, Bella Lead","age":"13+","poster":"movie1.jpg",
     "previews":["movie1-1.jpg","movie1-2.jpg"],"showtimes":"10:00, 13:00, 16:00","synopsis":"An exciting action adventure of a young hero."},
    {"title":"Family Tales","actors":"Zara Hope, Liam Fields","age":"PG","poster":"movie2.jpg",
     "previews":["movie2-1.jpg","movie2-2.jpg"],"showtimes":"11:00, 14:00, 17:00","synopsis":"A heartwarming story of family and friendship."},
    {"title":"Galaxy Wars","actors":"Chris Nova, Lee Star","age":"13+","poster":"movie3.jpg",
     "previews":["movie3-1.jpg","movie3-2.jpg"],"showtimes":"12:00, 15:00, 18:00","synopsis":"An epic space saga of war and heroism."}
]

pages = {}

# --- Home page ---
home_html = f"""<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Pine City Mall | Home</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>
<header><h1>Pine City Mall</h1>
<nav><a href='about.html'>About</a><a href='shops.html'>Shops</a><a href='movies.html'>Movies</a><a href='map.html'>Map</a><a href='contact.html'>Contact</a></nav></header>
<main>
<img src='images/mall-front.jpg' alt='Mall front'>
<h2>Featured Offers</h2>
<div class='card'><h3>Style Haven</h3><p>Up to 50% off summer collection!</p></div>
<div class='card'><h3>FreshMart</h3><p>Buy 2 get 1 free on select produce!</p></div>
<div class='card'><h3>Food Court</h3><p>Special combo meals this week!</p></div>
</main>
<footer><p>&copy; 2025 Pine City Mall</p></footer>
</body></html>"""
pages["index.html"] = home_html

# --- About page ---
about_html = f"""<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>About | Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>
<header><h1>About Pine City Mall</h1>
<nav><a href='index.html'>Home</a><a href='shops.html'>Shops</a><a href='movies.html'>Movies</a><a href='map.html'>Map</a><a href='contact.html'>Contact</a></nav></header>
<main>
<img src='images/mall-front.jpg' alt='Mall front'>
<div class='gallery'>
<img src='images/mall-inside1.jpg' alt='Mall interior 1'>
<img src='images/mall-inside2.jpg' alt='Mall interior 2'>
<img src='images/mall-inside3.jpg' alt='Food court interior'>
</div>
</main>
<footer><p>&copy; 2025 Pine City Mall</p></footer>
</body></html>"""
pages["about.html"] = about_html

# --- Map page ---
map_html = f"""<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Map | Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>
<header><h1>Mall Map</h1>
<nav><a href='index.html'>Home</a><a href='shops.html'>Shops</a><a href='movies.html'>Movies</a><a href='about.html'>About</a><a href='contact.html'>Contact</a></nav></header>
<main>
<img src='images/mall-map.jpg' alt='Mall map'>
</main>
<footer><p>&copy; 2025 Pine City Mall</p></footer>
</body></html>"""
pages["map.html"] = map_html

# --- Shops list page ---
shops_html = "<main><h2>Shops</h2>"
for i, shop in enumerate(shops, start=1):
    previews = "".join([f"<img src='images/{img}' alt='Preview'>" for img in shop["images"][:2]])
    pages["shops.html"] = None  # placeholder (will set after loop)
    shops_html += f"""
<div class='shop-item'>
  <img src='images/{shop['logo']}' alt='{shop['name']} logo' class='shop-logo'>
  <h3>{shop['name']}</h3>
  <p>{shop['category']}</p>
  <div class='gallery'>{previews}</div>
</div>"""
shops_html += "</main>"
shops_page_html = f"""<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Shops | Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>
<header><h1>Shops</h1>
<nav><a href='index.html'>Home</a><a href='movies.html'>Movies</a><a href='map.html'>Map</a><a href='contact.html'>Contact</a></nav></header>
{shops_html}
<footer><p>&copy; 2025 Pine City Mall</p></footer>
</body></html>"""
pages["shops.html"] = shops_page_html

# --- Individual shop pages ---
for i, shop in enumerate(shops, start=1):
    gallery_html = "".join([f"<img src='images/{img}' alt='Gallery'>" for img in shop["images"]])
    page_html = f"""<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>{shop['name']} | Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>
<header><h1>{shop['name']}</h1>
<nav><a href='index.html'>Home</a><a href='shops.html'>Shops</a><a href='movies.html'>Movies</a><a href='map.html'>Map</a><a href='contact.html'>Contact</a></nav></header>
<main>
<img src='images/{shop['logo']}' alt='{shop['name']} logo' class='shop-logo'>
<p>{shop['desc']}</p>
<div class='gallery'>{gallery_html}</div>
</main>
<footer><p>&copy; 2025 Pine City Mall</p></footer>
</body></html>"""
    pages[f"shop{i}.html"] = page_html

# --- Movies list page ---
movies_html = "<main><h2>Movies Currently Showing</h2>"
for i, movie in enumerate(movies, start=1):
    previews = "".join([f"<img src='images/{img}' alt='Preview'>" for img in movie["previews"]])
    movies_html += f"""
<div class='movie-item'>
  <img src='images/{movie['poster']}' alt='{movie['title']} poster' class='movie-poster'>
  <h3>{movie['title']}</h3>
  <p>Actors: {movie['actors']}</p>
  <p>Age: {movie['age']}</p>
  <div class='gallery'>{previews}</div>
</div>"""
movies_html += "</main>"
movies_page_html = f"""<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>Movies | Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>
<header><h1>Movies</h1>
<nav><a href='index.html'>Home</a><a href='shops.html'>Shops</a><a href='map.html'>Map</a><a href='contact.html'>Contact</a></nav></header>
{movies_html}
<footer><p>&copy; 2025 Pine City Mall</p></footer>
</body></html>"""
pages["movies.html"] = movies_page_html

# --- Individual movie pages ---
for i, movie in enumerate(movies, start=1):
    gallery_html = "".join([f"<img src='images/{img}' alt='Preview'>" for img in movie["previews"]])
    page_html = f"""<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>
<title>{movie['title']} | Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>
<header><h1>{movie['title']}</h1>
<nav><a href='index.html'>Home</a><a href='shops.html'>Shops</a><a href='movies.html'>Movies</a><a href='map.html'>Map</a><a href='contact.html'>Contact</a></nav></header>
<main>
<img src='images/{movie['poster']}' alt='{movie['title']} poster' class='movie-poster'>
<p><strong>Actors:</strong> {movie['actors']}</p>
<p><strong>Age Restriction:</strong> {movie['age']}</p>
<p><strong>Showtimes:</strong> {movie['showtimes']}</p>
<p>{movie['synopsis']}</p>
<div class='gallery'>{gallery_html}</div>
</main>
<footer><p>&copy; 2025 Pine City Mall</p></footer>
</body></html>"""
    pages[f"movie{i}.html"] = page_html

# --- Contact page ---
contact_html = """<!DOCTYPE html>
<html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial‑scale=1.0'>
<title>Contact | Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>
<header><h1>Contact Us</h1>
<nav><a href='index.html'>Home</a><a href='shops.html'>Shops</a><a href='movies.html'>Movies</a><a href='map.html'>Map</a><a href='about.html'>About</a></nav></header>
<main>
<img src='images/contact-mall.jpg' alt='Contact Pine City Mall'>
<h2>Visit Pine City Mall</h2>
<p><strong>Address:</strong> 123 Main Street, Pine City</p>
<p><strong>Business Hours:</strong> Mon–Sun, 9am–9pm</p>
<p><strong>Phone:</strong> +27 11 123 4567</p>
<p><strong>Email:</strong> info@pinecitymall.co.za</p>
<h3>Send Us a Message</h3>
<form onsubmit="event.preventDefault(); alert('Thank you! We’ll get back to you soon.');">
<input type='text' placeholder='Your Name' required>
<input type='email' placeholder='Your Email' required>
<textarea placeholder='Your Message' rows='4' required></textarea>
<button type='submit'>Send Message</button>
</form>
</main>
<footer><p>&copy; 2025 Pine City Mall</p></footer>
</body></html>"""
pages["contact.html"] = contact_html

# --- Write all pages ---
for filename, content in pages.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Pine City Mall site created using Mall‑of‑the‑South style layout – open 'index.html' to view.")
