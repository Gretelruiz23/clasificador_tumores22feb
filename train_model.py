import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, regularizers
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

#cargar el dataset

data = load_breast_cancer()
x,y=data.data, data.target

print(x)