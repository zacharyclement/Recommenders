# Recommenders
To use the recommendation system built for this project:
1. start the flask app (see directions below. if using a virtual environment, package installation takes 10-15 minutes) 
2. once the app is running, go to the 5_use_api notebook and run code there.

Besides the working api, there are various script for eda, feature engineering, and modeling. Details are provided in the script section

There are also various helper apps to help with model examination and experiement tracking. Details on these are in the helper app section.

## Folders

1. logs -> created by tensorflow for using tensorboard. 
2. mlruns -> created by mlflow for for tracking, model registry, and model serving.
3. retrieval_model -> holds the model artifact
4. ranking_model -> holds the model artifact 

## Scripts

* 1_EDA -> exploratory data analysis on raw data
* 2_create_feature_datasets  -> builds csv files for data with features
* 3_matrix_factorization_svd -> implementation with train/test of matrix factorization with singular value decomposition using suprise library
* 4_retrieval_ranking -> train/test a retrieval and ranking based recommender using Tensorflow 
* 5_use_api -> an basic api endpoint using flask app

## Helper Apps
1. tensorboard - to access tensorboard, go to the root of this project and run the following command in the terminal:<br/>  $ tensorboard --logdir logs/fit
2. MlFlow ui - To access MlFlow ui, go to the root of this project and run the following command in the terminal:<br/> $ mlflow ui 
3. Flask - to get api running, go to the root of this project and run: <br/>
$ conda create -n api_env python=3.7 <br/>
$ conda activate api_env <br/>
$ pip install tensorflow flask flask-bootstrap requests <br/>
$ export FLASK_APP=api <br/>
$ flask run -h localhost -p 3000 <br/>
