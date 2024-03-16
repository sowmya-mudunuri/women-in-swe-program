import os
import glob
import pathlib
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import regularizers, backend
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.callbacks import EarlyStopping, LearningRateScheduler, ModelCheckpoint
from tensorflow.keras.layers import Dense, MaxPooling2D, Flatten, Conv2D, Dropout, BatchNormalization
from tensorflow.keras.applications.vgg16 import VGG16
DIR_BASE = ("C:/Users/Sowmya Mudunuri/Downloads/archive")
DIR_TRAIN = os.path.join(DIR_BASE, 'train')
DIR_VALID = os.path.join(DIR_BASE, 'valid')
DIR_TEST = os.path.join(DIR_BASE, 'test')
def process(data):

    """
    Takes the directory as input and returns a panda DataFrame that contains our classe's labels.
    """
    path=pathlib.Path(data) # Converting String data to a Path data
    filepaths=list(path.glob(r"*/*.jpg"))
    labels=list(map(lambda x: os.path.split(os.path.split(x)[0])[1],filepaths)) # Separating labels from filepaths and storing it
    df1=pd.Series(filepaths,name='filepaths').astype(str)
    df2=pd.Series(labels,name='labels')
    df=pd.concat([df1,df2],axis=1) # Building the Dataframe
    return df
df_train=process(DIR_TRAIN)
df_valid=process(DIR_VALID)
df_test=process(DIR_TEST)
df_train.head()
filepath = pathlib.Path("C:/Users/Sowmya Mudunuri/Downloads/archive/birds.csv")
filepath.parent.mkdir(parents=True, exist_ok=True)
df_train.to_csv(filepath)
def calc_labels(dir):
    cnts, labels = {}, []
    for label in sorted(os.listdir(f'{dir}')):
        labels.append(label)
        cnts[label] = len(os.listdir(f'{dir}/{label}/'))
    return cnts, labels

def plot_classes_graph(dir):

    """
    takes the directory as input and displays a graph representing the number of images per bird's class in a directory.
    """

    labels_count = calc_labels(dir)[0]
    x, y = zip(*sorted(labels_count.items(), key = lambda e: e[0]))
    plt.figure(figsize=(25,5))
    plt.title('Nombre d\' images par classe d\'oiseaux dans le dossier train')
    plt.xlabel('Classe d\'oiseaux')
    plt.ylabel('Nombre d\'images')
    plt.plot(x, y, linewidth=1.5, label='Nombre d\' images par classe d\'oiseaux')
    plt.xticks(x, rotation=90)
    plt.legend(loc='upper right')
    plt.grid(alpha=0.5)
    plt.show()
plt.style.use('fivethirtyeight')
plot_classes_graph(DIR_TRAIN)
plt.style.use('default')

def plot_random_image_from_directory(target_dir):

    """
    takes the directory as input and displays 6 random images from the targeted directory.
    """

    target_dir=target_dir.sample(frac=1).reset_index(drop=True)
    fig,axes=plt.subplots(nrows=2,ncols=3,figsize=(10, 10))

    for i,ax in enumerate(axes.flat):
        x=plt.imread(target_dir['filepaths'][i])
        ax.imshow(x)
        ax.set_title(target_dir['labels'][i])
        ax.axis(False)
    plt.tight_layout()
    plt.show()

plot_random_image_from_directory(df_train)
generator = ImageDataGenerator()
train_ds=generator.flow_from_dataframe(
    dataframe=df_train,
    x_col='filepaths',
    y_col='labels',
    target_size=(224,224),
    batch_size=64,
    subset='training',
    random_seed=42)

valid_ds=generator.flow_from_dataframe(
    dataframe=df_valid,
    x_col='filepaths',
    y_col='labels',
    target_size=(224,224),
    batch_size=32,
    subset='training')

test_ds = generator.flow_from_dataframe(
    dataframe=df_test,
    x_col='filepaths',
    y_col='labels',
    target_size=(224,224),
    batch_size=32)

classes = list(train_ds.class_indices.keys())
classes
model = Sequential()

# Bloc 1
model.add(Conv2D(16, kernel_size = (3,3), padding = 'same', activation = 'relu', input_shape = (224,224,3)))
model.add(Conv2D(32, kernel_size = (3,3), padding = 'same', activation = 'relu'))
model.add(MaxPooling2D(pool_size = (3,3)))

# Bloc 2
model.add(Conv2D(32, kernel_size = (3,3), padding = 'same', activation = 'relu'))
model.add(Conv2D(64, kernel_size = (3,3), padding = 'same', activation = 'relu'))
model.add(MaxPooling2D(pool_size = (3,3)))

# Bloc 3
model.add(Conv2D(128, kernel_size = (3,3), padding = 'same', activation = 'relu'))
model.add(Conv2D(256, kernel_size = (3,3), padding = 'same', activation = 'relu'))
model.add(MaxPooling2D(pool_size = (3,3)))
model.add(BatchNormalization())

# Bloc 4
model.add(Flatten())
model.add(Dropout(0.3))
model.add(Dense(256, activation = 'relu', kernel_regularizer = regularizers.l2(0.001)))
model.add(Dense(100, activation = 'softmax'))

model.summary()
filepath = "C:/Users/Sowmya Mudunuri/Downloads/archive/EfficientNetB0-525-(224 X 224)- 98.97.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')
early_stopping_monitor = EarlyStopping(monitor = 'val_accuracy', patience = 3, restore_best_weights = True)

callbacks_list = [checkpoint, early_stopping_monitor]
cost_function = keras.losses.categorical_crossentropy
model.compile(loss = keras.losses.categorical_crossentropy, optimizer = 'adam', metrics = ["accuracy"])
history = model.fit(train_ds,epochs=40, verbose=1, validation_data = valid_ds, batch_size=32, callbacks=[callbacks_list])
model.evaluate(test_ds,use_multiprocessing=True,workers=10)
model.save('C:/Users/Sowmya Mudunuri/Downloads/archive/EfficientNetB0-525-(224 X 224)- 98.97.h5')
def plot_acc(history):

  acc = history.history['accuracy']
  val_acc = history.history['val_accuracy']
  epochs = range(len(acc))

  # Plot: accuracy vs epoch
  plt.figure(figsize=(15,3))
  plt.plot(epochs, acc,label='Training accuracy', linewidth=1.5)
  plt.plot(epochs, val_acc, 'r', label='Validation accuracy', linewidth=1.5)
  plt.title('Training accuracy')
  plt.xlabel('Epochs')
  plt.ylabel('Accuracy')
  plt.legend(loc='lower right')
  plt.figure()
  plt.show()
def plot_loss(history):

  loss = history.history['loss']
  val_loss = history.history['val_loss']
  epochs = range(len(loss))

  # Plot: loss values vs epoch
  plt.figure(figsize=(15,3))
  plt.plot(epochs, loss,label='Training loss', linewidth=1.5)
  plt.plot(epochs, val_loss, 'r', label='Validation loss', linewidth=1.5)
  plt.title('Training loss')
  plt.xlabel('Epochs')
  plt.ylabel('Loss')
  plt.legend(loc='upper right')
  plt.figure()
  plt.show()
plt.style.use('fivethirtyeight')
plot_acc(history)
plot_loss(history)
plt.style.use('default')
