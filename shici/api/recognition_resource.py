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
import os

import werkzeug
from flask import current_app
from flask_restful import Resource, reqparse
from flask_restful_swagger import swagger


class RecognitionApi(Resource):
    ALLOWED_EXTENSIONS = set(['wav'])

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')
        self.parser.add_argument('uid',type=str, required=True)
        self.parser.add_argument('fname',type=str, required=False)

    """
    为用户推荐一首诗
    """
    @swagger.operation(
        notes='上传语音文件, 诗词识别',
        parameters=[
            {
                "name": "uid",
                "description": "uid, 文件名",
                "required": True,
                "type": "string",
                "default": "unknown"
            },
            {
                "name": "fname",
                "description": "fname, 文件名",
                "required": False,
                "type": "string"
            },
        ],
        responseMessages=[
        ]
    )
    def post(self):
        args = self.parser.parse_args()
        wave_file = args['file']
        fname = args['fname']
        uid = args['uid']

        if wave_file:
            extension = wave_file.filename.split('.')[-1]
            if not extension in self.ALLOWED_EXTENSIONS:
                return {'message':'file type %s not suported.' % extension, 'status':'error'}
            # 文件存储
            security_path = os.path.expanduser(os.path.join(current_app.config['UPLOAD_FOLDER'], uid))
            if not os.path.exists(os.path.expanduser(security_path)):
                os.mkdir(os.path.expanduser(security_path))

            if fname:
                fullpath = os.path.join(security_path, fname)
            else:
                fullpath = os.path.join(security_path, wave_file.filename)
            wave_file.save(fullpath)

            # 语音识别
            result = current_app.recognition.recognize(fullpath)
            return result
        else:
            return {'message':'not upload file content', 'status':'error'}