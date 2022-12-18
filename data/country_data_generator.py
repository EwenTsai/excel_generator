import json
from pygtrans import Translate

if __name__ == '__main__':
    with open("CH_data.json", 'r') as data:
        CH_data_dict = json.load(data)

    with open("4PX_data.json", 'r') as data:
        _4PX_data_dict = json.load(data)

    with open("YQ_data.json", 'r') as data:
        YQ_data_dict = json.load(data)

    country_set = set()
    for CH_channel in CH_data_dict:
        for country in CH_data_dict[CH_channel]:
            country_set.add(country)

    for _4PX_channel in _4PX_data_dict:
        for country in _4PX_data_dict[_4PX_channel]:
            country_set.add(country)

    for YQ_channel in YQ_data_dict:
        for country in YQ_data_dict[YQ_channel]:
            country_set.add(country)

    country_dict = dict()
    for country in country_set:
        client = Translate()
        text = client.translate(country)
        country_dict[country] = text.translatedText

    with open("country_data.json", "w") as outfile:
        outfile.write(json.dumps(country_dict, ensure_ascii=False))
