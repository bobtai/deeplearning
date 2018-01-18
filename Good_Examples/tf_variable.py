import tensorflow as tf

# define variable
total = tf.Variable(0, name='counter')
# print(total.name)  # total.name = counter:0

# define constant
one = tf.constant(1)

# define add step
new_value = tf.add(total, one)

# assign new_value to total
update = tf.assign(total, new_value)

# must have if define variable
init = tf.global_variables_initializer()

with tf.Session() as sess:
	sess.run(init)
	for _ in range(3):
		sess.run(update)
		print(sess.run(total))

# result
# 1
# 2
# 3