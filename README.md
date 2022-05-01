# Recommenders
various recommendation system POCs

## Folders

1. logs -> created by tensorflow for using tensorboard. 
2. mlruns -> created by mlflow for for tracking, model registry, and model serving. 

## Scripts

1_EDA ->
<br>2_create_feature_datasets 
<br>3_matrix_factorization 
<br />4_retrieval_raning -> train/test a retrieval and ranking based recommender using Tensorflow 
<br />5_example_API -> an basic api endpoint using flask app

## Helper Apps
1. tensorboard - to access tensorboard, go to the root of this project and run the following command in the terminal:  tensorboard --logdir logs/fit
2. MlFlow ui - To access MlFlow ui, go to the root of this project and run the following command in the terminal: mlflow ui 
3. Flask - to get api running, go to the root of this project and run ...
