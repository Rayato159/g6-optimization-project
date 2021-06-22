import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

class Polynomial:
    def __init__(self, X, y, degree):
        self.X = X
        self.y = y

        self.degree = degree

        self.poly = PolynomialFeatures(self.degree)
        self.X_poly = self.poly.fit_transform(self.X)

        self.model = LinearRegression()

    def getFit(self):
        self.model.fit(self.X_poly, self.y)
        return self.model
    
    def getPredict(self):
        self.predict = self.model.predict(self.X_poly)
        return self.predict

    def getScore(self):
        self.score = self.model.score(self.X_poly, self.y)
        return self.score

    def getCoef(self):
        return self.model.coef_

    def getIntercept(self):
        return self.model.intercept_

class Equation():
    def __init__(self):
        self.df = pd.read_csv("../graph/exam1_output.csv")

        self.X = self.df[["X"]]
        self.y = self.df["Y"]

        self.my_model = Polynomial(self.X, self.y, 12)
        self.my_model.getFit()

        self.predict = self.my_model.getPredict()

        self.my_model.getScore()

        self.coef = self.my_model.getCoef()
        self.intercept = self.my_model.getIntercept()-1

