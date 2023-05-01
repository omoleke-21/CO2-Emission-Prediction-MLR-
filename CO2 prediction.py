# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/omole/Downloads/Machine learning/CO2 emission prediction (From modelling to deployment)/CO2trained_model.sav', 'rb'))


input = (2.0,4,8.5)
# changing the input_data to numpy array
input_as_numpy_array = np.asarray(input)

# reshape the array as we are predicting for one instance
input_reshaped = input_as_numpy_array.reshape(1,-1)

#prediction = loaded_model.predict(input_data_reshaped)
CO2_prediction = 66.08027751 + (11.16646391*input[0]) + (7.19082629*input[1]) + (9.73993878*input[2])
print("carbon dioxide emmission value is:", CO2_prediction)