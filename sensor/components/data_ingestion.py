from sensor.logger import logging
from sensor.exception import SensorException
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
from sensor.data_access.sensor_data import SensorData
import os,sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sensor.constant.training_pipeline import SCHEMA_FILE_PATH
from sensor.utils.main_utils import read_yaml_file

class DataIngestion:
    def __init__(self,data_ingestion_config=DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise SensorException(e, sys)

    def export_data_into_feature_store(self) -> DataFrame :
        """
        Export Mongo DB collection record into feature_store as Data Frame
        """
        try:
            logging.info(f"Exporting data from mongoDB to feature_store. ")

            sensor_data = SensorData()
            dataframe = sensor_data.export_collection_as_dataframe(
                                    collection_name=self.data_ingestion_config.collection_name)
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path

            #Create folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            
            return dataframe
        
        
        except Exception as e:
            raise SensorException(e, sys)

    def split_data_as_train_test(self,data_frame=DataFrame) -> None:
        """
        Split the feature_store dataset in train & test file
        data_frame: DataFrame which will besplited
        """
        try:
            train_set, test_set = train_test_split(data_frame,
                                    test_size=self.data_ingestion_config.train_test_split_ratio)

            print(f"train test split ratio = {self.data_ingestion_config.train_test_split_ratio}")
            # print(train_set.shape)
            # print(test_set.shape)


            logging.info(f"performed train test split on DataFrame")

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)

            logging.info(f"Creating the data ingestion directory to store the splited data at:{dir_path}")

            os.makedirs(dir_path,exist_ok=True)

            logging.info("Exporting train test data to the directory ")

            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )

            logging.info("Exported train and test file path.")

        except Exception as e:
            raise SensorException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            logging.info(f"{'<<'*10} Initiating the Data Ingestion. {'>>'*10}")
            dataframe = self.export_data_into_feature_store()
            dataframe = dataframe.drop(self._schema_config["drop_columns"],axis=1)
            self.split_data_as_train_test(data_frame=dataframe)

            data_ingestion_artifact=DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path)

            logging.info(f"Data ingestion Artifact sucessfully completed: {data_ingestion_artifact}")
            logging.info(f" {'<<'*10} Data ingestion completed sucessfully. {'>>'*10} \n")

            return data_ingestion_artifact
            
        except Exception as e:
            raise SensorException(e, sys)