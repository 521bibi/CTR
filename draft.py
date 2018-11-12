# coding=utf-8
import tensorflow as tf

labels = ''
XXX = ''
biases = ''

# logits = tf.nn.softmax(XXX)
# loss = tf.reduce_mean(-tf.reduce_sum(labels * tf.log(logits)))

logits = tf.matmul(XXX, XXX) + biases
loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=labels, logits=logits, name='losses')
