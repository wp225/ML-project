import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from data_transformation import DataTransformation, DataTransformationConfig
from model_trainer import ModelTrainer,ModelTrainerConfig

@dataclass()
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Entered Data Ingestion')
        try:
            df = pd.read_csv('/Users/anshujoshi/PycharmProjects/ML-Project/notebook/stud_data.csv')
            logging.info('Data Read Sucessfully as DataFrame')

            os.makedirs((os.path.dirname(self.ingestion_config.train_data_path)), exist_ok=True)
            os.makedirs((os.path.dirname(self.ingestion_config.test_data_path)), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train Test Initiated')

            train_set, test_set = train_test_split(df, test_size=.2, random_state=123)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Data Ingestion Complete')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )


        except Exception as E:
            logging.info(f'Error: {E}')
            raise CustomException(E, sys)


if __name__ == '__main__':
    injector = DataIngestion()
    train_data, test_data = injector.initiate_data_ingestion()
    data_transformation= DataTransformation()
    train_array,test_array,_ = data_transformation.initiate_date_transformation(test_data,test_data)
    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_array,test_array,)