from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:

    trained_file_path: str
    test_file_path: str


# class DataIngestionArtifact:
#     def __init__(self,trained_file_path: str,test_file_path: str):
#         self.trained_file_path=trained_file_path
#         self.test_file_path=test_file_path

@dataclass
class DataValidationArtifact:
    validation_status : str
    valid_train_file_path:str
    valid_test_file_path:str
    invalid_train_file_path:str
    invalid_test_file_path:str
    drift_report_file_path:str


@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_apth: str
