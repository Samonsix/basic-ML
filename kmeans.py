import tensorflow as tf
import numpy as np

# 样本数量
num, k = 300, 3

# 正太随机样本
x1 = tf.random_normal(shape=[int(num/3), 2], mean=[119, 80], stddev=[2, 2])
x2 = tf.random_normal(shape=[int(num/3), 2], mean=[140, 97], stddev=[2, 2])
x3 = tf.random_normal(shape=[int(num/3), 2], mean=[70, 120], stddev=[2, 2])

# 定义变量保存样本和中心,并初始化
vector = tf.Variable(tf.concat([x1, x2, x3], axis=0))
# 从打乱的vector中选取前k个样本,做为k个初始中心
center = tf.Variable(tf.slice(tf.random_shuffle(vector), [0, 0], [k, -1]))

# 扩展维度,方便不同尺寸进行减法
vectors = tf.expand_dims(vector, 1)
centers = tf.expand_dims(center, 0)

# 计算每个样本到每个聚类中心的'距离'
diff = tf.reduce_sum(tf.square(tf.subtract(vectors, centers)), axis=2)

# 找到每个样本离哪个聚类中心最近,将会被分配到哪个类别,然后更新聚类中心
min_ind = tf.argmin(diff, axis=1)
'''
下面这一句代码比较长,但骤并不复杂(主要因为拼接时'for c in range(k)'不好分开)
tf.where(tf.equal(min_ind, c))------找到被分配到c类的样本位置
tf.gather(vectors, tf.where(tf.equal(min_ind, c)))-----从总样本中选取被分配到c类的样本
tf.squeeze(tf.gather(vectors, tf.where(tf.equal(min_ind, c))), axis=[1, 2])-----去除空的维度(第1,2维)
tf.reduce_mean(xxx, axis=0, keepdims=True)-----对所有分配到c类的样本取平均,即重新该类的中心
tf.concat(xxx, 0)-----将所有新的中心连接成一个新的list,(每个中心shape=[1,2], 连接起来的shape=[k, 2])
'''
mean = tf.concat(([tf.reduce_mean(tf.squeeze(tf.gather(vectors, tf.where(tf.equal(min_ind, c))), axis=[1, 2])
                                  , axis=0, keepdims=True) for c in range(k)]), 0)

# 将新的中心赋值给center, 方便进行迭代
update_center = tf.assign(center, mean)

sess = tf.Session()

init = tf.global_variables_initializer()

sess.run(init)
for step in range(20):
    cent = sess.run([update_center])
    if step % 2 == 0:
        print(cent)

sess.close()


