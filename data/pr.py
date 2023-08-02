import pickle
import pprint

file=open("./val.pkl","rb")
data=pickle.load(file)
print(data)
file.close()
