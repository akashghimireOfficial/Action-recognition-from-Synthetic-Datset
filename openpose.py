import os 
import sys
sys.path.insert(0,"tf_pose_estimation")

import argparse
import logging
import time
import cv2
import numpy as np
from tf_pose_estimation.tf_pose.estimator import TfPoseEstimator
from tf_pose_estimation.tf_pose.networks import get_graph_path, model_wh
from pandas import DataFrame

w,h=432,368

model_dire='cmu'

e = TfPoseEstimator(get_graph_path(model_dire), target_size=(w, h))
 
 
 
def get_features_df(model,img_clone,upsample_size=4.0):
    humans = e.inference(img_clone, resize_to_default=(w > 0 and h > 0), upsample_size=4.0)
    skeletons = [[0.0,0.0,.0]]*18
    scale_h=4.0
    for human in humans:
        index=0
        for i, body_part in human.body_parts.items():# iterate dict
            idx=body_part.part_idx
            x=body_part.x
            y=body_part.y
            p=body_part.score
            skeletons[idx]=[x,y,p]
        
     
    
    df=DataFrame(skeletons,columns=['x','y','confidence'])
    return np.array(skeletons)[:,:2].flatten(),df



