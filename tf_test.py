import numpy as np
# import tensorflow as tf
from copy import deepcopy

# arr = np.array([[0 for i in range(17)] for _ in range(17)])
# gt_a = arr
# gt_b = arr
# print(gt_b)
# gt_a[8][8] = 1
# # print('*******')
# # print(gt_a)
# # gt_a = tf.convert_to_tensor(gt_a)
# gt_b[7][8] = 1
# print('*******')
# print(gt_a)
# gt_b = tf.convert_to_tensor(gt_b)
# sess = tf.Session()
# print(sess.run(gt_a))
# print(sess.run(gt_b))
arr = [2, 3]
a, b = deepcopy(arr), deepcopy(arr)
a[0] = 1
b[1] = 2
print(a)
print(b)