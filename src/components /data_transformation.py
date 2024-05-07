import numpy as np
import sys
from dataclasses import dataclass
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import os


@dataclass()
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            numerical_feature = [
                "reading_score",
                "writing_score"
            ]
            categorical_feature = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]

            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy="median")),
                    ('scaler', StandardScaler())
                ]
            )

            logging.info('Numerical Transformation Complete')

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy="most_frequent")),
                    ('one_hot_encoder', OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )
            logging.info('Catagorical Transformation Complete')

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_feature),
                    ('cat_pipeline', cat_pipeline, categorical_feature)
                ]
            )

            logging.info('Combined Transformation Complete')

            return preprocessor

        except Exception as E:
            logging.info(f'Exception {E}')
            raise CustomException(E, sys)

    def initiate_date_transformation(self, train_path, test_path):
        try:
                train_df = pd.read_csv(train_path)
                test_df = pd.read_csv(test_path)
                logging.info('Train/Test Read')

                preprocessor = self.get_data_transformer_object()

                target_column = "math_score"
                numerical_feature = [
                    "reading_score",
                    "writing_score"
                ]

                input_feature_train_df = train_df.drop(columns=target_column,axis=1)
                target_feature_train_df = train_df[target_column]
                input_feature_test_df = test_df.drop(columns=target_column,axis =1)
                target_feature_test_df = test_df[target_column]

                logging.info('Applying Preprocessing')

                input_feature_train = preprocessor.fit_transform(input_feature_train_df)
                input_feature_test = preprocessor.transform(input_feature_test_df)


                train_arr = np.c_[
                    input_feature_train,np.array(target_feature_train_df)
                ]
                test_arr = np.c_[
                    input_feature_test,np.array(target_feature_test_df)
                ]

                save_object(
                    file_path = self.data_transformation_config.preprocessor_obj_file_path,
                    obj = preprocessor
                )
                logging.info('Saved Preprocessing Object.')

                return (
                    train_arr,
                    test_arr,
                    self.data_transformation_config.preprocessor_obj_file_path,
                )
        except Exception as E:
            logging.info(f'Error- {E}')
            raise Exception
