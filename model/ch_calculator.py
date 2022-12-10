def match_weight(shipping_list, weight):
    for shipping in shipping_list:
        if shipping['weight_range'][0] < weight < shipping['weight_range'][1]:
            return shipping


# 根据重量的不同，运费加额外费用算法
def calculate_1(data_dict, input_data):
    if input_data['channel'] is not None:
        shipping_list = data_dict[input_data['channel']][input_data['country']]
        shipping = match_weight(shipping_list, input_data['weight'])
        return input_data['weight'] * shipping['shipping_cost'] + shipping['extra_charge']


# 首重加续重算法
def calculate_2(data_dict, input_data):
    shipping_list = data_dict[input_data['channel']][input_data['country']]
    shipping = match_weight(shipping_list, input_data['weight'])


# 重量对应运费算法
def calculate_3(data_dict, input_data):
    return 0
