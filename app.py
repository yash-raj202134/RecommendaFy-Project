from flask import Flask, request, render_template  # type: ignore
import pandas as pd # type: ignore
import random
from recommendafy.utils import truncate




app = Flask(__name__)

# Loading files
trending_products = pd.read_csv("data/trending_products.csv")
train_data = pd.read_csv("data/clean_data.csv")



# routes ----------------------------------------------------


# List of predefined image URLs
random_image_urls = [
    "recommendafy/web/static/images/img_1.png",
    "recommendafy/web/static/images/img_2.png",
    "recommendafy/web/static/images/img_3.png",
    "recommendafy/web/static/images/img_4.png",
    "recommendafy/web/static/images/img_5.png",
    "recommendafy/web/static/images/img_6.png",
    "recommendafy/web/static/images/img_7.png",
    "recommendafy/web/static/images/img_8.png",
]

@app.route("/")
def index():
    # Create a list of random image URLs for each product
    random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
    price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
    return render_template('index.html',trending_products=trending_products.head(8),truncate = truncate,
                           random_product_image_urls=random_product_image_urls,
                           random_price = random.choice(price))
