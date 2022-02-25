import streamlit as st
import requests
import pandas as pd
import numpy as np

st.markdown('''
# Rei's NY Taxi App
## All hail
Use this app to input your time, coordinates and how many of you there are, get an estimate of the fare.
''')

date = st.date_input('Day of Travel')
time = st.time_input('Time of Travel')
pickup_longitude = st.text_input('Pickup Longitude')
pickup_latitude = st.text_input('Pickup Latitude')
dropoff_longitude = st.text_input('Dropoff Longitude')
dropoff_latitude = st.text_input('Dropoff Latitude')
passenger_count = st.text_input('Number of Passengers')

if st.button('Submit'):

    url = 'https://fast-taxi-2g6nxe3ofq-ew.a.run.app/predict'

    params = {
        'pickup_datetime': str(date) + ' ' + str(time),
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }

    response = requests.get(url, params=params).json()
    fare = response['fare']

    st.text(f'Your estimated fare is {fare}')

    df = pd.DataFrame(
                np.array([[float(pickup_latitude), float(dropoff_latitude)],
                        [float(pickup_longitude), float(dropoff_longitude)]]),
                columns=['lat', 'lon']
            )

    st.map(df)
