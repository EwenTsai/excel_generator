import json

import pymysql
from pygtrans import Translate

if __name__ == '__main__':

    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="vincentmok2", database="shipping")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    with open("country_data.json", 'r') as data:
        country_data_dict = json.load(data)
    # for country_data in country_data_dict:
    # sql = 'insert into country_dict (country_ch, country_en) values ( "%s","%s" );' % (country_data,
    #                                                                                    country_data_dict.get(
    #                                                                                        country_data))

    with open("YQ_data.json", 'r') as data:
        data_dict = json.load(data)
    company_name = '悦琪'

    for channel in data_dict:
        for country in data_dict[channel]:
            for data in data_dict[channel][country]:
                client = Translate()
                text = client.translate(country)
                country_ch = text.translatedText
                sql = 'insert into shipping_data (' \
                      'country_name, weight_range, weight, company_name, shipping_cost, extra_charge,' \
                      'first_weight_charge, ' \
                      'continue_charge, ladder, channel) values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (
                          country_ch, data.get('weight_range'), data.get('weight'), company_name, data.get('shipping_cost'),
                          data.get('extra_charge')
                          , data.get('first_weight'), data.get('continue'), data.get('ladder'), channel)
                sql = sql.replace("\"None\"", "null")
                print(sql)
                cursor.execute(sql)

    db.commit()

    # 关闭数据库连接
    db.close()
