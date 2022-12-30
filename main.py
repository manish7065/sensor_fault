# from sensor.configuration.mongodb_connection import MongoDBClient
# from sensor.exception import SensorException
from sensor.pipeline.training_pipeline import TrainPipeline
import os,sys



if __name__ == "__main__":

    trainig_pipeline = TrainPipeline()
    trainig_pipeline.run_pipeline()




