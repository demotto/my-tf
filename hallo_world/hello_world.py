import tensorflow as tf

h = tf.constant("hello")
w = tf.constant("world")
hw = h + w
hw_val = hw.numpy()
print(hw_val)
