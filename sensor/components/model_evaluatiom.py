

class ModelEvaluation:

    def __init__(self,model_evaluation_config:ModelEvaluationConfig,
                data_validation_artifact:DataValidationArtifact,
                model_trainer_artifact:ModelTrainerArtifact):
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)

