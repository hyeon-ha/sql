import pickle

with open('./errors.pickle', 'rb') as f:
    data = pickle.load(f)
print(data)
a = "hello \"world\""
print(a)
