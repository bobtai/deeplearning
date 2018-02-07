import tensorflow as tf

# create two matrixes
matrix_1 = tf.constant([[2, 3]])  # 1*2 matrix
matrix_2 = tf.constant([[2], [3]])  # 2*1 matrix

product = tf.matmul(matrix_1, matrix_2)  # matrix multiply

# run graph
with tf.Session() as sess:
    result = sess.run(product)
    print(result)  # result = 2*2+3*3 = 13

# result
# [[13]]
