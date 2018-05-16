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
import unittest

from shici.service.recommand import Recommand
from shici.utils import config

class RecommandTest(unittest.TestCase):
    def setUp(self):
        config_info = config.user_config()
        self.recommand = Recommand(config_info)

    def test_recommand(self):
        recommand_item = self.recommand.recommand('wangzg')
        print(recommand_item)
        self.assertFalse(recommand_item.empty)

    def test_search(self):
        search_item = self.recommand.search(['朝露待日晞'])
        print(search_item)
        self.assertFalse(search_item.empty)