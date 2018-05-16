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
from qfund.utils import config
import pandas as pd


def response_csv(results, method, security, csv=False):
    """
    将results 中的dataframe 或 series 序列号到csv
    :param results:
    :param method:
    :param security:
    :return:
    """
    if csv:
        # csv path
        security_path = os.path.join(os.path.expanduser(config.qfund_report_path), security)
        if not os.path.exists(security_path):
            os.mkdir(security_path)
        csv_security_path = os.path.join(security_path, 'csv')
        if not os.path.exists(csv_security_path):
            os.mkdir(csv_security_path)

    # to response
    if isinstance(results, dict):
        for key, value in results.items():
            if isinstance(value, pd.DataFrame):
                results[key] = value.to_dict(orient='records')
                if csv:
                    filename = os.path.join(csv_security_path, '%s_%s.csv' % (method, key))
                    value.to_csv(filename)
            elif isinstance(value, pd.Series):
                results[key] = value.to_dict()
                if csv:
                    filename = os.path.join(csv_security_path, '%s_%s.csv' % (method, key))
                    value.to_csv(filename)
    elif isinstance(results, pd.DataFrame):
        # dataframe or series direct to csv
        if csv:
            filename = os.path.join(csv_security_path, '%s.csv' % (method))
            results.to_csv(filename)
        results = results.to_dict(orient='records')
    elif isinstance(results, pd.Series):
        if csv:
            filename = os.path.join(csv_security_path, '%s.csv' % (method))
            results.to_csv(filename)
        results = results.to_dict()
    return results