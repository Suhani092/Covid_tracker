import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from covid import Covid
import pandas as pd
import numpy as np

def showdata():
    covid = Covid()

    cases = []
    deaths = []
    confirmed = []
    active = []
    recovered = []

    try:
        countries = data.get()
        country_names = [country.strip() for country in countries.split(",")]

        for country in country_names:
            try:
                print(f"Fetching data for: {country}")
                status = covid.get_status_by_country_name(country)
                confirmed.append(status["confirmed"])
                active.append(status["active"])
                recovered.append(status["recovered"])
                deaths.append(status["deaths"])
            except Exception as e:
                print(f"Error fetching data for {country}: {e}")
                confirmed.append(0)
                active.append(0)
                recovered.append(0)
                deaths.append(0)

        confirmed_patch = mpatches.Patch(color='green', label='confirmed')
        active_patch = mpatches.Patch(color='red', label='active') 
        recovered_patch = mpatches.Patch(color='yellow', label='recovered') 
        deaths_patch = mpatches.Patch(color='blue', label='deaths') 

        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])

        for x in range(len(country_names)):
            plt.bar(country_names[x], confirmed[x], color='green')
            plt.bar(country_names[x], active[x], color='red')
            plt.bar(country_names[x], recovered[x], color='yellow')
            plt.bar(country_names[x], deaths[x], color='blue')
        
        plt.title('Current Covid Cases')
        plt.xlabel('Country names')
        plt.ylabel('Cases (in millions)')
        plt.show()

    except Exception as e:
        print(f"General error: {e}")
        data.set("Enter correct details again")

root = Tk()
root.geometry("600x400")
root.title("Covid-19 Data")

# Replace the path below with the path to your image
img_path = r"C:\covid data visualizer\covid19.jpg" 
img = ImageTk.PhotoImage(Image.open(img_path))
panel = Label(root, image=img)
panel.pack(fill="both", expand="no")

Label(root, text="Enter Countries Name", font="Rubik 11").pack()

data = StringVar()
entry = Entry(root, textvariable=data, width=70).pack()
Button(root, text="Get Data", command=showdata).pack()

root.mainloop()

