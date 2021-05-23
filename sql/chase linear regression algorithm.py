x1,          x2,       x3 -->              y linear regression
-100, 100.  10-20      red,green,blue
like training a deep neural network



1. do simple feature transformation
1-hot encoding for x3 (0,1,3)
x4-read, x5-green, x6-blue binary

x1 = (x1 - mean)/std #mean/std is calculated from training data, testing will use the same mean/std
do same for x2 as x1

-------------
|
|
|
-------------

2. y = t1*x1 + t2*x2 + .. + b.  define batch_size = nb
define loss fuction: L = sum_nb(y_hat - y)^2 = sum_nb(b + T*X - y)^2 + lambda*sum_nb(ti^2)
do gradien decent: dL/dt_i = 2*(b_i + t_1*x1 + .. ti*xi ... -y)*xi + lambda*sum_nb(t)*1

dropout: dropout_rate = 0.1
dL/dt_i = 2*(b_i + (random()>dropout_rate)*t_1*x1 + .. ti*xi ... -y)*xi

3. udpate coeffficents:
ti = ti_prev - lr*dL/dt_i

4. repeat step 3 until go through whole dataset for 1 epoch, and repeat for k epoch

------------------
1. 
training, testing, ytrain, ytest all in dataframe
x1_mean = mean(training[x1])
x1_std = std(training[x1])
training[x1] = (training[x1] - x1_mean)/x1_std
testing[x1] = (testing[x1] - x1_mean)/x1_std
validation

# do the same for x2

traing.iloc[x3, x3 == 'red'] == 0. #drawback: there hsould be no ordering
training[x4] = training[x3] == 'red'
training[x5] = training[x3] == 'green'
training[x6] = training[x3] == 'blue'

2. 
epochs = 5
batch_size = k
lr = 0.0001
residual_square = []
for e in range(epochs):
	training = randomize(training)
	for batch in range(len(training)//k + 1):
		for t in [t1, t2, t4, t5, t6]:
			dl/dt = calculate_gradient(training[(batch-1)*K: batch*k], T) 
			t = t - lr*dl/dt
			#output performance metrics on validation
			write_output(epoch, batch, sum(y_hat - y)^2)

		



