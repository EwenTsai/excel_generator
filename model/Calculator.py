def match_weight(shipping_list, weight):
    for shipping in shipping_list:
        if shipping['weight_range'][0] < weight < shipping['weight_range'][1]:
            return shipping


def match_country(data_dict, country):
    for channel in data_dict:
        if data_dict[channel].get(country) is not None:
            return data_dict[channel].get(country)


def weight_rounding(weight, ladder):
    if weight < ladder:
        return ladder
    elif weight % ladder == 0:
        return weight
    else:
        return (weight // ladder + 1) * ladder


def calculate(data_dict, input_data):
    shipping_list = match_country(data_dict, input_data['country'])
    shipping = match_weight(shipping_list, input_data['weight'])
    if shipping.get('shipping_cost') is not None and shipping.get('extra_charge') is not None:
        return calculate_1(shipping, input_data)
    elif shipping.get('first_weight') is not None and shipping.get('continue') is not None and shipping.get(
            'ladder') is not None:
        return calculate_2(shipping, input_data)


# 根据重量的不同，运费加额外费用算法
def calculate_1(shipping, input_data):
    return input_data['weight'] * shipping['shipping_cost'] + shipping['extra_charge']


# 首重加续重算法
def calculate_2(shipping, input_data):
    weight = weight_rounding(input_data['weight'], shipping['ladder'])
    if weight == shipping['ladder']:
        return shipping['first_weight']
    else:
        return shipping['first_weight'] + shipping['continue'] * (weight / shipping['ladder'] - 1)


# 重量对应运费算法
def calculate_3(shipping, input_data):
    weight = weight_rounding(input_data['weight'], shipping['ladder'])
    print(weight)
