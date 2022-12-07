import json

from model.CH_Shipping import CH_Shipping

if __name__ == '__main__':
    with open("./data.json", 'r') as data:
        data_dict = json.load(data)
        print(data_dict)

    with open("./input.json", 'r') as input_data:
        input_dict = json.load(input_data)

    # CH
    for input_data in input_dict:
        ch_shipping = CH_Shipping(input_data)
        print(input_data)

    with open("./dict.json", 'r') as name_data:
        name_dict = json.load(name_data)
