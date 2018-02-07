import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# create graph
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 1-dim, initial range -1 ~ 1
biases = tf.Variable(tf.zeros([1]))  # 1-dim, initial value = 0

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))  # define loss

optimizer = tf.train.GradientDescentOptimizer(0.5)  # learning rate = 0.5
train = optimizer.minimize(loss)

# excute graph
with tf.Session() as sess:  # auto close session
	init = tf.global_variables_initializer()  # initial all global variables
	sess.run(init)
	
	for step in range(301):  # training
		sess.run(train)
		if step % 20 == 0:
			print(step, sess.run(Weights), sess.run(biases))