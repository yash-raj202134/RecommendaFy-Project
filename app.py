from flask import Flask, request, render_template  # type: ignore
import pandas as pd # type: ignore
import random
from recommendafy.utils import truncate




app = Flask(__name__)

# Loading files
trending_products = pd.read_csv("data/trending_products.csv")
train_data = pd.read_csv("data/clean_data.csv")
