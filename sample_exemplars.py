import torch
import json
import numpy as np
import random
data = json.load(open('D:/NJUST/fine-grained data/RPC/single_feature.json'))
no_back_cls = np.load('D:/NJUST/fine-grained data/RPC/no_back_cls.npy')
# sample_num = random.sample(range(1, 41), 10)
# sample_num = [1+i*6 for i in range(6)]
sample_num = [30]
sample_num.sort()
# sample_num1 = [sample_num[0], sample_num[2], sample_num[4]]
# sample_num2 = [sample_num[1], sample_num[3], sample_num[5]]

# sample = {}
# proto = []
#
# sample_num=sample_num1
# for i in data:
#     for k in range(len(sample_num)):
#         for j in range(4):
#             if 'camera{}-{}'.format(j, sample_num[k]) in i['file_name'] and i['class_id'] not in no_back_cls:
#                 if 'back' not in i['file_name']:
#                     sample.update({'{}_{}'.format(i['class_id'], j + k * 4): i['file_name']})
#                 else:
#                     sample.update({'{}_{}'.format(i['class_id'], j + k * 4 + len(sample_num) * 4): i['file_name']})
#             elif 'camera{}-{}'.format(j, sample_num[k]) in i['file_name'] and i['class_id'] in no_back_cls:
#                 sample.update({'{}_{}'.format(i['class_id'], j + k * 4): i['file_name']})
#                 sample.update({'{}_{}'.format(i['class_id'], j + k * 4 + len(sample_num) * 4): i['file_name']})
#
# for i in range(200):
#     temp = torch.zeros([1, 2048])
#     for j in range(len(sample_num)):
#         temp += torch.from_numpy(np.load(
#             '/media/hao/Data/RPC/single_features/RPC_Single_Image_Features_res50_200/features/' + sample[
#                 '{}_{}'.format(i, j)]))
#         if j == len(sample_num)-1:
#             proto.append(temp / len(sample_num))
# proto = torch.cat(proto)
# torch.save(proto, '/media/hao/Data/RPC/single_features/RPC_Single_Image_Features_res50_200/proto_sample_24.pth')

sample_ = {}
# sample_num = sample_num1
for i in data:
    for k in range(len(sample_num)):
        for j in range(4):
            if 'camera{}-{}'.format(j, sample_num[k]) in i['file_name'] and i['class_id'] not in no_back_cls:
                if 'back' not in i['file_name']:
                    sample_.update({'{}_{}'.format(i['class_id'], j + k * 4): i['file_name']})
                else:
                    sample_.update({'{}_{}'.format(i['class_id'], j + k * 4 + len(sample_num) * 4): i['file_name']})
            elif 'camera{}-{}'.format(j, sample_num[k]) in i['file_name'] and i['class_id'] in no_back_cls:
                sample_.update({'{}_{}'.format(i['class_id'], j + k * 4): i['file_name']})
                sample_.update({'{}_{}'.format(i['class_id'], j + k * 4 + len(sample_num) * 4): i['file_name']})
train_data = json.load(open('D:/NJUST/fine-grained data/RPC/instances_train2019.json'))
# test_data = json.load(open('/media/hao/Data/RPC/instances_test2019.json'))
test_data = {'categories': train_data['categories'], 'images': [], 'annotations': []}
for i in range(len(train_data['images'])):
    if train_data['images'][i]['file_name'].split('.')[0]+'.npy' in list(sample_.values()):
        test_data['images'].append(train_data['images'][i])
        test_data['annotations'].append(train_data['annotations'][i])
json.dump(test_data, open('D:/NJUST/fine-grained data/RPC/exemplar_test_8.json', 'w'))
