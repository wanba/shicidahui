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

import pyttsx3 as pyttsx

engine = pyttsx.init()
voices = engine.getProperty('voices')
# voices = ['com.apple.speech.synthesis.voice.mei-jia',
# 'com.apple.speech.synthesis.voice.sin-ji.premium',
# 'com.apple.speech.synthesis.voice.ting-ting'];

for voice in voices:
    print(voice)
    engine.setProperty('voice', voice)
    # engine.say('将进酒; 唐 李白; - ;君不见，黄河之水天上来，奔流到海不复回。君不见，高堂明镜悲白发，朝如青丝暮成雪。人生得意须尽欢，莫使金樽空对月。天生我材必有用，千金散尽还复来。烹羊宰牛且为乐，会须一饮三百杯。岑夫子，丹丘生，将进酒，杯莫停。与君歌一曲，请君为我倾耳听。钟鼓馔玉不足贵，但愿长醉不复醒。古来圣贤皆寂寞，惟有饮者留其名。陈王昔时宴平乐，斗酒十千恣欢谑。主人何为言少钱，径须沽取对君酌。五花马，千金裘，呼儿将出换美酒，与尔同销万古愁。')
    engine.say('In Mac OS，there are all chinese voice，choose one your want.')

    engine.runAndWait()
# 朗读一次
engine.endLoop()