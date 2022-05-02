# Recommenders
The objective of this project was to:
1. create Python notebook which imports the data and trains a simple recommendation algorithm.
2. create a brief slide deck or memo which explains how the model was developed and presents a high-level design for integrating the recommendations into the business.

Key questions to answer include:
1. How does the model leverage the raw event data to provide the content recommendations?
2. How would you update the production model and/or recommendations over time?
3. How would you design the interface between the app and the recommendation engine (e.g. what are the inputs/outputs to an API)?
4. What resources would you leverage to support the recommendation engine? What are the advantages and disadvantages of your choices?
5. What details would you need to know about the app platform, activity patterns, or
other relevant details of the project to refine your design?

The slide deck can be found here -> [Slide Deck: Recommender System POC](https://docs.google.com/presentation/d/125fHNkl2iV7J0MNec3c1JziTNHdGIiupGeZDp3NKnoo/edit#slide=id.p)

To build a recommendation algorithm for this project, I broke apart the EDA, intermediate dataset creation, and training/testing work into different scripts (see the 'scripts' section of read me). Two different modeling approaches were examined: matrix factorization using SVD and a retrieval/ranking implementation using tensorflow/keras. In addition to the algorithm, I built a flask app to serve the model as a basic API. There are also various helper apps to help with model examination and experiement tracking. Details on these are in the 'helper app' section of this read me.

To use the retrieval/ranking model API:
1. start the flask app (see directions below. if using a virtual environment, package installation takes ~10 minutes) 
2. once the app is running, go to the 5_use_api notebook and run code there. The input into the api is {'user_id': 'abcd1234'} which returns a order dictionary of {content_1:score, content_2:score} ordered with the highest score and best recommendation first.


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

## Folders

1. logs -> created by tensorflow for using tensorboard. 
2. mlruns -> created by mlflow for for tracking, model registry, and model serving.
3. retrieval_model -> holds the model artifact
4. ranking_model -> holds the model artifact 


## Note
I’m not a “solve everything with deep learning” person. Generally I thin its important to balance performance with complexity - often deep learning introduces significant complexity without much additional performance. But recommenders seems to be an area - like computer vision - that neural nets perform much better. Because of this, I wanted to demonstrate some of the innovation in this area and show what is possible. 
