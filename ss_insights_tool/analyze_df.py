import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../ss_data.csv")

'''This function shows the percentages of the 18-22 and 23-26 age ranges, and then drops the age column inplace'''
def show_and_clear_ages():
    # We only want 18-22 and 23-26 age ranges, other answers are deprecated
    df.query('`1. Age` == "18-22" or `1. Age` == "23-26"', inplace=True)

    df["1. Age"].value_counts().plot(kind="pie")
    plt.show()
    df.drop(["1. Age"], axis=1, inplace=True)

'''This function shows the percentages of the male and female demographics, and then drops the gender column inplace'''
def show_and_clear_gender():
    # We only want Males and Females, other answers are deprecated
    df.query('`2. Gender` == "Male" or `2. Gender` == "Female"', inplace=True)

    df["2. Gender"].value_counts().plot(kind="pie")
    plt.show()
    df.drop(["2. Gender"], axis=1, inplace=True)

show_and_clear_ages()
show_and_clear_gender()
print(df.head())