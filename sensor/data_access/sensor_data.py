from sensor.exception import SensorException
from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.constant.database import DATABASE_NAME
from sensor.logger import logging
from typing import Optional
import os,sys
import pandas as pd
import numpy as np


class SensorData:
    """
    This class hepls to import entire mongo db record as pandas data frame.
    """
    def __init__(self):
        try:
            self.mongo_client=MongoDBClient(database_name=DATABASE_NAME)
            print(f"mongo_client: {self.mongo_client}")
        except Exception as e:
            raise SensorException(e, sys)
    def export_collection_as_dataframe(self,collection_name:str,
                                         database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Export entire collection to dataframe:
        return pd.DataFrame of collection
        """
        try:
            if database_name is None:
                print("database name is empty.")
                collection = self.mongo_client.database[collection_name]
            else:
                print(f"database name is given: {database_name}")
                collection = self.mongo_client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            
            #to delete column named _df
            if "_id" in df.columns.to_list():
                df = df.drop(columns=['_id'], axis=1)
            
            # replace na with Nan
            df.replace({'na':np.nan},inplace = True)
            # logging.info(f"Data read completed from DataBase: {df.head()}")
            return df
            
        except Exception as e:
            raise SensorException(e, sys)
