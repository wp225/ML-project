# End-to-End Machine Learning Project with Flask App

This project demonstrates the end-to-end workflow of a machine learning project, including data ingestion, preprocessing, model training, and deployment using Flask.

## Project Structure

ML-project/
│
├── notebook/
│ ├── EDA.ipynb
│ └── model_training.ipynb
│
├── src/
│ ├── components/
│ │ ├── artifacts/
│ │ │ ├── data.csv
│ │ │ ├── train.csv
│ │ │ ├── test.csv
│ │ │ ├── model.pkl
│ │ │ └── preprocessor.pkl
│ │ ├── data_ingestion.py
│ │ ├── data_transformation.py
│ │ └── model_trainer.py
│ ├── pipeline/
│ │ ├── infer_pipeline.py
│ │ └── training_pipeline.py
│ ├── exceptions.py
│ ├── logger.py
│ └── utils.py
│
└── templates/
|  ├── home.html
|  └── index.html
|── application.py
|── app.py

## Usage:

1. EDA.ipynb: Jupyter notebook for exploratory data analysis.
2. model_training.ipynb: Jupyter notebook for training machine learning models.
3. data_ingestion.py: Module for ingesting raw data.
4. data_transformation.py: Module for preprocessing data.
5. model_trainer.py: Module for training machine learning models.
6. infer_pipeline.py: Module for inference pipeline.
7. training_pipeline.py: Module for training pipeline.
8. exceptions.py: Module for custom exceptions.
9. logger.py: Module for logging.
10. utils.py: Module containing utility functions.
11. templates/: HTML templates for the Flask web application.

## How to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/wp225/ML-project.git
   cd ML-project
   
2. Create a docker image:
   docker build -t flask-app .
   
3.Run Docker Container:
  docker run -p 5000:5000 flask-app
