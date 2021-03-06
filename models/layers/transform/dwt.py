# Copyright 2021 Hang-Chi Shen. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import pywt
import numpy as np
import tensorflow as tf


class DWT(tf.keras.layers.Layer):
    """
    Convert tf tensor with DWT transform.
    shape[batch, h, w, channel] to shape[batch, h//2, w//2, channel*4].

    :param wave_name: input numpy array([h, w, channel])
    (Waring: Do not support batch, like shape[batch, h, w, channel])
    :param strides: (block_h, block_w) example (2, 2),
    block shape should <= input tensor shape
    :return: 3d tensor [batch, h//2, w//2, channel*4].
    """

    def __init__(self, wave_name='haar', strides=None):
        super(DWT, self).__init__()
        wavelet = pywt.Wavelet(wave_name)
        if strides is None:
            self.strides = [1, 1, 2, 2, 1]
        else:
            self.strides = strides

        # shape (2) ==>> (2, 2) ==>> (2, 2, 1)
        f1 = np.expand_dims(np.outer(wavelet.dec_lo, wavelet.dec_lo), axis=-1)
        f2 = np.expand_dims(np.outer(wavelet.dec_hi, wavelet.dec_lo), axis=-1)
        f3 = np.expand_dims(np.outer(wavelet.dec_lo, wavelet.dec_hi), axis=-1)
        f4 = np.expand_dims(np.outer(wavelet.dec_hi, wavelet.dec_hi), axis=-1)
        # shape 4*(2, 2, 1) ==>> (2, 2, 4)
        filters = np.concatenate((f1, f2, f3, f4), axis=-1)[::-1, ::-1]
        # shape 4*(2, 2, 4) ==>> (1, 2, 2, 1, 4)
        filters = np.expand_dims(filters, axis=(0, -2))
        self.filter = tf.constant(filters, dtype=tf.float32, name='filter')
        size = 2 * (len(wavelet.dec_lo) // 2 - 1)
        self.padding = tf.constant([[0, 0], [size, size], [size, size], [0, 0]])
        self.reshape = None

    def build(self, input_shape):
        self.reshape = tf.keras.layers.Reshape((input_shape[1] // 2, input_shape[2] // 2, input_shape[3] * 4))
        self.built = True

    def get_config(self):
        return super(DWT, self).get_config()

    def call(self, inputs, **kwargs):
        inputs = tf.pad(inputs, self.padding, mode='reflect')
        x = tf.expand_dims(inputs, 1)
        x = tf.transpose(x, (0, 4, 2, 3, 1))
        x = tf.nn.conv3d(x, self.filter, padding='VALID', strides=self.strides)
        x = tf.transpose(x, (0, 2, 3, 1, 4))
        x = self.reshape(x)
        return x

# class DWT(tf.keras.layers.Layer):
#
#     def __init__(self, wave_name='haar', strides=None):
#         super(DWT, self).__init__()
#         wavelet = pywt.Wavelet(wave_name)
#         if strides is None:
#             self.strides = [1, 1, 2, 2, 1]
#         else:
#             self.strides = strides
#
#         # shape (2) ==>> (2, 2) ==>> (2, 2, 1)
#         f1 = np.expand_dims(np.outer(wavelet.dec_lo, wavelet.dec_lo), axis=-1)
#         f2 = np.expand_dims(np.outer(wavelet.dec_hi, wavelet.dec_lo), axis=-1)
#         f3 = np.expand_dims(np.outer(wavelet.dec_lo, wavelet.dec_hi), axis=-1)
#         f4 = np.expand_dims(np.outer(wavelet.dec_hi, wavelet.dec_hi), axis=-1)
#         # shape 4*(2, 2, 1) ==>> (2, 2, 4)
#         filters = np.concatenate((f1, f2, f3, f4), axis=-1)[::-1, ::-1]
#         # shape 4*(2, 2, 4) ==>> (1, 2, 2, 1, 4)
#         filters = np.expand_dims(filters, axis=(0, -2))
#         self.filter = tf.Variable(filters, trainable=False, dtype=tf.float32)
#         self.size = 2 * (len(wavelet.dec_lo) // 2 - 1)
#
#     def build(self, input_shape):
#         print(input_shape)
#
#         self.batch = None
#         self.height = input_shape[1]
#         self.width = input_shape[2]
#         self.channel = input_shape[3]
#
#         print(self.batch, self.height, self.width, self.channel)
#         self.reshape = tf.keras.layers.Reshape((self.height // 2, self.width // 2, self.channel * 4))
#         self.built = True
#
#     def call(self, inputs, **kwargs):
#         self.batch = inputs.shape[0]
#         x = tf.pad(inputs,
#                    tf.constant([[0, 0],
#                                 [self.size, self.size],
#                                 [self.size, self.size],
#                                 [0, 0]]),
#                    mode='reflect')
#         x = tf.expand_dims(x, 1)
#         inputs = tf.split(x, [1] * int(x.shape.dims[4]), 4)
#
#         inputs = tf.concat([x for x in inputs], 1)
#
#         outputs_3d = tf.nn.conv3d(inputs, self.filter, padding='VALID', strides=self.strides)
#
#         outputs = tf.split(outputs_3d, self.channel, 1)
#
#         outputs = tf.concat([x for x in outputs], 4)
#
#         outputs = self.reshape(outputs)
#         return outputs
