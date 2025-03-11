import pickle
import sklearn
import numpy as np
import pandas as pd
file=pd.read_csv("Housing.csv")
house=pd.DataFrame(file)
# print(house.info())
house=house.replace("yes",1)
house=house.replace("no",0)
# # print(house.info())
# print(house["furnishingstatus"].unique())
house=house.replace("furnished",1)
house=house.replace("unfurnished",0)
house=house.replace("semi-furnished",0.5)
x=house[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
       'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
       'parking', 'prefarea', 'furnishingstatus']]
y=house["price"]
# print(x.shape,y.shape)
from sklearn.preprocessing import StandardScaler
scalar=StandardScaler()
scalar1=scalar.fit_transform(x)
# # print(scalar)
x_sc=pd.DataFrame(scalar1,columns=[['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad',
       'guestroom', 'basement', 'hotwaterheating', 'airconditioning',
       'parking', 'prefarea', 'furnishingstatus']])
# print(x_sc)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_sc,y,random_state=40,test_size=0.30)
# print(x_train.shape,X_test.shape,y_train.shape,Y_test.shape)
from sklearn.linear_model import LinearRegression
lg=LinearRegression()
lg.fit(x_train,y_train)

with open ("train3133.pkl","wb") as file:
    pickle.dump({"model":lg,"scalar":scalar},file)
print("Pickle file is generated successfully")