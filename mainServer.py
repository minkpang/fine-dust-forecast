from socket import *
import pymongo
import json
import thread
from model import Regresssion

PORT = 8080

try :
    connection = pymongo.MongoClient('mongodb://ec2-13-125-244-112.ap-northeast-2.compute.amazonaws.com:27017')
    db = connection['testmk']
    collection = db['Null']
except :
    print("MongoDB Connection Error")
    sys.exit()
else :
    print('MongoDB Connection Success')

def classificationOrd(user, addr) :
    while True :
        try :
            msg = user.recv(1024)
            msg = json.loads(msg.decode('utf-8'))
            ord = msg[0]
            data = msg[1:]
            if ord == '8080' :
                insert_post(data)
            else :
                linnearRegresssion(data, user)
        except Exception as e:
            break

def linnearRegresssion(data,user) :
    try :
        val = Regresssion(data,collection)
        user.sendall(json.dumps(val).encode('utf-8'))
        insert_post(val)
    except Exception as e:
        break
#Database name='test' & Collection name='Null'
#Insert document
def insert_post(value) :
    collection.insert(value)

if __name__ == '__main__' :
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('',PORT))
    server.listen(1000)
    print('Waiting Connect')
    while True :
        user, addr = server.accept()
        try :
            thread.start_new_thread(classificationOrd,(user,addr))
        except Exception as e :
            print('out : ', e)
            break
    print('Server closed')
