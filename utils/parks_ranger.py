"""This module provides a function to explore a number of possible estimators
for a random forest and returns a RandomForest object with the ideal number of
estimators.
"""
from .progress import update_progress

import pandas as pd
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier


def create_ideal_forest(
    num_estimators: int,
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_test: pd.DataFrame,
) -> RandomForestClassifier:
    """_summary_

    Args:
        num_estimators (int): The maximum number of estimators to test out
        x_train (pd.DataFrame): The training data
        y_train (pd.DataFrame): The training labels
        x_test (pd.DataFrame): The validation data
        y_test (pd.DataFrame): The validation labels

    Returns:
        RandomForestClassifier: The best random forest classifier out of the
        bunch
    """

    rf_df = pd.DataFrame()

    for num_estim in range(1, num_estimators):
        update_progress(num_estim / num_estimators)
        model = RandomForestClassifier(n_estimators=num_estim, random_state=42)
        model.fit(x_train, y_train)
        y_pred5 = model.predict(x_test)

        rf_df = pd.concat(
            [
                rf_df,
                pd.DataFrame(
                    [
                        {
                            "Estimators": num_estim,
                            "F1 Score": f1_score(y_test, y_pred5, average="weighted"),
                        }
                    ]
                ),
            ],
            ignore_index=True,
        )
    
    update_progress(1)

    rf_df = rf_df.reset_index()

    ideal_num_estimators = rf_df.loc[rf_df["F1 Score"].idxmax()]["Estimators"]

    print(f"Found the ideal number of estimators is {ideal_num_estimators}")

    return RandomForestClassifier(n_estimators=int(ideal_num_estimators), random_state=42)
