import pickle

f=open("test.txt","rb")
data=pickle.load(f)
print(data)