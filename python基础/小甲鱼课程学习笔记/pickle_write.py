import pickle

x,y,z=1,2,3
l=[5,6,3]
with open("data.pkl","wb") as f:
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(z,f)
    pickle.dump(l,f)