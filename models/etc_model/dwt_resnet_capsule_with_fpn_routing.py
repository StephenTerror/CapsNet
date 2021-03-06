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

import tensorflow as tf
from tensorflow.keras import layers

from models.layers.operators_vector import Heterogeneous
from models.layers.routing_vector import RoutingVector
from models.layers.layers_efficient import PrimaryCaps, Length
from models.etc_model.resnet_cifar_dwt import build_graph as build_resnet_dwt_backbone


def capsnet_graph(input_shape, num_classes, routing_name_list=None,
                  regularize=1e-4, depth=18, tiny=True, half=True, heterogeneous=False, softmax=False):
    routing_name_list = ['FPN', 'FPN', 'FPN'] if routing_name_list is None else routing_name_list
    inputs = tf.keras.Input(input_shape)
    # (32, 32, 3) ==>> (8, 8, 128)
    x = build_resnet_dwt_backbone(input_shape, num_classes, depth, tiny, half, backbone=True)(inputs)
    # x = ResNetBackbone(BasicBlockDWT, [2, 2, 2, 2])(inputs)

    x = layers.BatchNormalization()(x)
    # (4, 4, 256) ==>> (1, 1, 256) ==>> (32, 8)
    x = PrimaryCaps(256, x.shape[1], 32, 8)(x)
    # # (4, 4, 512) ==>> (1, 1, 512) ==>> (64, 8)
    digit_caps = RoutingVector(num_classes, routing_name_list, regularize=regularize)(x)

    digit_caps_len = Length()(digit_caps)
    if heterogeneous:
        digit_caps_len = Heterogeneous(num_class=num_classes)((x, digit_caps_len))

    if softmax:
        digit_caps_len = tf.math.softmax(digit_caps_len)

    return tf.keras.Model(inputs=[inputs], outputs=[digit_caps_len])


def build_graph(input_shape, num_classes, routing_name_list, regularize=1e-4,
                depth=18, tiny=True, half=True, heterogeneous=False, softmax=False):
    efficient_capsnet = capsnet_graph(input_shape, num_classes, routing_name_list,
                  regularize, depth, tiny, half, heterogeneous, softmax)
    efficient_capsnet.summary()
    return efficient_capsnet
