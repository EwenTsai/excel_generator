def get_lowest(price_list: list):
    for price in price_list:
        if not type(price) == float:
            if not type(price) == int:
                return None
    return min(price_list)


def match_weight(shipping_list: list, weight: float):
    for shipping in shipping_list:
        if shipping.get('weight_range') is not None:
            if shipping['weight_range'][0] <= weight <= shipping['weight_range'][1]:
                return shipping
        elif shipping.get('weight') is not None:
            if shipping['weight'] == weight:
                return shipping
        elif shipping.get('ladder') is not None:
            return shipping
    raise Exception("didn't match weight")


def match_country(data_dict: dict, country: str):
    for channel in data_dict:
        if data_dict[channel].get(country) is not None:
            return data_dict[channel].get(country)
    raise Exception("didn't match country")


def weight_rounding(weight: float, ladder: float):
    if weight < ladder:
        return ladder
    elif weight % ladder == 0:
        return weight
    else:
        return (weight // ladder + 1) * ladder


def calculate(data_dict: dict, input_data: dict):
    try:
        shipping_list = match_country(data_dict, input_data['country'])
        shipping = match_weight(shipping_list, input_data['weight'])
        if shipping.get('shipping_cost') is not None and shipping.get('extra_charge') is not None:
            return calculate_1(shipping, input_data)
        elif shipping.get('first_weight') is not None and shipping.get('continue') is not None and shipping.get(
                'ladder') is not None and shipping.get('extra_charge') is None:
            return calculate_2(shipping, input_data)
        elif shipping.get('weight') is not None and shipping.get('shipping_cost') is not None:
            return calculate_3(shipping)
        elif shipping.get('first_weight') is not None and shipping.get('continue') is not None and shipping.get(
                'ladder') is not None and shipping.get('extra_charge') is not None:
            return calculate_4(shipping, input_data)
        else:
            return "this company's country source data is wrong"
    except Exception as ex:
        return ex


# 根据重量的不同，运费加额外费用算法
def calculate_1(shipping: dict, input_data: dict):
    return input_data['weight'] * shipping['shipping_cost'] + shipping['extra_charge']


# 首重加续重算法
def calculate_2(shipping: dict, input_data: dict):
    weight = weight_rounding(input_data['weight'], shipping['ladder'])
    if weight == shipping['ladder']:
        return shipping['first_weight']
    else:
        return shipping['first_weight'] + shipping['continue'] * (weight / shipping['ladder'] - 1)


# 重量对应运费算法
def calculate_3(shipping: dict):
    return shipping['shipping_cost']


def calculate_4(shipping: dict, input_data: dict):
    weight = weight_rounding(input_data['weight'], shipping['ladder'])
    if weight == shipping['ladder']:
        return shipping['first_weight'] + shipping['extra_charge']
    else:
        return shipping['first_weight'] + shipping['continue'] * (weight / shipping['ladder'] - 1) + \
            shipping['extra_charge']
