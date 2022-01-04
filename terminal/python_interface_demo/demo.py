import pickle

# array = ['kaan', 'beyda']

fileread = open('c:/users/hkizildag/desktop/array', 'rb')

# filewrite = open('c:/users/hkizildag/desktop/array', 'wb')
# pickle.dump(array, filewrite)


array = pickle.load(fileread)

print(array)
