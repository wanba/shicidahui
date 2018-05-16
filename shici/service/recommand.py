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
from random import randint

import pandas as pd

from shici.data.shici import ShiCi


class Recommand:
    def __init__(self,config_info):
        self.shici = ShiCi(config_info)

    def recommand(self, uid):
        """
        更加用户进行诗词推荐
        :param uid:
        :return:
        """
        all_shici = self.shici.getall()
        if not all_shici.empty:
            id = randint(1, len(all_shici))
            recommand_item = all_shici.loc[all_shici['id']==id, :]
            return recommand_item
        else:
            return pd.DataFrame()

    def search(self, keys):
        """
        根据关键字搜索诗词内容
        :param keys: '_' 分割的多个关键字
        :return:
        """
        all_shici = self.shici.getall()
        if not all_shici.empty:
            select_shici = pd.DataFrame()
            for key in keys:
                filter_shici = all_shici.loc[all_shici['content'].str.contains(key), :]
                if not filter_shici.empty:
                    filter_shici.loc[:, 'key'] = key
                    select_shici = select_shici.append(filter_shici)
            return select_shici
        else:
            return pd.DataFrame()
