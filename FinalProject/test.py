import pickle
model = pickle.load(open('modelNewData.pkl','rb'))

test = pickle.load(open('modelNewData.pkl','rb'))
prediction = test.predict([[2.3,25,1111,0,0,0,0,0,0,1,0]])

print(prediction)