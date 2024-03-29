# -*- coding: utf-8 -*-

# Copyright 2010-2011 OpenStack Foundation
#
# Copyright 2021 EagleSoft Bt.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import functools

from pecan import abort

from oslo_commonlibs.common import exception


def db_exceptions(func):
    @functools.wraps(func)
    def decorate(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except exception.DBException as db_exc:
            abort(db_exc.code, db_exc.message)
    return decorate
