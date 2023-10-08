from sklearn.svm import SVC

x = [[38,4],[35,8],[51,10],[20,10],[25,7]]
y = [1,0,1,0,0]
model = SVC()
model.fit(x,y)
pred = model.predict([[45,3]])
print(pred)