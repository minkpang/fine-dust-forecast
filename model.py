import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits.mplot3d import Axes3D
import pymongo
from pymongo import MongoClient
import datetime
import pytz

def set_post(msg, data) :
  post = {
    "Station" : str(msg[0]),
    "Name" : str(msg[1]),
    "PM25": str(round(data[3],2)),
    "PM10": str(round(data[2],2)),
    "Humi": str(round(data[1],2)),
    "Temp": str(round(data[0],2)),
    "NOW":str(datetime.datetime.now(pytz.timezone('KST')))
  }
  return post

def fit_plane(x0, x1, t, y):
    c_tx0 = np.mean(t*x0)-np.mean(t)*np.mean(x0)
    c_tx1 = np.mean(t*x1)-np.mean(t)*np.mean(x1)
    c_x0x1 = np.mean(x0*x1) - np.mean(x0)*np.mean(x1)
    v_x0 = np.var(x0)
    v_x1 = np.var(x1)
    w0 = (c_tx1 * c_x0x1 - v_x1*c_tx0) / (c_x0x1**2 - v_x0 * v_x1)
    w1 = (c_tx0 * c_x0x1 - v_x0*c_tx1) / (c_x0x1**2 - v_x0 * v_x1)
    w2 = -w0 * np.mean(x0) - w1*np.mean(x1) + np.mean(t)
    w3 = -w0 * np.mean(x0) - w1*np.mean(x1) + np.mean(y)
    return np.array([w0, w1, w2, w3])

def Regresssion(msg, collection):
    trainData = pd.DataFrame(columns=['Temp','Humi','PM10','PM25'])
    temp = []
    humi = []
    pm10 = []
    pm25 = []

    data = collection.find({"Station":msg[0],"Name":msg[1]})

    for detail in data:
       # print(detail['Temp'],detail['Humi'],detail['PM10'])
        temp.append(float(detail['Temp']))
        humi.append(float(detail['Humi']))
        pm10.append(float(detail['PM10']))
        pm25.append(float(detail['PM25']))
    trainData['temperature'] = temp
    trainData['humidity']  = humi
    trainData['miwar_index']  = pm10
    trainData['miwar_super'] = pm25
    return set_post(msg,fit_plane(trainData['temperature'], trainData['humidity'], trainData['miwar_index'], trainData['miwar_super']))

if __name__ == '__main__' :
    try :
        connection = pymongo.MongoClient('mongodb://ec2-13-125-244-112.ap-northeast-2.compute.amazonaws.com:27017')
        db = connection['testmk']
        collection = db['Null']
    except :
        print("MongoDB Connection Error")
        sys.exit()
    else :
        print('MongoDB Connection Success')
    W = Regresssion(['s1','n1'],collection)
    print("wo={0:.1f}, w1={1:.1f}, w2={2:.1f}, w3={3:.1f}".format(W[0], W[1], W[2], W[3]))
