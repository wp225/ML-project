import os
import sys
import pandas as pd
import numpy as np
from src.logger import logging
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as E:
        logging.info('Pickel File Save - Failed')
        raise Exception(E, sys)

    logging.info('Saved Preprocessing Object.')


def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}

        for _, model in models.items():
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            test_score = r2_score(y_test, y_test_pred)

            report[model] = test_score

        logging.info('All model trained sucessfully')

        return report
    except Exception as E:
        logging.info('Failed Training Model')
        raise CustomException(E, sys)
