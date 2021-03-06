# Copyright 2021 Vittorio Mazzia & Francesco Salvetti. All Rights Reserved.
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


def marginLoss(y_true, y_pred):
    lbd = 0.5
    m_plus = 0.9
    m_minus = 0.1

    L = y_true * tf.square(tf.maximum(0., m_plus - y_pred)) + \
        lbd * (1 - y_true) * tf.square(tf.maximum(0., y_pred - m_minus))

    return tf.reduce_mean(tf.reduce_sum(L, axis=1))


def multiAccuracy(y_true, y_pred):
    label_pred = tf.argsort(y_pred, axis=-1)[:, -2:]
    label_true = tf.argsort(y_true, axis=-1)[:, -2:]

    acc = tf.reduce_sum(tf.cast(label_pred[:, :1] == label_true, tf.int8), axis=-1) + \
          tf.reduce_sum(tf.cast(label_pred[:, 1:] == label_true, tf.int8), axis=-1)
    acc /= 2
    return tf.reduce_mean(acc, axis=-1)


def Accuracy(y_true, y_pred):
    label_pred = tf.argsort(y_pred, axis=-1)[:, -1:]
    label_true = tf.argsort(y_true, axis=-1)[:, -1:]
    acc = tf.reduce_sum(tf.cast(label_pred == label_true, tf.int8), axis=-1)
    return tf.reduce_mean(acc, axis=-1)
