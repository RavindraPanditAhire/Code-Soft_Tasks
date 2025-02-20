import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 

def load_data(file_path):
    return pd.read_csv(file_path)

def plot_survival_count(df):
    sns.countplot(x='Survived', data = df)
    plt.title('Survivat Rate by Passenger Class')
    plt.xlabel('Survived (0=No , 1=Yes)')
    plt.ylabel('Count')
    plt.show()

def plot_class_distribution(df):
    sns.barplot(x='Pclass', y='Survived', data = df)
    plt.title('Survivat Rate by Passenger Class')
    plt.xlabel('Passemger Class')
    plt.ylabel('Survival Rate')
    plt.show()

    if __name__== "__main__":
        df = load_data('Titanic-Dataset.csv')
        plot_survival_count(df)
        plot_class_distribution(df)
