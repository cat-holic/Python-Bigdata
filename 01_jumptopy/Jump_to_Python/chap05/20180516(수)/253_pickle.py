import pickle

f = open("test.txt","wb")
data={1:'hello', 2:'bye'}
pickle.dump(data,f)
f.close()69999