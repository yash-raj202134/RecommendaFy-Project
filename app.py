from flask import Flask, request, render_template  # type: ignore
import pandas as pd # type: ignore
import random
from recommendafy.utils import truncate




app = Flask(__name__)

# Loading files
