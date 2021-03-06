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

import numpy as np
import tensorflow as tf
from scipy import fft
from .block2channel import Block2Channel2d
from .block2channel import Block2Channel3d
from .block2channel import block2channel_2d
from .block2channel import block2channel_3d


def channel2fft(np_array, block_shape, check_shape=True):
    """
    Convert 2d or 3d numpy array to 3d, then do fft op at last dimension.
    :param np_array: 2d or 3d array
    :param block_shape: (block_h, block_w) example (2, 2),
    block shape should <= input tensor shape
    :param check_shape: check shape while run block2channel_2d(...) or block2channel_3d(...)
    :return: 3d numpy array, the same like output of block2channel_2d(...) or block2channel_3d(...)
    """
    if len(np_array.shape) == 2:
        out = block2channel_2d(np_array, block_shape, False, check_shape)

    elif len(np_array.shape) == 3:
        out = block2channel_3d(np_array, block_shape, False, check_shape)

    else:
        print("shape {} not support, recommend [h, w] or [h, w, channel]".format(np_array.shape))
        raise NotImplementedError
    # todo: fix bugs here
    return fft.rfft(out.astype(np.float32))


class RFFTLayer2d(tf.keras.layers.Layer):
    """
    Convert tf tensor with batch(like [batch, h, w]) to [h//block_H, w//block_w, block_h*block_w]
    then do DCT op at last dimension.
    :param block_shape: (block_h, block_w) example (2, 2),
    block shape should <= input tensor shape
    :param check_shape: check shape while run block2channel_2d(...)
    :return: [batch, h//block_H, w//block_w, block_h*block_w]
    """

    def __init__(self, block_shape, groups=None, dct_type=2, check_shape=True, **kwargs):
        super(RFFTLayer2d, self).__init__(**kwargs)
        self.block_shape = block_shape
        self.groups = groups
        self.dct_type = dct_type
        self.check_shape = check_shape
        self.block2Channel2d = None

    def build(self, input_shape):
        self.block2Channel2d = Block2Channel2d(self.block_shape, False, self.check_shape)

    def call(self, inputs, **kwargs):
        # [batch, h, w] ==>> [batch, h//block_H, w//block_w, block_h*block_w]
        out = self.block2Channel2d(inputs)
        if self.groups:
            print("NotImplemented!")
            raise NotImplemented
        else:
            return tf.cast(tf.signal.rfft(tf.cast(out, dtype=tf.float32)), dtype=tf.float32)


class RFFTLayer3d(tf.keras.layers.Layer):
    """
    Convert tf tensor with batch [batch, h, w, channel] to [batch, h//block_H, w//block_w, channel*block_h*block_w],
    then do rfft op at last dimension.
    :param block_shape: (block_h, block_w) example (2, 2),
    block shape should <= input tensor shape
    :param dct_type: default 2, example tf.signal.dct(tensor, type=dct_type)
    :param check_shape: check shape while run block2channel_3d(...)
    :return: [batch, h//block_H, w//block_w, channel*block_h*block_w]
    """

    def __init__(self, block_shape, groups=None, data_type=tf.float32, check_shape=True, **kwargs):
        super(RFFTLayer3d, self).__init__(**kwargs)
        self.block_shape = block_shape
        self.groups = groups
        self.data_type = data_type
        self.check_shape = check_shape
        self.block2Channel3d = None

    def build(self, input_shape):
        self.block2Channel3d = Block2Channel3d(self.block_shape, False, self.check_shape)

    def call(self, inputs, **kwargs):
        # [batch, h, w, channel] ==>> [batch, h//block_H, w//block_w, channel*block_h*block_w]
        out = self.block2Channel3d(inputs)
        if self.groups:
            print("NotImplemented!")
            raise NotImplemented

        else:
            return tf.cast(tf.signal.rfft(tf.cast(out, dtype=tf.float32)), dtype=self.data_type)
