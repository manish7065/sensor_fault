from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from sensor.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact,DataTransformationArtifact
from sensor.logger import logging
from sensor.exception import SensorException
from sensor.components.data_ingestion import DataIngestion
from sensor.components.data_validation import DataValidation
from sensor.components.data_transformation import DataTransformation

import os,sys


class TrainPipeline:
    is_pipeline_running = False
    def __init__(self):
        self.training_pipeline_config=TrainingPipelineConfig()




    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("starting data ingestion. ")
            self.data_ingestion_config = DataIngestionConfig(
                                        training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"data insgestion completed at artifact: {data_ingestion_artifact} ")

            return data_ingestion_artifact

        except Exception as e:
            raise SensorException(e, sys)

    # def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
    #     try:
    #         data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
    #         data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
    #         data_validation_config = data_validation_config
    #         )
    #         data_validation_artifact = data_validation.initiate_data_validation()
    #         return data_validation_artifact
    #     except  Exception as e:
    #         raise  SensorException(e,sys)

    def start_data_validation(self,data_ingestion_artifact=DataIngestionArtifact)->DataValidationArtifact:
        try:
            logging.info(f"Data valiodation starts")
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            # logging.info(f"Data valiodation config completed sucessfully: {data_validation_config}")
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                            data_validation_config=data_validation_config)
            # logging.info(f"data validation completed.")                               
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact
            logging.info(f"Data valiodation completed")

        except Exception as e:
            raise SensorException(e, sys)from e

    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact)->DataTransformationArtifact:
        try:
            logging.info("Start Data Transformation")
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(
                data_validation_artifact = data_validation_artifact, 
                data_transformation_config = data_transformation_config)

            data_transformation_artifact = data_transformation.initiate_data_transformation()

            return data_transformation_artifact
        except Exception as e:
            raise SensorException(e, sys)
            
            

    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise SensorException(e, sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact:DataIngestionArtifact=self.start_data_ingestion()
            data_validation_artifact:DataValidationArtifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact:DataTransformationArtifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
        except Exception as e:
            raise SensorException(e, sys)