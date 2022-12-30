from sensor.exception import SensorException
from sensor.logger import logging

import os,sys

class TargetValueMapping:
    def __init__(self):
        self.neg:int = 0
        self.pos:int = 1

    def to_dict(self):
        return self.__dict__

    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))


# Write a code to train model and check the accuracy

class SensorModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise SensorException(e, sys)


    def predict(self):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise SensorException(e, sys)


class ModelResolver:
    def __init__(self,model_dir):
        try:
            pass
        except Exception as e:
            