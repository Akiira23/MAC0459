import csv
import numpy as np
import matplotlib.pyplot as plt


with open('winequality-red.csv', 'r') as f:
    winesR = list(csv.reader(f, delimiter=';'))

winesR = np.array(winesR[1:], dtype = np.float)
print('MediaTinto:', winesR.mean(0))
print('VarianciaTinto:', winesR.var(0))
print('ValorMinimoTinto:', np.amin(winesR, axis = 0))
print('MedianaTinto:', np.median(winesR, axis = 0))
print('ValorMaximoTinto:', np.amax(winesR, axis = 0))

with open('winequality-white.csv', 'r') as f:
    winesW = list(csv.reader(f, delimiter=';'))

winesW = np.array(winesR[1:], dtype = np.float)
print('MediaBranco:', winesW.mean(0))
print('VarianciaBranco:', winesW.var(0))
print('ValorMinimoBranco:', np.amin(winesW, axis = 0))
print('MedianaBranco:', np.median(winesW, axis = 0))
print('ValorMaximoBranco:', np.amax(winesW, axis = 0))

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
axs[0].hist(winesR[:,0], bins='auto', color = "red")
axs[1].hist(winesW[:,0], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,1], bins='auto', color = "red")
axs[1].hist(winesW[:,1], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,2], bins='auto', color = "red")
axs[1].hist(winesW[:,2], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,3], bins='auto', color = "red")
axs[1].hist(winesW[:,3], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,4], bins='auto', color = "red")
axs[1].hist(winesW[:,4], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,5], bins='auto', color = "red")
axs[1].hist(winesW[:,5], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,6], bins='auto', color = "red")
axs[1].hist(winesW[:,6], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,7], bins='auto', color = "red")
axs[1].hist(winesW[:,7], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,8], bins='auto', color = "red")
axs[1].hist(winesW[:,8], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,9], bins='auto', color = "red")
axs[1].hist(winesW[:,9], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,10], bins='auto', color = "red")
axs[1].hist(winesW[:,10], bins='auto', color = "grey")

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

axs[0].hist(winesR[:,11], bins='auto', color = "red")
axs[1].hist(winesW[:,11], bins='auto', color = "grey")