from data_preprocessing import load_data,preprocess_data
from exploratory_analysis import plot_survival_count,plot_class_distribution
from titanic_model import train_model,evaluation_model

if __name__ == "__main__":
    df = load_data('Titanic-Dataset.csv')
    processed_df = preprocess_data(df)
    plot_survival_count(processed_df)
    plot_class_distribution(processed_df)

    model, X_test, y_test = train_model(df)
    evaluation_model(model, X_test, y_test)
