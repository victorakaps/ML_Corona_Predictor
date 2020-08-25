from datetime import date

from recovered import *
from active import *
from confirmed import *
from deceased import *

def plot():
    plotConfirmed(days) 
    plotActive(days)
    plotDeceased(days)
    plotRecovered(days)

def accuracy():
    accuracyConfirmed()
    accuracyActive()
    accuracyDeceased()
    accuracyRecovered()

def prediction():
    predictConfirmed(days)
    predictRecovered(days)
    predictActive(days)
    predictDeceased(days)
    choice = int(input('Enter 1 to check accuracy of model and 2 to see plotted data: '))
    if choice == 2:
        plot()
    elif choice == 1:
        accuracy()

year = int(input('Enter year(eg 2020): '))
month = int(input('Enter month(eg 11 for nov): '))
day = int(input('Enter day(eg 20): '))
print('\n')
predict_date = date(year, month, day)

init_date = date(2020, 8, 24)
delta = predict_date - init_date
days = delta.days
print(f'Prediction of {predict_date} is as follow:')
prediction()