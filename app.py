"""
@author: Viet Nguyen <nhviet1009@gmail.com>
"""
import os
import random
import string
from flask import Flask, request, render_template
import torch
import torch.nn.functional as F
import csv
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER = "flask_images"
rand_str = lambda n: "".join([random.choice(string.ascii_letters + string.digits) for _ in range(n)])

model = None
word2vec = None
max_length_sentences = 0
max_length_word = 0
num_classes = 0
categories = None


@app.route("/")
def home():
    return render_template("main.html")

@app.route("/input")
def new_input():
    return render_template("input.html")

@app.route("/show", methods=["POST"])
def show():
    global model, dictionary, max_length_word, max_length_sentences, num_classes, categories
    trained_model = request.files["model"]
    if torch.cuda.is_available():
        model = torch.load(trained_model)
    else:
        model = torch.load(trained_model, map_location=lambda storage, loc: storage)
    dictionary = pd.read_csv(filepath_or_buffer=request.files["word2vec"], header=None, sep=" ", quoting=csv.QUOTE_NONE,
                             usecols=[0]).values
    dictionary = [word[0] for word in dictionary]
    max_length_sentences = model.max_sent_length
    max_length_word = model.max_word_length
    num_classes = list(model.modules())[-1].out_features
    if "classes" in request.files:
        df = pd.read_csv(request.files["classes"], header=None)
        categories = [item[0] for item in df.values]
    return render_template("input.html")


@app.route("/result", methods=["POST"])
def result():
    global dictionary, model, max_length_sentences, max_length_word, categories
    text = request.form["message"]
    document_encode = [
        [dictionary.index(word) if word in dictionary else -1 for word in word_tokenize(text=sentences)] for sentences
        in sent_tokenize(text=text)]

    for sentences in document_encode:
        if len(sentences) < max_length_word:
            extended_words = [-1 for _ in range(max_length_word - len(sentences))]
            sentences.extend(extended_words)

    if len(document_encode) < max_length_sentences:
        extended_sentences = [[-1 for _ in range(max_length_word)] for _ in
                              range(max_length_sentences - len(document_encode))]
        document_encode.extend(extended_sentences)

    document_encode = [sentences[:max_length_word] for sentences in document_encode][
                      :max_length_sentences]

    document_encode = np.stack(arrays=document_encode, axis=0)
    document_encode += 1
    empty_array = np.zeros_like(document_encode, dtype=np.int64)
    input_array = np.stack([document_encode, empty_array], axis=0)
    feature = torch.from_numpy(input_array)
    if torch.cuda.is_available():
        feature = feature.cuda()
    model.eval()
    with torch.no_grad():
        model._init_hidden_state(2)
        prediction = model(feature)
    prediction = F.softmax(prediction)
    max_prob, max_prob_index = torch.max(prediction, dim=-1)
    prob = "{:.2f} %".format(float(max_prob[0])*100)
    if categories != None:
        category = categories[int(max_prob_index[0])]
    else:
        category = int(max_prob_index[0]) + 1
    return render_template("result.html", text=text, value=prob, index=category)


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(host="0.0.0.0", port=4555, debug=True)
