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
import wave
import os
from aip import AipSpeech

class Recognition:
    def __init__(self, config_info):
        self.baidu = config_info['baidu']
        self.speech = AipSpeech(self.baidu['appId'], self.baidu['apiKey'], self.baidu['secretKey'])

    def get_wave_file(self, wave_file):
        if os.path.exists(wave_file):
            fp=wave.open(wave_file,'rb')
            nf = fp.getnframes()  # 获取文件的采样点数量
            print('sampwidth:', fp.getsampwidth(), 'framerate:', fp.getframerate(), 'channels:', fp.getnchannels())
            f_len = nf * fp._sampwidth  # 文件长度计算，每个采样2个字节
            audio_data = fp.readframes(nf)
            frame_rate = fp._framerate
            return (audio_data, frame_rate, f_len)
        else:
            raise FileNotFoundError

    def recognize(self, audio_file):
        # 格式支持：pcm（不压缩）、wav（不压缩，pcm编码）、amr（压缩格式）。
        # 推荐pcm 采样率 ：16000 固定值。 编码：16bit 位深的单声道。
        # 百度服务端会将非pcm格式，转为pcm格式，因此使用wav、amr会有额外的转换耗时。
        (wave_content, frame_rate, len) = self.get_wave_file(audio_file)
        result = self.speech.asr(wave_content, 'pcm', frame_rate, {'lan': 'zh'})
        return result
