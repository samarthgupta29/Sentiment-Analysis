import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tkinter
from tkinter import *

twitter_data = pd.read_csv('result.csv')
window=Tk()
window.geometry("600x400")


plt.figure()
hist1,edges1 = np.histogram(twitter_data.friends)
plt.bar(edges1[:-1],hist1,width=edges1[1:]-edges1[:-1])

window.mainloop()
plt.scatter(twitter_data.followers,twitter_data.retwc)