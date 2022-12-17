import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#for interactivity
from ipywidgets import interact

data = pd.read_csv('data.csv')
print("Shape of the dataset :", data.shape)
data.head()
data.describe()
data.describe()
data['label'].value_counts()

print("Average Ratio of Nitrogen in the soil : {0: .2f}".format(data['N'].mean()))
print("Average Ratio of Phosphorous in the soil : {0: .2f}".format(data['P'].mean()))
print("Average Ratio of Potassium in the soil : {0: .2f}".format(data['K'].mean()))
print("Average Temperature in Celsius : {0: .2f}".format(data['temperature'].mean()))
print("Average Relative humidity in % : {0: .2f}".format(data['humidity'].mean()))
print("Average PH Value of the soil : {0: .2f}".format(data['ph'].mean()))
print("Average Rainfall in mm : {0: .2f}".format(data['rainfall'].mean()))


# Summary Statistics For Each Crop
@interact
def summary(crops = list(data['label'].value_counts().index)):
    x = data[data['label'] == crops]
    print("----------------------------------------------")
    print("Statistics for Nitrogen")
    print("Minimum Nitrogen required : ", x['N'].min())
    print("Average Nitrogen required : ", x['N'].mean())
    print("Maximum Nitrogen required : ", x['N'].max())
    print("----------------------------------------------")
    print("Statistics for Phosphorous")
    print("Minimum Phosphorous required : ", x['P'].min())
    print("Average Phosphorous required : ", x['P'].mean())
    print("Maximum Phosphorous required : ", x['P'].max())
    print("----------------------------------------------")
    print("Statistics for Potassium")
    print("Minimum Potassium required : ", x['K'].min())
    print("Average Potassium required : ", x['K'].mean())
    print("Maximum Potassium required : ", x['K'].max())
    print("----------------------------------------------")
    print("Statistics for Temperature")
    print("Minimum Temperature required : {0: .2f}".format(data['temperature'].min()))
    print("Avergae Temperature required : {0: .2f}".format(data['temperature'].mean()))
    print("Maximum Temperature required : {0: .2f}".format(data['temperature'].max()))
    print("----------------------------------------------")
    print("Statistics for Humidity")
    print("Minimum Humidity required : {0: .2f}".format(data['humidity'].min()))
    print("Avergae Humidity required : {0: .2f}".format(data['humidity'].mean()))
    print("Maximum Humidity required : {0: .2f}".format(data['humidity'].max()))
    print("----------------------------------------------")
    print("Statistics for PH")
    print("Minimum PH required : {0: .2f}".format(data['ph'].min()))
    print("Avergae PH required : {0: .2f}".format(data['ph'].mean()))
    print("Maximum PH required : {0: .2f}".format(data['ph'].max()))
    print("----------------------------------------------")
    print("Statistics for Rainfall")
    print("Minimum Rainfall required : {0: .2f}".format(data['rainfall'].min()))
    print("Avergae Rainfall required : {0: .2f}".format(data['rainfall'].mean()))
    print("Maximum Rainfall required : {0: .2f}".format(data['rainfall'].max()))

    # Average Requirement For Each Crop With Average Conditions
    @interact
    def compare(conditions = ['N', 'P', 'K', 'temperature', 'ph', 'humidity', 'rainfall']):
        print("Average Value for", conditions,"is {0:.2f}".format(data[conditions].mean()))
        print("----------------------------------------------")
        print("Rice : {0:.2f}".format(data[(data['label'] == 'rice')][conditions].mean()))
        print("orange : {0:.2f}".format(data[(data['label'] == 'orange')][conditions].mean()))
        print("blackgram : {0:.2f}".format(data[(data['label'] == 'blackgram')][conditions].mean()))
        print("grapes : {0:.2f}".format(data[(data['label'] == 'grapes')][conditions].mean()))
        print("mango : {0:.2f}".format(data[(data['label'] == 'mango')][conditions].mean()))
        print("coffee : {0:.2f}".format(data[(data['label'] == 'coffee')][conditions].mean()))
        print("muskmelon : {0:.2f}".format(data[(data['label'] == 'muskmelon')][conditions].mean()))
        print("jute : {0:.2f}".format(data[(data['label'] == 'jute')][conditions].mean()))
        print("papaya : {0:.2f}".format(data[(data['label'] == 'papaya')][conditions].mean()))
        print("maize : {0:.2f}".format(data[(data['label'] == 'maize')][conditions].mean()))
        print("mungbean : {0:.2f}".format(data[(data['label'] == 'mungbean')][conditions].mean()))
        print("cotton : {0:.2f}".format(data[(data['label'] == 'cotton')][conditions].mean()))
        print("banana : {0:.2f}".format(data[(data['label'] == 'banana')][conditions].mean()))
        print("chickpea : {0:.2f}".format(data[(data['label'] == 'chickpea')][conditions].mean()))
        print("pigeonpeas : {0:.2f}".format(data[(data['label'] == 'pigeonpeas')][conditions].mean()))
        print("watermelon : {0:.2f}".format(data[(data['label'] == 'watermelon')][conditions].mean()))
        print("lentil : {0:.2f}".format(data[(data['label'] == 'lentil')][conditions].mean()))
        print("kidneybeans : {0:.2f}".format(data[(data['label'] == 'kidneybeans')][conditions].mean()))
        print("mothbeans : {0:.2f}".format(data[(data['label'] == 'mothbeans')][conditions].mean()))
        print("apple : {0:.2f}".format(data[(data['label'] == 'apple')][conditions].mean()))
        print("pomegranate : {0:.2f}".format(data[(data['label'] == 'pomegranate')][conditions].mean()))
        print("coconut : {0:.2f}".format(data[(data['label'] == 'coconut')][conditions].mean()))

