
conda activate pytorch

tensorboard --logdir=runs

torch.cuda.is_available()

device = torch.device("cuda")


import torch
x = torch.rand(2,2, device=device)
y = torch.rand(2,2)
y = y.to(device)
y = y.to("cpu")

y.add_(x)  #inplace
y + x #element wise, *, /
torch.add(x,y)
torch.sub(x,y) #mul, div

print(x[:,0]) #slicing
x[1,1].item() #actuall value

x.view(4) #reshaping, 
x.view(-1,8) #fix 8, the other determined by number of element

import numpy as np
b = x.numpy()
print(type(b)) #numpy.ndarray, b and x share the same memory when in CPU, numpy can only handle 
x = torch.from_numpy(b)


x = torch.ones(5,requires_grad=True)


grad
x = torch.rand(3, requires_grad=True)
print(x)
y = x + 2
z = y*y*2
z = z.mean()
z.backward()
print(x.grad)
#or give vector if not scalar
v = torch.tensor([0.1,0.2,0.3], dtype = torch.float32)
z.backward(v)
#remove grad
# x.requires_grad_(False)
# y = x.detach()
# with torch.no_grad():
#     y  = x + 2


weights = torch.ones(4,requires_grad = True)
for epoch in range(3):
    model_output = (weights*3).sum()
    model_output.backward()
    
    print(weights.grad)
    weights.grad.zero_() #avoid grad accumulate



# linear regression
x = torch.tensor(1.0)
y = torch.tensor(2.0)
w = torch.tensor(1.0, requires_grad = True)
#forward pass
y_hat = w*x
loss = (y_hat - y)**2
print(loss)
#backward pass
loss.backward()
print(w.grad)
#update weights, next forward and backward


#manual numpy
# f = 2*x

X = np.array([1,2,3,4], dtype = np.float32)
y = np.array([2,4,6,8], dtype = np.float32)
w = 0.0

# model prediction
def forward(x):
    return w*x

# loss = MSE
def loss(y, y_predicted):
    return ((y_predicted -y)**2).mean()

# gradient
# MSE = 1/N*(w*x - y)**2
# dJ/dw = 1/N 2x (w*x - y)
def gradient(x,y,y_predicted):
    return np.dot(2*x, y_predicted-y).mean()

print(f'Prediction before training: f(5) = {forward(5):.3f}')

learning_rate = 0.01
n_iters = 10

for epoc in range(n_iters):
    #prediction forward
    y_pred = forward(X)
    # loss
    l = loss(y, y_pred)
    #gradidents
    dw = gradient(X,y, y_pred)
    #update weights
    w -= learning_rate*dw
    if epoch%1 == 0:
        print(f'epoch {epoch + 1}: w = {w:.3f}, loss = {l:.8f}')

print(f'Prediction after training: f(5) = {forward(5):.3f}')

#manual pytorch version
X = torch.tensor([1,2,3,4], dtype = torch.float32)
y = torch.tensor([2,4,6,8], dtype = torch.float32)
w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

# model prediction
def forward(x):
    return w*x

# loss = MSE
def loss(y, y_predicted):
    return ((y_predicted -y)**2).mean()

# gradient
# MSE = 1/N*(w*x - y)**2
# dJ/dw = 1/N 2x (w*x - y)
def gradient(x,y,y_predicted):
    return np.dot(2*x, y_predicted-y).mean()

print(f'Prediction before training: f(5) = {forward(5):.3f}')

learning_rate = 0.01
n_iters = 100

for epoch in range(n_iters):
    #prediction forward
    y_pred = forward(X)
    # loss
    l = loss(y, y_pred)
    #gradidents
    l.backward() #dl/dw
    #update weights
    with torch.no_grad():
        w -= learning_rate*w.grad
    
    #zero gradients
    w.grad.zero_()
    if epoch%10 == 0:
        print(f'epoch {epoch + 1}: w = {w:.3f}, loss = {l:.8f}')

print(f'Prediction after training: f(5) = {forward(5):.3f}')


#all pytorch module
import torch
import torch.nn as nn

X = torch.tensor([[1],[2],[3],[4]], dtype = torch.float32)
y = torch.tensor([[2],[4],[6],[8]], dtype = torch.float32)

X_test = torch.tensor([5], dtype=torch.float32)

n_samples,n_features = X.shape
input_size = n_features
output_size = n_features

model = nn.Linear(input_size, output_size)

#or define a model
class LinearRegression(nn.Module):
    def __init__(self,input_dim,output_dim):
        super(LinearRegression,self).__init__()
        #define layers
        self.lin = nn.Linear(input_dim, output_dim)
    
    def forward(self,x):
        return self.lin(x)


class LogisticRegression(nn.Module):
    def __init__(self,n_input_features):
        super(LogisticRegression,self).__init__()
        self.linear=nn.Linear(n_input_features,1)
        
    def forward(self,x):
        y_predicted = torch.sigmoid(self.linear(x))
        return y_predicted
    
model = LinearRegression(input_size,output_size)

print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')

learning_rate = 0.01
n_iters = 1000

loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)

for epoch in range(n_iters):
    #prediction forward
    y_pred = model(X)
    # loss
    l = loss(y, y_pred)
    #gradidents
    l.backward() #dl/dw
    #update weights
    optimizer.step()
    
    #zero gradients
    optimizer.zero_grad()
    
    if epoch%100 == 0:
        [w,b] = model.parameters()
        print(f'epoch {epoch + 1}: w = {w[0][0].item():.3f}, loss = {l:.8f}')

print(f'Prediction after training: f(5) = {model(X_test).item():.3f}')


#big data size
# 1) design model (input, output size, forward pass)
# 2) construct loss and optimizer
# 3) training loop
#    - forward pass: compute prediction
#    - backward pass: gradients
#.   - update weights

import torch
import torch.nn as nn
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

X_numpy, y_numpy = datasets.make_regression(n_samples=100,n_features=1,noise=20,random_state=1)

X = torch.from_numpy(X_numpy.astype(np.float32))
y = torch.from_numpy(y_numpy.astype(np.float32))

y = y.view(y.shape[0],1)
n_sample,n_features=X.shape

# 1)model
input_size = n_features
output_size = 1
model = nn.Linear(input_size, output_size)

#2) loss and optimizer
learning_rate = 0.01
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr = learning_rate)

# 3) training loop
num_epochs = 100
for epoch in range(num_epochs):
    #forward
    y_predicted = model(X)
    loss = criterion(y_predicted, y)
    #backward
    loss.backward()
    #update
    optimizer.step()
    optimizer.zero_grad()
    
    if (epoch+1)%10 == 0:
        print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')
              
#plot
predicted = model(X).detach().numpy() #do not calcualte gradient anymore
plt.plot(X_numpy, y_numpy, 'ro')
plt.plot(X_numpy, predicted, 'b')
plt.show()



#load data and batch
import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
import numpy as np
import math

class WineDataset(Dataset):
    def __init__(self, transform=None):
        xy = np.loadtxt('./Desktop/wine.csv', delimiter=",", dtype=np.float32, skiprows=1)
        self.x = (xy[:,1:])
        self.y = (xy[:,[0]])
        self.n_samples = xy.shape[0]
        
        self.transform = transform
                                     
    def __getitem__(self,index):
        sample = self.x[index], self.y[index]
        if self.transform:
            sample = self.transform(sample)
        
        return sample
                                     
    def __len__(self):
        return self.n_samples

class ToTensor:
    def __call__(self,sample):
        inputs,targets=sample
        return torch.from_numpy(inputs), torch.from_numpy(targets)

class MulTransform:
    def __init__(self,factor):
        self.factor = factor
        
    def __call__(self,sample):
        inputs,targets=sample
        inputs = self.factor
        return iniputs, targets

composed = torchvision.transform.Compose(ToTensor(),MulTransform())

dataset = WineDataset(transfrom=ToTensor())

dataloader = DataLoader(dataset=dataset, batch_size=4, shuffle=True,num_workers=2)
     
# dataiter = iter(dataloader)
# data = dataiter.next()

num_epochs = 2
total_samples = len(dataset)
n_iterations = math.ceil(total_samples/4)

for epoch in range(num_epochs):
    for i, (inputs, labels) in enumerate(dataloader):
        if (i+1)%5 == 0:
            print(f'epoch {epoch+1}/{num_epochs}, step{i+1}/{n_iterations}, inputs {inputs.shape}')


 #cross entropy L = -1/N(sum(y*logY_hat))
 #softmax y_hat = e^yi/sum(e^yi)
 import torch
import torch.nn as nn
import numpy as np

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x), axis=0)


def cross_entropy(actual, predicted):
    loss = -np.sum(actual*np.log(predicted))
    return loss #/float(predicted.shape[0])

loss = nn.CrossEntropyLoss()
# = nn.LogSoftmax + nn.NLLLoss; Y has class labels, not one-hot
# Y_pred has raw scores (logits, no softmax)

Y = torch.tensor([0])
# nsamples X nclasses
Y_pred_good = torch.tensor([[2.0,1.0,0.1]])

l1 = loss(Y_pred_good, Y)
print(l1.item())

_,prediction = torch.max(Y_pred_good, 1)


#classification
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

#multiclass problem
class NeuralNet2(nn.Module):
    def __init__(self,input_size, hidden_size, num_classes):
        super(NeuralNet2, self).__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_size, num_classes)
        
    def forward(self,x):
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        #no softmax at the end
        return out
    
model = NeuralNet2(input_size = 28*28, hidden_size = 5, num_classes = 3)
criterion = nn.CrossEntropyLoss() #applies softmax
#nn.BCELoss() binary cross entropy need sigmoid at the end
class NeuralNet2(nn.Module):
    def __init__(self,input_size, hidden_size):
        super(NeuralNet2, self).__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_size, 1)
        self.sigmoid = nn.Sigmoid()
        
    def forward(self,x):
        out = self.linear1(x)
        out = self.relu(out) #nn.Sigmoid, nn.Softmax, nn.TanH, nn.LeakyReLU
        out = self.linear2(out)
        y_pred = torch.sigmoid(out) #or self.sigmoid(out)
        return y_pred

    def forward2(self,x):
        out = torch.relu(self.linear1(x)) #torch.Softmax, torch.tanh
        #F.relu, F.leaky_relu()
        out = torch.sigmoid(self.linear2(out))
        return out

# sigmoid function f(x) = 1/(1+exp(-x)) (0,1) last layer in binary class
# TanH f(x) = 2/(1+exp(-2x)) - 1 (-1,1)
# ReLU f(x) = max(0,x) hidden layers, leaky x if x >= 0 or a*x a = 0.001. avoid vanishing gradient because normal version slope is 0 at x < 0
# softmax, last layer in multi class




# MNIST
# DataLoader, Transformation
# Multilayer Neural Net, activation function
# Loss and Optimizer
# Training Looop (batch training)
# Model evaluation
# GPU support

import torch
import torch.nn  as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

#device config
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# hyper parameters
input_size = 784 #28*28
hidden_size = 100
num_classes = 10
num_epochs = 2
batch_size = 100
learning_rate = 0.001

# MNIST
training_dataset = torchvision.datasets.MNIST(root='./data', train=True, 
            transform = transforms.ToTensor(), download=True)
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, 
            transform = transforms.ToTensor(), download=True)

train_loader = torch.utils.data.DataLoader(dataset=training_dataset, 
                    batch_size =batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, 
                    batch_size =batch_size, shuffle=False)

examples = iter(train_loader)
samples, labels = examples.next()
print(samples.shape,labels.shape)

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(samples[i][0], cmap='gray') 
plt.show

class NeuralNet(nn.Module):
    def __init__(self,input_size, hidden_size, num_classes):
        super(NeuralNet,self).__init__()
        self.l1 = nn.Linear(input_size,hidden_size)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(hidden_size,num_classes)
    
    def forward(self,x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        #no softmax
        return out
        
model=NeuralNet(input_size, hidden_size, num_classes)
#loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

#training loop
n_total_steps = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        # 100, 1(channel), 28, 28
        #need 100, 784
        images = images.reshape(-1,28*28).to(device)
        labels = labels.to(device)
        
        #forward
        outputs = model(images)
        loss = criterion(outputs,labels)
        
        #backwards
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1)%100 == 0:
            print(f'epoch {epoch+1}/{num_epochs}, step {i+1}/{n_total_steps}, loss = {loss.item():.4f}')
            
#test
with torch.no_grad():
    n_correct = 0
    n_samples = 0
    for images, labels in test_loader:
        images = images.reshape(-1,28*28).to(device)
        labels = labels.to(device) 
        outputs = model(images)
        
        # value, index
        _,predictions = torch.max(outputs,1)
        n_samples += labels.shape[0]
        n_correct += (predictions==labels).sum().item()
        
acc = 100.0*n_correct/n_samples
print(f'accuracy = {acc}')



#convolutional network: (W - F + 2P)/S + 1
# pooling: max in a region, move whole region, reduce size and computation cost/parameters, avoid overfitting by abstract form of input

import torch
import torch.nn  as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np

#device config
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# hyper
num_epochs = 4
batch_size = 4
learning_rate = 0.001

# dataset has PILImage range [0,1], transform to [-1,1]
transform = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))
        ])

training_dataset = torchvision.datasets.CIFAR10(root='./data1', train=True, 
            transform = transform, download=True)
test_dataset = torchvision.datasets.CIFAR10(root='./data1', train=False, 
            transform = transform, download=True)

train_loader = torch.utils.data.DataLoader(dataset=training_dataset, 
                    batch_size =batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, 
                    batch_size =batch_size, shuffle=False)

classes = ('plane', 'car', 'bird', 'cat',
            'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# implement conv net
class ConvNet(nn.Module):
    def __init__(self):
        super(ConvNet, self).__init__()
        self.conv1 = nn.Conv2d(3,6,5) #input ch, output ch, kernel_size
        self.pool = nn.MaxPool2d(2,2) #kernel size, strip size
        self.conv2 = nn.Conv2d(6,16,5)
        self.fc1 = nn.Linear(16*5*5, 120) #use the formula of padding/stripe#the 5 is not from above line
        self.fc2 = nn.Linear(120,84)
        self.fc3 = nn.Linear(84,10) #10 classes
    
    def forward(self,x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1,16*5*5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        
        return x

    
model = ConvNet().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)

n_total_steps = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        #origin shape: [4,3,32,32] = [4,3,1024]
        # input_layer: 3 input channels, 6 output channels, 5 kernel size
        images = images.to(device)
        labels = labels.to(device)
        
        #forward pass
        outputs = model(images)
        loss = criterion(outputs,labels)
        
        # backwrd and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if (i+1)%100 == 0:
            print(f'epoch {epoch+1}/{num_epochs}, step {i+1}/{n_total_steps}, loss = {loss.item():.4f}')
            
print('Finished Training')

with torch.no_grad():
    n_correct = 0
    n_samples = 0
    n_class_correct = [0 for i in range(10)]
    n_class_samples = [0 for i in range(10)]
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)
        
        # value, index
        _,predicted = torch.max(outputs,1)
        n_samples += labels.shape[0]
        n_correct += (predicted==labels).sum().item()
        
        for i in range(batch_size):
            label = labels[i]
            pred = predicted[i]
            if (label == pred):
                n_class_correct[label] += 1
            n_class_samples[label] += 1
            
    acc = 100.0*n_correct/n_samples
    print(f'Accuracy of the network: {acc}%')
    
    for i in range(10):
        acc = 100.0*n_class_correct[i]/n_class_samples[i]
        print(f'Accuracy fo {classes[i]}: {acc}%')
                




