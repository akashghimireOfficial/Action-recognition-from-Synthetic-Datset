import os 
from glob import glob 
import tensorflow as tf 
from tensorflow.keras.layers import Layer,Dropout,Dense,BatchNormalization,Flatten
from tensorflow.keras.utils import to_categorical,plot_model
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from openpose import *
import cv2 as cv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


seed_constant = 50
np.random.seed(seed_constant)
random.seed(seed_constant)
tf.random.set_seed(seed_constant)

data_set_dire='UCF-101'
CLASSES_LIST = ["WalkingWithDog", "TaiChi", "Swing", "HorseRace"]
seq_len=20
#resized_height,resized_width=128,128
num_features=36

def get_features(video_dire):
    extracted_features=[]
    video_reader=cv.VideoCapture(video_dire)
    total_frames=int(video_reader.get(cv.CAP_PROP_FRAME_COUNT))
    skip_frames=max(int(total_frames/seq_len),1)
    for frame_counter in range(total_frames):
        video_reader.set(cv.CAP_PROP_POS_FRAMES,frame_counter*skip_frames)
        sucess,frame=video_reader.read()
        if not sucess:
            break
        #resized_frame=cv.resize(frame,(resized_width,resized_height))
        feature,_=get_features_df(e,frame)
        extracted_features.append(feature)
    extracted_features=np.array(extracted_features)
    return extracted_features


    
def create_dataset():
    labels=[]
    features=[]
    for idx,className in enumerate(CLASSES_LIST):
        video_dires_list=glob(os.path.join(data_set_dire,className)+"/*")
        for video_dire in video_dires_list:
            extracted_frames=get_features(video_dire)
            if len(extracted_frames)==20:
                print(1)
                get_features=feature_extractor_model.predict(extracted_frames)
                features.append(get_features)
                labels.append(idx)
                
    return features,labels