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
from flask_restful import Resource, reqparse
from flask import current_app
from flask_restful_swagger import swagger


class RecommandApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("uid", type=str, required=False)

    """
    为用户推荐一首诗
    """
    @swagger.operation(
        notes='get recommand shici for user',
        parameters=[
            {
                "name": "uid",
                "description": "uid, 不指定是返回全局推荐, 根据日期进行推荐",
                "required": False,
                "type": "string",
                "default": 'unknown'
            },
        ],
        responseMessages=[
        ]
    )
    def get(self):
        args = self.parser.parse_args()
        uid = args['uid']

        results = current_app.recommand.recommand(uid)
        return results.to_dict(orient='records')


class SearchApi(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("keys", type=str, required=True)

    """
    根据关键字搜索
    """
    @swagger.operation(
        notes='search shici by keys',
        parameters=[
            {
                "name": "keys",
                "description": "keys支持多个关键字(或), eg: 春_石",
                "required": False,
                "type": "string"
            },
        ],
        responseMessages=[
        ]
    )
    def get(self):
        """
        key 支持多个关键字以'_'分割
        :param key:
        :return:
        """

        args = self.parser.parse_args()
        keys = args['keys']
        keys_array = keys.split('_')
        results = current_app.recommand.search(keys_array)
        return results.to_dict(orient='records')
