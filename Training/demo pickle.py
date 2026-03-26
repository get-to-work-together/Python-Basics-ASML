import pickle

d = {'A':[1,2,3,4], 'B':[5,6,7,8], 'C':{'x':[9,10], 'y':[11,12]}}

print(d)

with open('data.pkl', 'wb') as f:
    pickle.dump(d, f)

del d

with open('data.pkl', 'rb') as f:
    stored_d = pickle.load(f)

print(stored_d)
