import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

winesR = pd.read_csv('winequality-red.csv', sep=';')
winesW = pd.read_csv('winequality-white.csv', sep=';')
winesR.info()
winesW.info()
winesR['fixed acidity'].value_counts()
winesR['fixed acidity'].mean()
sns.distplot(winesW['quality'], rug=True, kde=False);

sns.jointplot(winesW['quality'], winesR['volatile acidity'], kind='kde')
sns.jointplot(winesW['quality'], winesR['alcohol'], kind='kde', color='g')
sns.jointplot(winesW['quality'], winesR['total sulfur dioxide'], kind='kde', color='red')