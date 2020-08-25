import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

data = pd.read_csv('india.csv',sep=',')
data = data[['day','confirmed']]

x = np.array(data['day']).reshape(-1,1)
y = np.array(data['confirmed']).reshape(-1,1)
plt.plot(y,'-m')

polyFeat = PolynomialFeatures(degree=3)
x = polyFeat.fit_transform(x)

model = linear_model.LinearRegression()
model.fit(x,y)

accuracy = model.score(x,y)
y0 = model.predict(x)

def accuracyConfirmed():
    print(f'Accuracy-Confirmed_cases:{round(accuracy*100,3)}%')

def predictConfirmed(days):
    print("Confirmed: ",round(int(model.predict(polyFeat.fit_transform([[208+days]])))/1000000,2),'Million')
    
def plotConfirmed(days):
    x1 =np.array(list(range(1,208+days))).reshape(-1,1)
    y1 = model.predict(polyFeat.fit_transform(x1))
    plt.plot(y0,'--b')
    plt.plot(y1,'--r')
    plt.show()