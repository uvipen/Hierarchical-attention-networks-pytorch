# [PYTORCH] Hierarchical Attention Networks for Document Classification

## Introduction

Here is my pytorch implementation of the model described in the paper **Hierarchical Attention Networks for Document Classification** [paper](https://www.cs.cmu.edu/%7Ediyiy/docs/naacl16.pdf). 

<p align="center">
  <img src="demo/video.gif"><br/>
  <i>An example of app demo for my model's output for Dbpedia dataset.</i>
</p>

<p align="center">
  <img src="demo/output.gif"><br/>
  <i>An example of my model's performance for Dbpedia dataset.</i>
</p>

## How to use my code

With my code, you can:
* **Train your model with any dataset**
* **Given either my trained model or yours, you could evaluate any test dataset whose have the same set of classes**
* **Run a simple web app for testing purpose**

## Requirements:

* **python 3.6**
* **pytorch 0.4**
* **tensorboard**
* **tensorboardX** (This library could be skipped if you do not use SummaryWriter)
* **numpy**

## Datasets:

Statistics of datasets I used for experiments. These datasets could be download from [link](https://drive.google.com/drive/u/0/folders/0Bz8a_Dbh9Qhbfll6bVpmNUtUcFdjYmF2SEpmZUZUcVNiMUw1TWN6RDV3a0JHT3kxLVhVR2M)

| Dataset                | Classes | Train samples | Test samples |
|------------------------|:---------:|:---------------:|:--------------:|
| AG’s News              |    4    |    120 000    |     7 600    |
| Sogou News             |    5    |    450 000    |    60 000    |
| DBPedia                |    14   |    560 000    |    70 000    |
| Yelp Review Polarity   |    2    |    560 000    |    38 000    |
| Yelp Review Full       |    5    |    650 000    |    50 000    |
| Yahoo! Answers         |    10   |   1 400 000   |    60 000    |
| Amazon Review Full     |    5    |   3 000 000   |    650 000   |
| Amazon Review Polarity |    2    |   3 600 000   |    400 000   |

Additionally, I also use word2vec pre-trained models, taken from GLOVE, which you could download from [link](https://nlp.stanford.edu/projects/glove/). I run experiments with all 4 word2vec files (50d, 100d, 200d and 300d). You could easily switch to other common word2vec models, like the one provided in FastText [link](https://fasttext.cc/docs/en/crawl-vectors.html) 
In the paper, it is said that a pre-trained word2vec is used. However, to the best of my knowledge, at least in pytorch, there is no implementation on github using it. In all HAN github repositories I have seen so far, a default embedding layer
was used, without loading pre-trained word2vec model. I admit that we could still train HAN model without any pre-trained word2vec model. However, to serve the purpose of re-implementing origin model, in all experiments, as mentioned above, I used 1 out of 4 pre-trained word2vec models as initilization for embedding layer.

## Setting:

During my experiments, I found out that given different datasets and different embedding layer's dimension, some combinations of batch size and learning rate yield better performance (faster convergence and higher accuracy) than others. Particularly in some cases, if you set wrong values for these 2 very important parameters, your model will never converge. Detail setting for each experiments will be shown in **Experiments** part.
I have not set a fixed number of epoches for each experiment. Instead, I apply early stopping technique, to stop training phase after test loss has not been improved for **n** epoches. 

## Training

If you want to train a model with default parameters, you could run:
- **python train.py**

If you want to train a model with your preference parameters, like optimizer and learning rate, you could run:
- **python train.py --batch_size batch_size --lr learning_rate**: For example, python train.py --batch_size 512 --lr 0.01

If you want to train a model with your preference word2vec model, you could run:
- **python train.py --word2vec_path path/to/your/word2vec**

## Test

For testing a trained model with your test file, please run the following command:
- **python test.py --word2vec_path path/to/your/word2vec**, with the word2vec file is the same as the one you use in training phase.

You could find some trained models I have trained in [link](https://drive.google.com/open?id=1A50PDQMm0THnU6QDxOEsvKqH-ZTxmGpT)

## Experiments:

Results for test set are presented as follows:  A(B/C):
- **A** is accuracy.
- **B** is learning rate used.
- **C** is batch size.

Each experiment is run over 10 epochs.

| GLOVE word2vec|        50      |      100     |      200     |      300     |
|:---------------:|:------------------:|:------------------:|:------------------:|:------------------:|
|    ag_news    |   updated soon   |   updated soon   |   updated soon   |   updated soon   |
|   sogu_news   |   updated soon   |   updated soon   |   updated soon   |   updated soon   |
|    db_pedia   |   updated soon   |   updated soon   |   updated soon   |   updated soon   |
| yelp_polarity |   updated soon   |   updated soon   |   updated soon   |   updated soon   |
|  yelp_review  |   updated soon   |   updated soon   |   updated soon   |   updated soon   |
|  yahoo_answer |   updated soon   |   updated soon   |   updated soon   |   updated soon   |
| amazon_review |   updated soon   |   updated soon   |   updated soon   |   updated soon   |
|amazon_polarity|   updated soon   |   updated soon   |   updated soon   |   updated soon   |

The training/test loss/accuracy curves for each dataset's experiments (with the order from left to right, top to bottom is 50d, 100d, 200d and 300d word2vec) are shown below:

- **ag_news**

<img src="demo/agnews_50.png" width="420"> <img src="demo/agnews_100.png" width="420"> 
<img src="demo/agnews_200.png" width="420"> <img src="demo/agnews_300.png" width="420">

- **db_pedia**

<img src="demo/dbpedia_50.png" width="420"> <img src="demo/dbpedia_100.png" width="420"> 
<img src="demo/dbpedia_200.png" width="420"> <img src="demo/dbpedia_300.png" width="420">

- **yelp_polarity**

<img src="demo/yelpreviewpolarity_50.png" width="420"> <img src="demo/yelpreviewpolarity_100.png" width="420"> 
<img src="demo/yelpreviewpolarity_200.png" width="420"> <img src="demo/empty.png" width="420">

- **yelp_review**

<img src="demo/yelpreviewfull_50.png" width="420"> <img src="demo/empty.png" width="420"> 
<img src="demo/empty.png" width="420"> <img src="demo/yelpreviewfull_300.png" width="420">

- **Yahoo! Answers**

<img src="demo/yahoo_50.png" width="420"> <img src="demo/yahoo_100.png" width="420"> 
<img src="demo/yahoo_200.png" width="420"> <img src="demo/yahoo_300.png" width="420">

- **amazon_review**

<img src="demo/amazonreviewfull_50.png" width="420"> <img src="demo/empty.png" width="420"> 
<img src="demo/amazonreviewfull_200.png" width="420"> <img src="demo/empty.png" width="420">

- **amazon_polarity**

<img src="demo/amazonreviewpolarity_50.png" width="420"> <img src="demo/amazonreviewpolarity_100.png" width="420"> 
<img src="demo/empty.png" width="420"> <img src="demo/amazonreviewpolarity_50.png" width="420">

There are some experiments I have not had time to train. For such experiments, statistics as well as loss/accuracy visualization are empty. Additionally, there are some other experiments, I can not wait until they are finished, hence I stopped training phase before it should be . You could see whether a model was stopped by early stopping technique or by me by looking at the test loss curve, if the loss is not improved for 5 consecutive epoches, it is the former case. Othewise, if the loss is still going down, it is the latter case. When I have time, I will complete the incomplete experiments, and update results here.

After completing training phase, you could see model's parameters you have set, accuracy, loss and confusion matrix for test set at the end of each epoch at **root_folder/trained_models/logs.txt**. One example is shown below:

<p align="center">
  <img src="demo/output.png"><br/>
  <i>An example of logs.txt for Dbpedia dataset.</i>
</p>

## Demo:

I wrote a simple web which is suitable for quick test with any input text. In order to use the app, you could follow the following steps:

- **Step 1**: Run the script app.py
<img src="demo/1.png" width="800">

- **Step 2**: Web interface
<img src="demo/2.png" width="800">

- **Step 3**: Select trained model
<img src="demo/3.png" width="800">

- **Step 4**: Select word2vec model
<img src="demo/4.png" width="800">

- **Step 5 (Optional)**: Select file containing classes (one class per line)
<img src="demo/5.png" width="800">

- **Step 6**: After all necessary files are selected, press submit button
<img src="demo/6.png" width="800">

- **Step 7**: You could paste any text to the textbox
<img src="demo/7.png" width="800">

- **Step 8**: A sample text
<img src="demo/8.png" width="800">

- **Step 9**: After submit button pressed, predicted category and probability are shown
<img src="demo/9.png" width="800">
