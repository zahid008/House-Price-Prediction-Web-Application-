from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# Create your views here.
def home(request):
    return render(request, 'home.html')


def prediction(request):
    return render(request, 'prediction.html')


def outcome(request):
    data = pd.read_csv(r'hpp/USA_Housing.csv')
    data = data.drop(['Address'], axis=1)
    X = data.drop('Price', axis=1)
    Y = data['Price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.03)
    model = LinearRegression()
    model.fit(X_train, Y_train)

    income = float(request.GET['i'])
    age = float(request.GET['a'])
    room = float(request.GET['r'])
    bedroom = float(request.GET['b'])
    population = float(request.GET['p'])

    predictIt = model.predict(np.array([income, age, room, bedroom, population]).reshape(1, -1))

    return render(request, 'prediction.html', {'message': predictIt})


def about(request):
    return render(request,'about.html')