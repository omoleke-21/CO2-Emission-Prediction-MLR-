# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 15:36:29 2023

@author: omole
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/omole/Downloads/Machine learning/CO2 emission prediction (From modelling to deployment)/CO2trained_model.sav', 'rb'))


def CO2_emmision_prediction(input):
    
  #input = (2.0,4,8.5)
  # changing the input_data to numpy array
  input_as_numpy_array = np.asarray(input)

  # reshape the array as we are predicting for one instance
  input_reshaped = input_as_numpy_array.reshape(1,-1)

  #prediction = loaded_model.predict(input_data_reshaped)
  CO2_prediction = 66.08027751 + (11.16646391*input[0]) + (7.19082629*input[1]) + (9.73993878*input[2])
  return CO2_prediction
      
def main():
    #title for webapp
    st.title('CO2 Emission Prediction')
    
    enginesize = st.number_input('engine size of the car')
    cylinders = st.number_input('number of cylinders')
    fuel_consumption = st.number_input('fuel consumption of the car')
    
    CO2_prediction = ''
    if st.button('CO2 prediction'):
        CO2_prediction = CO2_emmision_prediction([enginesize, cylinders, fuel_consumption])
        st.success(CO2_prediction)
        
if __name__=='__main__':
    main()
    