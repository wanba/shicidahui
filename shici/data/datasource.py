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
import pandas as pd
import pymysql
from flask import current_app


class Mysql:
    def __init__(self, database):
        self.host = database['host']
        self.user = database['user']
        self.password = database['password']
        self.database = database['database']
        self.charset = database['charset']

    def open(self):
        """
        建立数据库连接
        :return: conn
        """
        return pymysql.connect(self.host, self.user, self.password, self.database, charset=self.charset)

    @staticmethod
    def close(conn):
        conn.close()


class DataSource:
    def __init__(self, config):
        self.shici = Mysql(config['database']['shici'])

    def read_sql(self, sql, database):
        try:
            conn = database.open()
            sql_df = pd.read_sql(sql, conn)
            if not sql_df.empty:
                return sql_df
            else:
                return pd.DataFrame()
        except Exception as e:
            current_app.logger.warn("read sql error, sql=%s database=%s" % (sql, database))
        finally:
            Mysql.close(conn)

    def execute_sql(self, sql, database):
        try:
            conn = database.open()
            cur = conn.cursor()
            result=cur.execute(sql)
            # 1 success
            return result
        except Exception as e:
            current_app.logger.warn("execute sql error, sql=%s database=%s" % (sql, database))
        finally:
            conn.commit()
            Mysql.close(conn)
