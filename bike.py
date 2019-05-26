import numpy as np
import pandas as pd


train = pd.read_csv("data/train.csv", parse_dates=["datetime"])
test = pd.read_csv("data/test.csv", parse_dates=["datetime"])

#print(train.shape)
#print(test.shape)

import seaborn as sns
import matplotlib.pyplot as plt

train["year"] = train["datetime"].dt.year
train["month"] = train["datetime"].dt.month
train["day_date"] = train["datetime"].dt.day
train["hour"] = train["datetime"].dt.hour
train["minute"] = train["datetime"].dt.minute
train["second"] = train["datetime"].dt.second

test["year"] = test["datetime"].dt.year
test["month"] = test["datetime"].dt.month
test["hour"] = test["datetime"].dt.hour

train["day"] = train["datetime"].dt.dayofweek
test["day"] = test["datetime"].dt.dayofweek

#print(test.year)
