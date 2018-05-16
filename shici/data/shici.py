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
from shici.data.datasource import DataSource


class ShiCi(DataSource):
    def __init__(self, config_info):
        DataSource.__init__(self, config_info)

    def getall(self):
        table = 'shici'
        columns = ['id', 'name', 'author', 'content', 'dynasty', 'comment', 'translation', 'created_at', 'updated_at']
        sql = 'select %s from %s' % (",".join(columns), table)
        print(sql)
        all_shici = self.read_sql(sql, self.shici)
        return all_shici

    def get(self, id):
        table = 'shici'
        columns = ['id', 'name', 'author', 'content', 'dynasty', 'comment', 'translation', 'created_at', 'updated_at']
        sql = 'select %s from %s where id=%s' % (",".join(columns), table, id)
        print(sql)
        shici = self.read_sql(sql, self.shici)
        return shici

