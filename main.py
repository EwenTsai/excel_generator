import json
import pandas as pd

from model import Calculator

if __name__ == '__main__':
    with open("CH_data.json", 'r') as data:
        CH_data_dict = json.load(data)

    with open("4PX_data.json", 'r') as data:
        _4PX_data_dict = json.load(data)

    input_data_frame = pd.read_csv('shipping.csv')
    for index, data in input_data_frame.iterrows():
        input_data_frame.loc[index, 'CH'] = Calculator.calculate(CH_data_dict, data.to_dict())
        input_data_frame.loc[index, '4PX'] = Calculator.calculate(_4PX_data_dict, data.to_dict())

    input_data_frame.to_csv('shipping.csv', index=False)
