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
import unittest
import wave

from shici.service.recognition import Recognition
from shici.utils import config

class RecognitionTest(unittest.TestCase):
    def setUp(self):
        config_info = config.user_config()
        self.recognition = Recognition(config_info)

    def test_recognition(self):
        file_path = os.path.dirname(__file__)
        wave_file = os.path.join(file_path, '01.wav')
        result = self.recognition.recognize(wave_file)
        print(result)