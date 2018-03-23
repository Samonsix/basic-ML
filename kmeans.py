import tensorflow as tf
import numpy as np

n = 200
k = 2
x1 = tf.random_normal(shape=[100, 2], mean=[119, 80], stddev=[2, 2])
x2 = tf.random_normal(shape=[100, 2], mean=[140, 97], stddev=[2, 2])

vector = tf.Variable(tf.concat([x1, x2], axis=0))
center = tf.Variable(tf.slice(tf.random_shuffle(vector), [0, 0], [k, -1]))

vectors = tf.expand_dims(vector, 1)
centers = tf.expand_dims(center, 0)

diff = tf.reduce_sum(tf.square(tf.subtract(centers, vectors)), axis=2)
loss = tf.reduce_sum(diff)

min_ind = tf.argmin(diff, axis=1)

mean = tf.concat(([tf.reduce_mean(tf.squeeze(tf.gather(vectors, tf.where(tf.equal(min_ind, c))), axis=[1, 2])
                                  , axis=0, keepdims=True) for c in range(k)]), 0)

update_center = tf.assign(center, mean)

sess = tf.Session()

init = tf.global_variables_initializer()

sess.run(init)
for step in range(30):
    cent, lss = sess.run([update_center, loss])
    if step % 1 == 0:
        print(cent)
        print(lss)

sess.close()


