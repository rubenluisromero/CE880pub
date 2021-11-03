
import random
class neuron:
    def __init__(self,n_hidden,xdist,ydist,weights=None):
        self.weights=weights
        self.n_hidden=n_hidden
        self.xdist=xdist
        self.ydist=ydist
    def weightset(self):
        n=self.n_hidden
        weights=self.weights
        if weights is None:
            weights=list()
            for w in range(n*2):
                w=random.random()
                weights.append(w)
        print("The starting weights are: ", weights)
    def hiddenlayer(self):
        x=self.xdist
        y=self.ydist
        n=self.n_hidden
        hlayer=list()
        count=0
        cnt=0
        cnt1=3
        for w in range(n):
            w=(weights[0]*x[count])+(weights[3]*y[count])
            hlayer.append(w)
            count=count+1
            cnt=cnt+1
            cnt1=cnt1+1
        print("The values for the hidden layer are: ",hlayer)

xdistance=[2,2]
ydistance=[2,2]
tst=neuron(2,xdistance,ydistance)
tst.weightset()
tst.hiddenlayer()
