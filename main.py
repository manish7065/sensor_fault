# from sensor.configuration.mongodb_connection import MongoDBClient
# from sensor.exception import SensorException
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import read_yaml_file
from sensor.constant.application import APP_HOST,APP_PORT
from sensor.exception import SensorException
import os,sys


from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from uvicorn import run as app_run


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainPipeline()
        if train_pipeline.is_pipeline_running:
            return Response("Training Pipeline is already running.")
        train_pipeline.run_pipeline()
        return Response("Training Sucessfull.")
    except Exception as e:
        return Response(f"Error Occured! {e}")


@app.get("/predict")
async def predict_route():
    try:
        #get data from user csv file
        #convert csv file to data frame

        df=None
        model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not model_resolver.is_model_exists():
            return Response("Model is not Available.Please Train first.")

        best_model_path = model_resolver.get_best_model_path()
        model = load_object(file_path=best_model_path)
        y_pred = model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping(), inplace=True)

        # Return the file to user as you wish

    except Exception as e:
        raise Response(f"Error Occured! {e}")

env_file_path = os.path.join(os.getcwd(),"env.yaml")

def set_env_variable(env_file_path):
    if os.getenv('MONGO_DB_URL',None) is None:
        env_config = read_yaml_file(env_file_path)
        os.environ['MONGO_DB_URL']=env_config['MONGO_DB_URL']

def main():
    try:
        set_env_variable(env_file_path)
        trainig_pipeline = TrainPipeline()
        trainig_pipeline.run_pipeline()

    except Exception as e:
        raise SensorException(e, sys)
        # logging.info(e)


if __name__ == "__main__":
    try:
        app_run(app, host=APP_HOST, port=APP_PORT)
    except Exception as e:
        raise SensorException(e, sys)

    # trainig_pipeline = TrainPipeline()
    # trainig_pipeline.run_pipeline()




