import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def load_data(file_path):
    return pd.read_csv(file_path)

def train_model(df):
    x = df.drop('Survived', axiz=1)
    y = df['Survived']

    X_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

    model = RandomForestClassifier(n_estimators = 100, random_state = 42)
    model.fit(X_train, y_train)

    return model,X_test, y_test

def evaluation_model(model, X_test, y_test):
    prediction = model.predict(X_test)
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))


if __name__ == "__main__":
    df = load_data('Titanic-Dataset.csv')
    model, X_test, y_test = train_model(df)
    evaluation_model(model, X_test, y_test)
