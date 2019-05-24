# now lets get straight to it (that's what she said)
import matplotlib.pyplot as plot
import numpy as np
from pprint import pprint
n=1000
theta=np.linspace(0,n,n,endpoint=True)
plot.title('Loss function over iterations')
plot.xlabel('Iterations')
plot.ylabel('Loss')
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.ylim(0, 100)
Loss=[]


def sigmoid(x):
	return 1.0/(1+np.exp(-x))
def sigmoid_derivative(x):
	return x*(1.0-x)

class Heras:
	
	def __init__(self,X,Y,n,m):
		self.input=X
		self.weights1=np.random.rand(self.input.shape[1],n)
		# here n and m are number of neurons in the present layer
		# and m is the number of desired neurons in the next layer
		#m=1 #lets begin with the easiest case
		self.weights2=np.random.rand(n,m)
		self.Y=Y
		self.output=np.zeros(self.Y.shape)
	def loss(self):
		#print(((Y-self.output)**2).sum())
		return ((Y-self.output)**2).sum()/n

	def FeedForward(self):
		# now in this alpha version I'm taking the activation function
		# to be sigmoid ex pos facto
		self.layer1=sigmoid(np.dot(self.input,self.weights1))
		self.output=sigmoid(np.dot(self.layer1,self.weights2))

	def BackProp(self):
		# i'm not gonna lie, it's gonna get ugly here
 		derivative_w2=np.dot(self.layer1.T,(2*(self.Y-self.output)*sigmoid_derivative(self.output)))
 		derivative_w1=np.dot(self.input.T,(np.dot(2*(self.Y-self.output)*sigmoid_derivative(self.output),self.weights2.T)*sigmoid_derivative(self.layer1)))
 		# updating the weights here
 		self.weights1+=derivative_w1
 		self.weights2+=derivative_w2

if __name__ =="__main__":
	dataset=np.loadtxt("data.csv",delimiter=',')
	X=np.array(dataset[:,0:8])
	Y=np.array(dataset[:,8])
	#print(X.shape,Y.shape)
	nn=Heras(X,Y,30,768)

	for i in range(n):
		nn.FeedForward()
		nn.BackProp()
		Loss.append(nn.loss())
		print(nn.loss())

	#pprint(nn.output)
	plot.plot(theta,Loss)
	plot.show()
	#pprint(Y)