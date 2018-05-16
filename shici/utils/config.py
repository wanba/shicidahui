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
import codecs
import yaml


shici_path = "~/.shici/"
if not os.path.exists(os.path.expanduser(shici_path)):
    os.mkdir(os.path.expanduser(shici_path))

shici_file_path = "~/.shici/storage/"
if not os.path.exists(os.path.expanduser(shici_file_path)):
    os.mkdir(os.path.expanduser(shici_file_path))

config_file = 'config.yml'


def load_yaml(path):
    with codecs.open(path, encoding='utf-8') as f:
        return yaml.load(f)


def load_from_folder(folder, file):
    folder = os.path.expanduser(folder)
    path = os.path.join(folder, file)
    config = load_yaml(path) if os.path.exists(path) else {}

    return config


def user_config():
    return load_from_folder(shici_path, config_file)







