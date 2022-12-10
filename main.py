import json
import pandas as pd

from model import Calculator

if __name__ == '__main__':
    with open("CH_data.json", 'r') as data:
        data_dict = json.load(data)

    input_data_frame = pd.read_csv('shipping.csv', skiprows=0)
    for index, data in input_data_frame.iterrows():
        input_data_frame.loc[index, 'CH'] = Calculator.calculate_1(data_dict, data.to_dict())

    input_data_frame.to_csv('shipping.csv')
