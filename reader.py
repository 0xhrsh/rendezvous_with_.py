import json
from pprint import pprint
f=open('data.json','r')
x=f.read()
#data =dict(accno=f.read(),pasw=f.read())
#with open('data.json') as f:
data = json.loads(x)
	#print(data)
	#pprint(data)
pprint(data)