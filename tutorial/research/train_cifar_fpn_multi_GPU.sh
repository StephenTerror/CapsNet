#!/bin/bash

## Adam optimizer
#mkdir "log"
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_Tiny_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 1 --test True \
#>>./log/DWT_Tiny_Half_R18_Tiny_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 2 --test True \
#>>./log/DWT_Tiny_Half_R18_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_Attention_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 3 --test True \
#>>./log/DWT_Tiny_Half_R18_Attention_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_Tiny_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 4 --test True \
#>>./log/DWT_Tiny_Half_R34_Tiny_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 5 --test True \
#>>./log/DWT_Tiny_Half_R34_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_Attention_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 6 --test True \
#>>./log/DWT_Tiny_Half_R34_Attention_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_Tiny_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 7 --test True \
#>>./log/DWT_Tiny_Half_R50_Tiny_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 8 --test True \
#>>./log/DWT_Tiny_Half_R50_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_Attention_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 9 --test True \
#>>./log/DWT_Tiny_Half_R50_Attention_FPN_CIFAR.txt &
#
#echo "[INFO]Starting!"


## heterogeneous
#mkdir "log"
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_Tiny_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 1 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R18_Tiny_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 2 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R18_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_Attention_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 3 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R18_Attention_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_Tiny_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 4 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R34_Tiny_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 5 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R34_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_Attention_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 6 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R34_Attention_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_Tiny_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 7 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R50_Tiny_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 8 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R50_FPN_CIFAR.txt &
#
#python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_Attention_FPN_CIFAR \
#--data-name CIFAR10 --initial-epoch 0 --select-gpu 9 --test True  --heterogeneous True\
#>>./log/DWT_Tiny_Half_R50_Attention_FPN_CIFAR.txt &
#
#echo "[INFO]Starting!"


# softmax
mkdir "log"

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_Tiny_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 1 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R18_Tiny_FPN_CIFAR.txt &

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 2 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R18_FPN_CIFAR.txt &

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R18_Attention_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 3 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R18_Attention_FPN_CIFAR.txt &

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_Tiny_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 4 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R34_Tiny_FPN_CIFAR.txt &

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 5 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R34_FPN_CIFAR.txt &

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R34_Attention_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 6 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R34_Attention_FPN_CIFAR.txt &

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_Tiny_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 7 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R50_Tiny_FPN_CIFAR.txt &

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 8 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R50_FPN_CIFAR.txt &

python main.py --arch ETCModel --model-name DWT_Tiny_Half_R50_Attention_FPN_CIFAR \
--data-name CIFAR10 --initial-epoch 0 --select-gpu 9 --test True  --softmax True\
>>./log/DWT_Tiny_Half_R50_Attention_FPN_CIFAR.txt &

echo "[INFO]Starting!"
