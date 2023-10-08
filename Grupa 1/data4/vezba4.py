from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score

x = [[1],[2],[3],[4],[5],[6],[7],[8]]
y = [2,4,6,8,10,12,14,16]

trx, tstx, trry, tsty = train_test_split(x,y)

model = LinearRegression()
model.fit(trx,trry)

pred = model.predict(tstx)
print(pred)
print(tsty)


print(explained_variance_score(pred,tsty))


