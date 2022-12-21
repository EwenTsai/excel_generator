import json
import os

import Calculator

if __name__ == '__main__':
    with open("data/CH_data.json", 'r') as data:
        CH_data_dict = json.load(data)

    with open("data/4PX_data.json", 'r') as data:
        _4PX_data_dict = json.load(data)

    with open("data/YQ_data.json", 'r') as data:
        YQ_data_dict = json.load(data)

    input_data_list = list()
    header = '国家,重量,春红,悦琪,4PX,最低价格\n'
    with open('shipping.csv', 'r', encoding="utf-8") as file:
        for line in file:
            if not line == header:
                data_arr = line.replace("\n", "").split(",")
                data_dict = dict()
                data_dict['country'] = data_arr[0]
                data_dict['weight'] = float(data_arr[1])
                input_data_list.append(data_dict)

    output_file_data = str(header)
    for input_data in input_data_list:
        CH_price = Calculator.calculate(CH_data_dict, input_data)
        YQ_price = Calculator.calculate(YQ_data_dict, input_data)
        _4PX_price = Calculator.calculate(_4PX_data_dict, input_data)

        output_file_data += input_data['country']
        output_file_data += ","
        output_file_data += str(input_data['weight'])
        output_file_data += ","
        output_file_data += str(CH_price)
        output_file_data += ","
        output_file_data += str(YQ_price)
        output_file_data += ","
        output_file_data += str(_4PX_price)
        output_file_data += ","
        output_file_data += str(Calculator.get_lowest(price_list=[CH_price, YQ_price, _4PX_price])) + "\n"

    os.remove("shipping.csv")

    with open("shipping.csv", "w") as file:
        file.write(output_file_data)
