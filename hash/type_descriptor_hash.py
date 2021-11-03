import mmh3
import json

with open('type_descriptor_names.txt', 'r') as f:
    type_descriptor_list = f.read().split('\n')

with open('data_type_names.txt', 'r') as f:
    data_type_list = f.read().split('\n')

type_descriptor_hash_list = [mmh3.hash(type_descriptor, 0xFFFFFFFF) for type_descriptor in type_descriptor_list]

data_type_dict = {}
f = open('type_descriptor_hash.csv', 'w')
for i in range(len(type_descriptor_hash_list)):
    if type_descriptor_hash_list[i] < 0:
        type_descriptor_hash_list[i] += 0xFFFFFFFF + 1
    f.write(str(type_descriptor_hash_list[i]))
    f.write(',')
    f.write(type_descriptor_list[i])
    f.write(',')
    f.write(data_type_list[i])
    f.write('\n')
    data_type_dict[type_descriptor_hash_list[i]] = data_type_list[i]
f.close()

with open('data_type_dict.json', 'w') as f:
    json.dump(data_type_dict, f)
