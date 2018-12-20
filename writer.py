# data writer
import json
f = open('data.json','a')
print("enter number of data to be added")
n=input()
#print("n")
#n=10
i=0
while i<int(n):
	print("Enter Accno and Pasw respectively")
	x =dict(accno=input(),pasw=input())
	json.dumps(x)
	#pprint(json.dumps(x))
	i+=1