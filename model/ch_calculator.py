
def match_weight(ch_shipping_list, weight):
    for ch_shipping in ch_shipping_list:
        if ch_shipping['weight_range'][0] < weight < ch_shipping['weight_range'][1]:
            return ch_shipping


def calculate(data_dict, input_data):
    if input_data['channel'] is not None:
        ch_shipping_list = data_dict[input_data['channel']][input_data['country']]
        ch_shipping = match_weight(ch_shipping_list, input_data['weight'])
        return input_data['weight'] * ch_shipping['shipping_cost'] + ch_shipping['extra_charge']
