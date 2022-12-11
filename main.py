import json
import pandas as pd

import Calculator

if __name__ == '__main__':
    with open("data/CH_data.json", 'r') as data:
        CH_data_dict = json.load(data)

    with open("data/4PX_data.json", 'r') as data:
        _4PX_data_dict = json.load(data)

    with open("data/YQ_data.json", 'r') as data:
        YQ_data_dict = json.load(data)

    input_data_frame = pd.read_csv('shipping.csv')
    for index, data in input_data_frame.iterrows():
        CH_price = Calculator.calculate(CH_data_dict, data.to_dict())
        YQ_price = Calculator.calculate(YQ_data_dict, data.to_dict())
        _4PX_price = Calculator.calculate(_4PX_data_dict, data.to_dict())
        input_data_frame.loc[index, 'CH'] = CH_price
        input_data_frame.loc[index, 'YQ'] = YQ_price
        input_data_frame.loc[index, '4PX'] = _4PX_price
        input_data_frame.loc[index, 'Lowest'] = Calculator.get_lowest(price_list=[CH_price, YQ_price, _4PX_price])

    input_data_frame.to_csv('shipping.csv', index=False)
