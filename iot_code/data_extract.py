import pymongo
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = pymongo.MongoClient('mongodb://<user_id>:<password>@cluster0-shard-00-00-hiqkj.mongodb.net:27017,cluster0-shard-00-01-hiqkj.mongodb.net:27017,cluster0-shard-00-02-hiqkj.mongodb.net:27017/iot?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')
# database is iot 
db=client.iot

# chage directories of plate.txt, check.txt accordingly

file = open('/home/pi/Desktop/iot/piproject/plate.txt')
plate = file.read()
file.close()

#print(plate)


user = db.users.find_one({'noplate' : plate})
x = user['status']
email = user['email']
#print (x)
st=''
if(x == 1):
    st = 'OK'
    db.users.update_one({'email' : email}, {"$set" : {'status' : 0}})
else:
    print('No such vehicle id found')
    st = 'NO'
    
with open('/home/pi/Desktop/iot/piproject/check.txt', 'w') as f:
    f.write(str(st))
f.close()


#install 'pip install dnspython'
