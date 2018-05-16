#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Snowball Beijing, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
百度汉语中的诗词库,支持翻页获取接口, 总共729首诗词
http://hanyu.baidu.com/hanyu/ajax/search_list?category=%E5%9C%BA%E6%99%AF&about=%E5%85%A8%E9%83%A8&dynasty=%E5%85%A8%E9%83%A8&ptype=poem_tag&pn=1

"""

import requests
import json
import pandas as pd


def parse_shici_content(content):
    """
    解析诗词内容
    :param content:
    :return:
    """
    name = content['display_name'][0].replace('\'','')
    if name.find('/') > 0:
        name = name.split('/')[0].replace(' ','')
    auther = content['literature_author'][0].replace('\'','')
    dynasty = content['dynasty'][0].replace('\'','')
    body = content['body'][0].replace('\'','')
    return {'name': name, 'author': auther, 'dynasty': dynasty, 'body': body}


def baidu_crawler(url, page=1):
    """
    翻页获取baidu url内容,并解析
    :param url:
    :param page:
    :return:
    """
    baidu_url = url + str(page)
    resp = requests.get(baidu_url)
    if resp.status_code == 200:
        content = json.loads(resp.content.decode("utf-8"))
        _shici = content['extra']
        _total_page = _shici['total-page']
        _return_num = _shici['return-num']
        _total_num = _shici['entity-num']
        _shici_array = content['ret_array']
        assert _return_num == len(_shici_array)
        shici_items = []
        for item in _shici_array:
            shici_item = parse_shici_content(item)
            shici_items.append(shici_item)

        if page < _total_page:
            _num, _shici_items = baidu_crawler(url, page+1)
            _return_num = _return_num + _num
            shici_items.extend(_shici_items)

        return _return_num, shici_items
    else:
        print("get response error", resp.content)

if __name__ == '__main__':
    baidu_url = 'http://hanyu.baidu.com/hanyu/ajax/search_list?category=%E5%9C%BA%E6%99%AF&about=%E5%85%A8%E9%83%A8&dynasty=%E5%85%A8%E9%83%A8&ptype=poem_tag&pn='
    total_num, shici_items = baidu_crawler(baidu_url)
    shici_df = pd.DataFrame.from_dict(shici_items)

    shici_df.to_csv('data/baidu_shici.csv', encoding='utf-8', sep='|')
    # engine = create_engine('sqlite:///shici.db')
    # shici_df.to_sql('baidu_shici', if_exists='replace', con=engine)

