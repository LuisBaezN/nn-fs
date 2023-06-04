# Neural network from scratch

This repo is based in the work of Samson Zhang. To get the data, you can download it [here](https://www.kaggle.com/datasets/oddrationale/mnist-in-csv), which is in csv format.

The data set has a total of 70,000 examples wich is divided in 60,000 samples to train and 10,000 samples to test. The neural network uses 1000 examples of the train dataset. 

If you want to transform the data to images of any partition use the script called csvtoimg.py. It takes two arguments, the first one must be train or test, and the second one must be the number of samples that you want to transform. If no argument is given, the script will take all the train data set.

## Attention

Further modifications will be added to take the model to a web app.