'''
import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * tf.random_normal(shape=[1], mean=7, stddev=0.01) + tf.random_normal(shape=[1], mean=0.8, stddev=0.08)

weights = tf.Variable(tf.random_normal(shape=[1], mean=2))
biases = tf.Variable(tf.random_normal(shape=[1], mean=9))

y = weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(2001):
        sess.run(train)
        if step % 200 == 0:
            print (step, sess.run(weights), sess.run(biases))


'''

import tensorflow as tf
import numpy as np

n = 100
x = np.random.normal(20, 5, 100)
y = tf.random_normal(shape=[100], mean=[3], stddev=0.1) * x + tf.random_normal(shape=[100], mean=[0.8], stddev=0.09)

k = tf.Variable(tf.random_normal(shape=[1], mean=8))
b = tf.Variable(tf.random_normal(shape=[1], mean=8))

yx = k * x + b

loss = tf.reduce_mean(tf.square(yx - y))

optimizer = tf.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(20):
        sess.run(train)
        if step % 1 == 0:
            print(sess.run(k))

