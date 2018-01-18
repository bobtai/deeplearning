import tensorflow as tf

# define placeholder
width = tf.placeholder(tf.int32)
height = tf.placeholder(tf.int32)

area = tf.multiply(width, height)

with tf.Session() as sess:
	# give placeholder value by feed_dict in a session
	print(sess.run(area, feed_dict={
		width: 3,
		height: 5
		}))

# result
# 15