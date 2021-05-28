import streamlit as st
import datetime
import requests

'''
# Welcome to the Taxi Fare Prediction page
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

'''
### Dear customer, please provide following inputs to calculate the taxi fare prediction:

'''

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

pickup_date = st.date_input(
    "Insert date",
    datetime.date(2021, 5, 28))

pickup_time = st.time_input('Insert time', datetime.time(9, 0))

pickup_longitude = st.number_input('Insert pick up longitude')

pickup_latitude = st.number_input('Insert pick up latitude')

dropoff_longitude = st.number_input('Insert drop off longitude')

dropoff_latitude = st.number_input('Insert drop off latitude')

passenger_count = st.number_input('Insert passenger count', min_value=0)

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

# url = 'http://localhost:8000/predict' # use this url when using docker run putting own predict API to webserver
url = 'https://taxifare.lewagon.ai/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

params = {'pickup_datetime': f'{pickup_date} {pickup_time}',
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': int(passenger_count)}

response = requests.get(url, params=params)
prediction = response.json()['prediction']

st.write('Taxi fare prediction is', f'{prediction:.2f} USD')
