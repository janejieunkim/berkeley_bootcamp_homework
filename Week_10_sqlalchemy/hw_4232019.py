from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

import numpy as np
import pandas as pd


engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# We can view all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Hawaii Climate API <br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )



@app.route("/api/v1.0/precipitation")
def precipitation():
     # Calculate previous year date
    previous_yr = dt.date(2017, 8, 1) - dt.timedelta(days=365)

    # Query date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= previous_yr).all()

    # Dictionary with date as the key and prcp as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    result = session.query(Station.station).all()

    stations = list(np.ravel(result))
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    # Calculate previous year date
    previous_yr = dt.date(2017, 8, 1) - dt.timedelta(days=365)

    # Query the primary station for tob
    result = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= previous_yr).all()

    temps = list(np.ravel(result))

    return jsonify(temps)


@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
 
    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # calculate TMIN, TAVG, TMAX 
        result = session.query(*sel).\
            filter(Measurement.date >= start).all()
   
        temps = list(np.ravel(result))
        return jsonify(temps)

    # calculate TMIN, TAVG, TMAX
    result = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
   
    temps = list(np.ravel(result))
    return jsonify(temps)


if __name__ == '__main__':
    app.run()
