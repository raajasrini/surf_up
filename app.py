import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask , jasonify

engine = create_engine("sqlite:///hawaii.sqlite")
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

print("example __name__ = %s", __name__)
if __name__ == "__main__":
    print("example is being run directly.")
else:
    print("example is being imported")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

