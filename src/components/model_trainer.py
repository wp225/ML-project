from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from catboost import CatBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import evaluate_model, save_object

import os
import sys


@dataclass
class ModelTrainerConfig:
    trained_model_file = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Splitting Training Test Data')
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )

            models = {
                'Linear': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'Random Forrest': RandomForestRegressor(),
                'SVR': SVR(),
                'KNN': KNeighborsRegressor(),

            }

            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            logging.info('Model Report Generated Sucessfully')
            best_model = list(sorted(model_report.items(), key=lambda x: x[1]))[-1]

            print(best_model[0],best_model[1])

            save_object(
                file_path=self.model_trainer_config.trained_model_file,
                obj=best_model[0]
            )
            logging.info('Model Saved Sucessfully')

        except Exception as E:
            logging.info('Model Training Failed')
            raise CustomException(sys, E)
