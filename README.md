# Sensor-Fault-Detection

In this branch the code is written in such a way that it can run in any docker machine or in docker play lab.

To try it follow the following steps:

step:-1. # Get ready with a system
```
open the terminal/instance/[docker playground](https://labs.play-with-docker.com/)
```

step:-2. # Clone the repo
```
git clone -b nero-lab https://github.com/manish7065/sensor_fault.git  
```

step:-3. # Select the downloaded directory 
```
cd sensor_fault 
```
step:-4. # built the docker image
```
docker build -t demo:lts . 
```
step:-5. # check the docker images
```
docker images
```
step:-6 # You can copy Image ID from the above command response and replace the mongodb url with your own. otherwise it will give you error at the time of model training
```
docker run -p 8080:8080 -e PORT=8080 -e MONGO_DB_URL="mongodb+srv://trialmongo:<pwd>@cluster0.2gugo3n.mongodb.net/test" <image_name>/<Image ID>
```
Now you can check the port 8080. A FastAPI backend interface will be there.
You can train the model here


## Problem Statement

This project aims to detect and predict faults in the Air Pressure System (APS) of a heavy-duty vehicle. By accurately identifying the faulty component of the APS, this project aims to reduce repair costs and time. The problem at hand is a binary classification task, in which the goal is to determine whether a failure was caused by a specific component of the APS or by some other factor.

## Solution:
The proposed solution for this project is to use machine learning techniques to accurately predict faults in the Air Pressure System (APS) of a heavy-duty vehicle. The datasets used for training and testing will have a positive class indicating component failures for a specific component of the APS, and a negative class indicating failures for components unrelated to the APS. The goal is to minimize false predictions in order to reduce repair costs.

## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions

#Architect Intro:

The data for this project has been ingested to mongo data base in JSON formet then it has been processed as per the project Architech to build the model. All the artifacts has been stored in S3 bucket.
Docker has been used to contanerised the preject and all the deployment steps are written in git workflow.
ECR has been used to build the docker and then it will be pulled in EC2 instance of AWS.
FastAPI has been used to provide the API interface to Train & predict the model.


## Data Collections
![image](https://user-images.githubusercontent.com/57321948/193536736-5ccff349-d1fb-486e-b920-02ad7974d089.png)


## Project Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536768-ae704adc-32d9-4c6c-b234-79c152f756c5.png)



## Steps to build the projec on local system

### Step 1: Clone the repository
```bash
git clone https://github.com/sethusaim/Sensor-Fault-Detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n sensor python=3.7.6 -y
```

```bash
conda activate sensor
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```


### Step 4 - Run the application server
```bash
python app.py
```

### Step 5. Train application
```bash
http://localhost:8080/train

```

### Step 6. Prediction application
```bash
http://localhost:8080/predict

```

## Build & Run Docker locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build -t <image_name> <path_to_Dockerfile>

```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```

To run the project  first execute the below commmand to set the env veriable.

windows user

```
MONGO_DB_URL=mongodb+srv: <your mongo-db url >
```

Linux/Mac user

```
export MONGO_DB_URL= <your mongo-db url >
```

then run 
```
python main.py
```

git config --global user.name manish
git config --global user.email manumi296@gmail.com