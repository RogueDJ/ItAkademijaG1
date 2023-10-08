from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,accuracy_score

x = [[3],[4],[2],[5],[3],[6],[8]]
y = [1,1,0,1,1,1,1]

model = SVC()
model.fit(x,y)

pred = model.predict(x)
print(pred)

print(confusion_matrix(pred,y))
print(accuracy_score(pred,y))

