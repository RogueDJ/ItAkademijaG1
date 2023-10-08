from sklearn.linear_model import LinearRegression

x = [[90,20],[100,24],[95,28],[80,15],[110,18],[120,22],[140,15]]
y = [120,140,130,110,150,180,220]
model = LinearRegression()
model.fit(x,y)

predvidjanje = model.predict([[85,28]])
print(predvidjanje)