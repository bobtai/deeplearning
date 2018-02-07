import tensorflow as tf


def add_layer(inputs, input_dim, output_dim, activation=None):
    # initial weights matrix by random_normal
    # weights matrix size is input_dim * output_dim
    weights = tf.Variable(tf.random_normal([input_dim, output_dim]))
    # initial all values of biases matrix are zero
    # biases matrix size is 1 * output_dim
    # in machine learning, biases are recommended to set nonzero, so plus 0.1
    biases = tf.Variable(tf.zeros([1, output_dim]) + 0.1)
    # define Wx + b
    wx_plus_b = tf.matmul(inputs, weights) + biases

    if activation is None:
        outputs = wx_plus_b
    else:
        outputs = activation(wx_plus_b)
    return outputs
