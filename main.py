import json

from model import ch_calculator

if __name__ == '__main__':
    with open("./data.json", 'r') as data:
        data_dict = json.load(data)

    with open("./input.json", 'r') as input_data:
        input_list = json.load(input_data)

    with open("./dict.json", 'r') as name_data:
        name_dict = json.load(name_data)

    # CH
    f = open('result.csv', 'w')
    for input_data in input_list:
        input_data['CH'] = ch_calculator.calculate(data_dict['CH'], input_data)
        f.write(input_data['country'] + ',')
        f.write(input_data['channel'] + ',')
        f.write(str(input_data['weight']) + ',')
        f.write(str(input_data['CH']) + ','+'\n')
    f.close()
