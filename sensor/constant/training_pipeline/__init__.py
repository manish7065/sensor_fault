import os



#defining common constant variable for training pipeline
TARGET_COLUMN : str = 'class'
PIPELINE_NAME : str = 'sensor'
ARTIFACT_DIR : str = 'artifact'
FILE_NAME : str = 'sensor.csv'

TRAIN_FILE_NAME : str = 'train.csv'
TEST_FILE_NAME : str = 'test.csv'

PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SCHEMA_FILE_PATH = os.path.join("config","schema.yaml")
SCHEMA_DROP_COLS = "drop_columns"

"""
Data Ingestion related constants starts with DATA_INGESTION
"""
DATA_INGESTION_COLLECTION_NAME : str = 'car'
DATA_INGESTION_DIR_NAME : str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR : str = 'feature_store'
DATA_INGESTION_INGESTED_DIR : str= 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION :float = 0.2

"""
Data Validation related constants starts with DATA_VALIDATION
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str ="validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"



"""
Data Tramsformation related constant start with DATA_TRANSFORMATION
"""

DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"


"""
Model Trainer related constant
"""
MODEL_TRAINER_DIR_NAME:str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str ="model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD:float = 0.05
