from flask import Flask, request, render_template  # type: ignore
import pandas as pd # type: ignore
import random

app = Flask(__name__)

