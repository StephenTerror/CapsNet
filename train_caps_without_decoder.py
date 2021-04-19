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

import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from models import ETCModel
from utils import Dataset, plotHistory

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_visible_devices(gpus[4], 'GPU')
tf.config.experimental.set_memory_growth(gpus[4], True)

# data_name = 'MNIST'
# data_name = 'MNIST_SHIFT'
# data_name = 'FASHION_MNIST'
# data_name = 'FASHION_MNIST_SHIFT'
data_name = 'CIFAR10'
# data_name = 'CIFAR10_SHIFT'
# data_name = 'SMALLNORB'

dataset = Dataset(data_name, config_path='config.json')
# batch_size = 128


# model = ETCModel(data_name=data_name, model_name='GHOSTNET')
# model = ETCModel(data_name=data_name, model_name='CapsNet_Without_Decoder')
# model = ETCModel(data_name=data_name, model_name='RESNET_DWT50', optimizer='SGD')
# model = ETCModel(data_name=data_name, model_name='RESNET_DWT18', optimizer='SGD')
# model = ETCModel(data_name=data_name, model_name='RESNET_DWT50', optimizer='Adam')
model = ETCModel(data_name=data_name, model_name='RESNET_DWT18', optimizer='Adam')

history = model.train(dataset)

model.model.evaluate(dataset.X_test, dataset.y_test)

# 4.0 Plot history
plotHistory(history)

model.load_graph_weights()  # load graph weights (bin folder)