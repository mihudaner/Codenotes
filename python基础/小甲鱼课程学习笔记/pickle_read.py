import pickle

with open("data.pkl","rb") as f:
    x=pickle.load(f)#load 是按顺序的
    y=pickle.load(f)
    z=pickle.load(f)
    l=pickle.load(f)
print(x,y,z,l,sep="\n")

