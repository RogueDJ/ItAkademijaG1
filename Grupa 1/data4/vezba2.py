from sklearn.linear_model import LogisticRegression

x = [[4],[7],[2],[1],[0],[2],[3],[5],[1]]
y = [1,1,0,0,0,0,0,1,0]

model = LogisticRegression()
model.fit(x,y)

ulaz = [[5]]
pred =  model.predict(ulaz)
print(pred)