import pandas as pd 

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(df):
    # For Handle Missing Value
    df.ffill(inplace=True)

    # for encode variable(categorical)
    df=pd.get_dummies(df,columns=['Sex','Embarked'],drop_first=True)

    # for removal of uneccessary columns
    df.drop(['Name','Ticket','Cabin'],axis=1,inplace=True)

    return df

if __name__ == "__main__":
    df = load_data('Titanic-Dataset.csv')
    processed_df = preprocess_data(df)
    print(processed_df.head())
