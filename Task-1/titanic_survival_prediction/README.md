

# Titanic Survival Prediction

## Project Description
This project aims to predict the survival of passengers on the Titanic based on various features such as age, sex, and fare. The goal is to apply machine learning techniques to analyze the dataset and build a predictive model that can classify whether a passenger survived or not.

## Dataset Information
- **Source:** [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data)
- **Features:**
  - `PassengerId`: Unique identifier for each passenger
  - `Survived`: Survival status (0 = No, 1 = Yes)
  - `Pclass`: Ticket class (1st, 2nd, 3rd)
  - `Name`: Name of the passenger
  - `Sex`: Gender of the passenger
  - `Age`: Age of the passenger
  - `SibSp`: Number of siblings/spouses aboard
  - `Parch`: Number of parents/children aboard
  - `Ticket`: Ticket number
  - `Fare`: Ticket fare
  - `Cabin`: Cabin number
  - `Embarked`: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

## Installation Instructions
To set up the project, clone the repository and install the required packages:
```bash
git clone <repository_url>
cd titanic_survival_prediction
pip install -r requirements.txt

## Usage Instructions
## Run the main script to execute the prediction model:


python main.py
Model Evaluation
The model achieved an accuracy of 80% on the test dataset, with a precision of 0.75 and a recall of 0.70. The evaluation metrics indicate that the model performs reasonably well in predicting survival.

Results
Key findings include:

Females had a higher survival rate compared to males.
Passengers in first class had a significantly higher chance of survival than those in second or third class.
Younger passengers tended to have a higher survival rate.

Conclusion
The project demonstrated that various factors, including gender and class, significantly influenced survival on the Titanic. Future work could involve exploring more advanced modeling techniques or incorporating additional features for improved predictions.