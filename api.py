from flask import Flask, request, make_response, jsonify
import tensorflow as tf
import os
import numpy as np

app = Flask(__name__)

@app.route("/recommender", methods=['POST'])
def get_recommendations():

    event_data = request.json
    USER_ID = event_data['user_id']
    print('USER_ID: ', event_data)

    # get retrieval model. Pass a user id in, get top predicted movie titles back.
    cwd = os.getcwd()
    retrieval_path = os.path.join(cwd, "retrieval_model")
    loaded_retrieval = tf.saved_model.load(retrieval_path)
    _ , content_ids_recommended = loaded_retrieval([USER_ID])

    # Handoff from retrieval to ranking. Load model and get ranking for each conent_id
    ranking_path = os.path.join(cwd, "ranking_model")
    loaded_ranking = tf.saved_model.load(ranking_path)

    final_ratings = {}
    content_ids_from_retrieval = content_ids_recommended[0]

    for content_id in content_ids_from_retrieval:
        content_id = content_id.numpy()
        final_ratings[content_id] = loaded_ranking(
            {"user_id": np.array([f"{USER_ID}"]), "content_id": np.array([content_id])}
        )

    # sort and prepare object to return
    api_return = {}
    for content_id, score in sorted(
        final_ratings.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"{content_id}: {score}")
        api_return[f'{content_id}'] = score.numpy()[0][0]

    return jsonify(str(api_return))

@app.route("/")
def home():
    return "<p>Use Provided Script to See Recommendations. See https://github.com/zacharyclement/Recommenders</p>"


if __name__ == '__main__':
    app.run(debug=True)
