import pandas as pd

def get_data():
    df = pd.read_csv('data.csv')

    # Drop columns which doesn't contribute much to the survival decision
    dataframe = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])

    # One hot encoding of categorical columns
    dataframe = pd.get_dummies(dataframe, columns=['Sex', 'Embarked'], drop_first=True)

    # Fill missing values
    dataframe['Age'].fillna(dataframe['Age'].mean(), inplace=True)

    return dataframe

get_data()