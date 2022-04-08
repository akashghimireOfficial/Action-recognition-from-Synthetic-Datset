# **Action-recognition-from-Synthetic-Datset**

## ***System Information Used for training and testing***
1. **GPU** : RTX 3070 Mobile Version
2. **CPU** : AMD Ryzen 9 5000 series (8 Cores)
3. **Memory** : 24 GB 3200 MHz




## *Purpose*
1. Use synthetic dataset for training Action Recognition and get good accuracy
2. Evaluate how will it perform on Real test Dataset



## ***Dataset Used***
> [Eldersim Synthetic Datas] (https://ai4robot.github.io/ElderSim/) \
> Total 55 classes of Action Recognition \
> Synthetic Dataset was produced using ***etri-dataset***
>>[***etri-dataset***] (https://ai4robot.github.io/ElderSim/)

A big thank you to **@sard0r** for providing these dataset. 


## **Pose estmation using tf pose**
1. to use this repo first install [**tf_pose**] (https://github.com/gsethi2409/tf-pose-estimation) in the same folder.
2. Original CMU weight of openpose was used as weights for tf pose for extracting 

## **Model Architecture**
![model Architecture](https://github.com/akashghimireOfficial/Action-recognition-from-Synthetic-Datset/blob/main/more%20information/model_architecture.png)
## ***Result***
i. ***Training Result***
  1. > Training Accuracy :98.09 % 
  2. > Valiation Accuracy : 96.46%

ii. ***Testing Result***
  1. On synthetic Dataset : 98.41 %
  2. On Non-synthetic Dataset : **yet to be tested**
