import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn

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

'''This function generates a heatmap that shows the positive/negative correlations between students' university, dept, year, anxiety label, and whether they received a waiver/scholarship'''
def show_anxiety_levels():
    # Make a smaller df for the columns we need
    smaller_df = df[['3. University', '4. Department', '5. Academic Year', 'Anxiety Label', '7. Did you receive a waiver or scholarship at your university?']]

    # Initialize the LabelEncoder
    le = LabelEncoder()

    # Fit and transform the data
    encoded_uni = le.fit_transform(smaller_df['3. University'])
    encoded_dept = le.fit_transform(smaller_df['4. Department'])
    encoded_year = le.fit_transform(smaller_df['5. Academic Year'])
    encoded_anxiety = le.fit_transform(smaller_df['Anxiety Label'])
    encoded_schol = le.fit_transform(smaller_df['7. Did you receive a waiver or scholarship at your university?'])

    # Make a df off of the encoded data
    enc_df = pd.DataFrame({
        'Encoded University': encoded_uni,
        'Encoded Department': encoded_dept,
        'Encoded Academic Year': encoded_year,
        'Encoded Anxiety Label': encoded_anxiety,
        'Encoded Scholarship Label': encoded_schol
    })

    # Make a correlation matrix and display the heatmap
    corr_matrix = enc_df.corr()
    seaborn.heatmap(corr_matrix, annot=True)
    plt.title("Frequency of Anxiety Levels: Did receiving a scholarship/waiver mitigate anxiety?")
    plt.show()

    # print the encoded correlation matrix
    print("Encoded df:", corr_matrix)

'''This function generates a heatmap that shows the positive/negative correlations between students' anxiety, stress, their current CGPA'''
def show_stress_levels():
    # Make a smaller df for the columns we need
    smaller_df = df[['Anxiety Label', 'Stress Label', '6. Current CGPA']]

    # Initialize the LabelEncoder
    le = LabelEncoder()

    # Fit and transform the data
    encoded_gpa = le.fit_transform(smaller_df['6. Current CGPA'])
    encoded_stress = le.fit_transform(smaller_df['Stress Label'])
    encoded_anxiety = le.fit_transform(smaller_df['Anxiety Label'])

    # Make a df off of the encoded data
    enc_df = pd.DataFrame({
        'Encoded GPA': encoded_gpa,
        'Encoded Stress': encoded_stress,
        'Encoded Anxiety Label': encoded_anxiety
    })

    # Make a correlation matrix and display the heatmap
    corr_matrix = enc_df.corr()
    seaborn.heatmap(corr_matrix, annot=True)
    plt.title("Frequency of Stress Levels: How does anxiety level and GPA relate to stress levels?")
    plt.show()

    # print the encoded correlation matrix
    print("Encoded df:", corr_matrix)

'''This function generates a heatmap that shows the positive/negative correlations between students' depression, stress, and anxiety levels'''
def show_depression_levels():
    # Make a smaller df for the columns we need
    smaller_df = df[['Depression Label', 'Stress Label', 'Anxiety Label']]

    # Initialize the LabelEncoder
    le = LabelEncoder()

    # Fit and transform the data
    encoded_stress = le.fit_transform(smaller_df['Stress Label'])
    encoded_depression = le.fit_transform(smaller_df['Depression Label'])
    encoded_anxiety = le.fit_transform(smaller_df['Anxiety Label'])

    # Make a df off of the encoded data
    enc_df = pd.DataFrame({
        'Encoded Depression': encoded_depression,
        'Encoded Stress': encoded_stress,
        'Encoded Anxiety Label': encoded_anxiety
    })

    # Make a correlation matrix and display the heatmap
    corr_matrix = enc_df.corr()
    seaborn.heatmap(corr_matrix, annot=True)
    plt.title("Frequency of Depression Levels: Higher anxiety, higher stress, or both?")
    plt.show()

    # print the encoded correlation matrix
    print("Encoded df:", corr_matrix)