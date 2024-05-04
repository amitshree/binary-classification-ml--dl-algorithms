import pandas as pd

def get_data():
    original_df = pd.read_csv('data.csv')

    # Drop columns which doesn't contribute much to the survival decision
    transformed_df = original_df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])

    # One hot encoding of categorical columns
    transformed_df = pd.get_dummies(transformed_df, columns=['Sex', 'Embarked'], drop_first=True)

    # Fill missing values
    transformed_df['Age'].fillna(transformed_df['Age'].mean(), inplace=True)

    return (original_df, transformed_df)