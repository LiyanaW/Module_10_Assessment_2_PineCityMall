import os
import urllib.request

# ====== SETUP FOLDERS ======
folders = ["css", "images", "shops", "movies"]
for f in folders:
    os.makedirs(f, exist_ok=True)

# ====== IMAGE HELPER ======
def download_image(filename, text, width=800, height=600):
    safe_text = text.replace(" ", "+")
    url = f"https://placehold.co/{width}x{height}?text={safe_text}"
    urllib.request.urlretrieve(url, os.path.join("images", filename))

# ====== MAIN IMAGES ======
download_image("hero-mall.jpg", "Pine City Mall Exterior", 1200, 600)
download_image("interior1.jpg", "Mall Interior", 800, 450)
download_image("map.jpg", "Mall Map", 800, 600)
download_image("contact-banner.jpg", "Visit Pine City Mall", 1200, 400)

# ====== SHOPS DATA ======
shops = [
    {"key":"style-haven", "name":"Style Haven", "category":"Clothing & Fashion"},
    {"key":"freshmart", "name":"FreshMart", "category":"Supermarket"},
    {"key":"tech-hub", "name":"Tech Hub", "category":"Electronics"},
    {"key":"book-nook", "name":"Book Nook", "category":"Books & Gifts"},
    {"key":"gadget-world", "name":"Gadget World", "category":"Electronics"},
    {"key":"food-court", "name":"Food Court", "category":"Dining"}
]
for shop in shops:
    download_image(f"{shop['key']}-logo.jpg", shop["name"], 300, 300)
    for i in range(1, 4):
        download_image(f"{shop['key']}-{i}.jpg", f"{shop['name']} {i}", 400, 250)

# ====== MOVIES DATA ======
movies = [
    {"key":"the-escape", "title":"The Escape", "actors":"Alex Star, Bella Lead", "age":"13+"},
    {"key":"family-tales", "title":"Family Tales", "actors":"Zara Hope, Liam Fields", "age":"PG"},
    {"key":"galaxy-wars", "title":"Galaxy Wars", "actors":"Chris Nova, Lee Star", "age":"13+"}
]
for movie in movies:
    download_image(f"{movie['key']}-poster.jpg", movie["title"], 300, 450)
    for i in range(1, 3):
        download_image(f"{movie['key']}-preview{i}.jpg", f"{movie['title']} Preview {i}", 200, 120)

# ====== CSS ======
css = """
:root {
  --primary-color: #004d40;
  --accent-color: #00796b;
  --bg-light: #f7f7f7;
  --text-dark: #222;
}
* { box-sizing: border-box; margin:0; padding:0; }
body { font-family: 'Poppins', sans-serif; background: var(--bg-light); color: var(--text-dark); }
header { background: var(--primary-color); color:white; padding:1rem 2rem; }
header h1 { margin-bottom:0.5rem; }
nav a { color:white; text-decoration:none; margin-right:1rem; font-weight:500; }
nav a:hover { text-decoration:underline; }
main { padding:2rem; }
.hero img { width:100%; border-radius:10px; }
.hero .overlay { position:absolute; top:50%; left:10%; transform:translateY(-50%); background:rgba(0,0,0,0.5); color:white; padding:1rem 2rem; border-radius:8px;}
.section { margin-top:2rem; }
.section h2 { color:var(--primary-color); margin-bottom:1rem; }
.shop-item, .movie-item { background:white; border-radius:8px; padding:1rem; box-shadow:0 2px 8px rgba(0,0,0,0.1); margin-bottom:1.5rem; }
.shop-item img.logo, .movie-item img.poster { width:120px; border-radius:8px; float:left; margin-right:1rem; }
.gallery { display:flex; gap:0.75rem; margin-top:0.75rem; }
.gallery img { width:calc((100% - 1.5rem)/3); border-radius:6px; }
footer { background:var(--primary-color); color:white; text-align:center; padding:2rem; margin-top:3rem; }
form { max-width:480px; margin:auto; display:flex; flex-direction:column; gap:1rem; }
form input, form textarea { padding:0.75rem; border:1px solid #ccc; border-radius:6px; }
form button { background:var(--accent-color); color:white; border:none; padding:0.75rem; border-radius:6px; cursor:pointer; font-size:1rem;}
form button:hover { background:var(--primary-color);}
@media (max-width:700px){ .shop-item img.logo,.movie-item img.poster{float:none;margin:0 0 1rem;width:100%;} }
"""
with open("css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

# ====== COMMON HEADER/FOOTER ======
header = """<header>
  <h1>Pine City Mall</h1>
  <nav>
    <a href='index.html'>Home</a>
    <a href='about.html'>About</a>
    <a href='map.html'>Map</a>
    <a href='shops.html'>Shops</a>
    <a href='movies.html'>Movies</a>
    <a href='contact.html'>Contact</a>
  </nav>
</header>"""

footer = "<footer><p>&copy; 2025 Pine City Mall — All rights reserved.</p></footer>"

# ====== PAGES ======
# Home
home = f"""
<!DOCTYPE html><html lang='en'><head>
<meta charset='UTF-8'><title>Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>{header}
<main>
<div class='hero'><img src='images/hero-mall.jpg'><div class='overlay'><h2>Welcome to Pine City Mall</h2><p>Your one-stop destination for shopping, dining & entertainment!</p></div></div>
<div class='section'><h2>Special Offers</h2>
<div class='gallery'>
  <img src='images/style-haven-1.jpg'>
  <img src='images/freshmart-1.jpg'>
  <img src='images/tech-hub-1.jpg'>
</div>
<p>Visit our featured stores for great seasonal discounts and promotions!</p>
</div>
</main>{footer}</body></html>
"""
open("index.html", "w", encoding="utf-8").write(home)

# About
about = f"""<!DOCTYPE html><html lang='en'><head>
<meta charset='UTF-8'><title>About - Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>{header}
<main><h2>About Pine City Mall</h2>
<p>Pine City Mall is a premier shopping and entertainment destination offering a vibrant mix of stores, restaurants, and entertainment venues. We strive to deliver a world-class experience for our visitors.</p>
<div class='gallery'>
<img src='images/interior1.jpg'><img src='images/interior2.jpg'><img src='images/food-court.jpg'>
</div></main>{footer}</body></html>"""
open("about.html", "w", encoding="utf-8").write(about)

# Map
map_page = f"""<!DOCTYPE html><html lang='en'><head>
<meta charset='UTF-8'><title>Map - Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>{header}
<main><h2>Mall Map</h2>
<p>Explore the layout of Pine City Mall to find your favorite stores and facilities.</p>
<img src='images/map.jpg' style='width:100%;border-radius:10px;'>
</main>{footer}</body></html>"""
open("map.html", "w", encoding="utf-8").write(map_page)

# Shops list
shops_html = f"""<!DOCTYPE html><html lang='en'><head>
<meta charset='UTF-8'><title>Shops - Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>{header}<main><h2>Shops at Pine City Mall</h2>"""
for shop in shops:
    shops_html += f"""
<div class='shop-item'>
  <img class='logo' src='images/{shop['key']}-logo.jpg'>
  <h3><a href='shops/{shop['key']}.html'>{shop['name']}</a></h3>
  <p>Category: {shop['category']}</p>
  <div class='gallery'>
    <img src='../images/{shop['key']}-1.jpg'>
    <img src='../images/{shop['key']}-2.jpg'>
    <img src='../images/{shop['key']}-3.jpg'>
  </div>
</div>"""
shops_html += "</main>"+footer+"</body></html>"
open("shops.html", "w", encoding="utf-8").write(shops_html)

# Individual shop pages
for shop in shops:
    shop_page = f"""<!DOCTYPE html><html lang='en'><head>
<meta charset='UTF-8'><title>{shop['name']} - Pine City Mall</title>
<link rel='../css/style.css' rel='stylesheet'>
</head><body>{header}
<main><h2>{shop['name']}</h2>
<img src='../images/{shop['key']}-logo.jpg' style='width:150px;'>
<p><strong>Category:</strong> {shop['category']}</p>
<p>Welcome to {shop['name']}, where you’ll find top-quality products and exceptional service.</p>
<div class='gallery'>
  <img src='../images/{shop['key']}-1.jpg'>
  <img src='../images/{shop['key']}-2.jpg'>
  <img src='../images/{shop['key']}-3.jpg'>
</div>
<p><a href='../shops.html'>← Back to Shops</a></p>
</main>{footer}</body></html>"""
    open(f"shops/{shop['key']}.html", "w", encoding="utf-8").write(shop_page)

# Movies list
movies_html = f"""<!DOCTYPE html><html lang='en'><head>
<meta charset='UTF-8'><title>Movies - Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>{header}<main><h2>Now Showing</h2>"""
for movie in movies:
    movies_html += f"""
<div class='movie-item'>
  <img class='poster' src='images/{movie['key']}-poster.jpg'>
  <h3><a href='movies/{movie['key']}.html'>{movie['title']}</a></h3>
  <p><strong>Actors:</strong> {movie['actors']}</p>
  <p><strong>Age:</strong> {movie['age']}</p>
  <div class='gallery'>
    <img src='../images/{movie['key']}-preview1.jpg'>
    <img src='../images/{movie['key']}-preview2.jpg'>
  </div>
</div>"""
movies_html += "</main>"+footer+"</body></html>"
open("movies.html", "w", encoding="utf-8").write(movies_html)

# Individual movie pages
for movie in movies:
    movie_page = f"""<!DOCTYPE html><html lang='en'><head>
<meta charset='UTF-8'><title>{movie['title']} - Pine City Mall</title>
<link rel='../css/style.css' rel='stylesheet'>
</head><body>{header}
<main><h2>{movie['title']}</h2>
<img src='../images/{movie['key']}-poster.jpg' style='width:200px;'>
<p><strong>Actors:</strong> {movie['actors']}</p>
<p><strong>Age Restriction:</strong> {movie['age']}</p>
<p><strong>Showtimes:</strong> 10:00 AM | 1:30 PM | 4:30 PM | 7:00 PM</p>
<p><strong>Synopsis:</strong> An exciting new blockbuster that will keep you on the edge of your seat!</p>
<p><a href='../movies.html'>← Back to Movies</a></p>
</main>{footer}</body></html>"""
    open(f"movies/{movie['key']}.html", "w", encoding="utf-8").write(movie_page)

# Contact
contact = f"""<!DOCTYPE html><html lang='en'><head>
<meta charset='UTF-8'><title>Contact - Pine City Mall</title>
<link rel='stylesheet' href='css/style.css'>
</head><body>{header}
<main><h2>Contact Us</h2>
<img src='images/contact-banner.jpg' style='width:100%;border-radius:10px;margin-bottom:1rem;'>
<p>Address: 123 Main Street, Pine City<br>
Phone: +27 11 555 1234<br>
Email: info@pinecitymall.co.za<br>
Hours: Mon–Sun 9am–9pm</p>
<form action='#' method='post'>
<input type='text' name='name' placeholder='Your Name' required>
<input type='email' name='email' placeholder='Your Email' required>
<textarea name='message' rows='5' placeholder='Your Message'></textarea>
<button type='submit'>Send Message</button>
</form>
</main>{footer}</body></html>"""
open("contact.html", "w", encoding="utf-8").write(contact)

print("✅ Pine City Mall website generated successfully with all pages and linked shop/movie pages.")
