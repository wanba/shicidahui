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

from shici.data.shici import ShiCi
from shici.utils import config

class ShiciTest(unittest.TestCase):
    def setUp(self):
        config_info = config.user_config()
        self.shici = ShiCi(config_info)

    def test_get_by_id(self):
        shici_item = self.shici.get(1)
        print(shici_item)
        self.assertFalse(shici_item.empty)

    def test_get_all(self):
        shici_all = self.shici.getall()
        print(shici_all.head(5))
        self.assertFalse(shici_all.empty)