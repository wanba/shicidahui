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
from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger

from shici.api.recognition_resource import RecognitionApi
from shici.api.recommand_resource import RecommandApi, SearchApi
from shici.api.stats_resource import StatsApi
from shici.service.recognition import Recognition
from shici.service.recommand import Recommand
from shici.utils import config


app = Flask(__name__)
config_info = config.user_config()
app.config['UPLOAD_FOLDER'] = config.shici_file_path

app.recommand = Recommand(config_info)
app.recognition = Recognition(config_info)
api = swagger.docs(Api(app), apiVersion='1.0')

# urls
api.add_resource(StatsApi, '/stats')
api.add_resource(RecommandApi, '/shici/recommand')
api.add_resource(SearchApi, '/shici/search')
api.add_resource(RecognitionApi, '/shici/recognize')
port = config_info['api']['port']

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)