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
生成诗词数据库的索引, 结构如下:
1\ 数据库中每个字出现的次数
2\ 某个字在那些诗词中出现过
3\ 某个作者的所有诗词
4\ 某个朝代的所有诗词
"""
import pandas as pd
from sqlalchemy import create_engine


def gen_index(shici_file):
    shici_df= pd.read_csv(shici_file, sep='|')
    indexes = []
    # auther index
    author_groups = shici_df.groupby('author')
    for author, group in author_groups:
        indexes.append({'name': author, 'type': 'author', 'index': ",".join([str(index) for index in group.index.values])})

    # dynasty index
    dynasty_groups = shici_df.groupby('dynasty')
    for dynasty, group in dynasty_groups:
        indexes.append({'name': dynasty, 'type': 'dynasty', 'index': ",".join([str(index) for index in group.index.values])})

    # body
    word_index = {}
    for index, row in shici_df.iterrows():
        body = row['body']
        for word in body:
            if word in word_index:
                _indexes = word_index.get(word)
                _indexes.add(str(index))
                word_index.update({word: _indexes})
            else:
                word_index.update({word: set(str(index))})

    for key,value in word_index.items():
        indexes.append({'name': key, 'type': 'word', 'index': ",".join([index for index in value])})

    return indexes

if __name__ == '__main__':
    name = 'baidu_shici'
    indexes = gen_index('data/%s.csv' % name)
    index_df = pd.DataFrame(indexes)
    index_df.to_csv('data/%s_index.csv' % name, encoding='utf-8', sep='|')
    # engine = create_engine('sqlite:///shici.db')
    # index_df.to_sql('baidu_shici_index', if_exists='replace',con=engine)