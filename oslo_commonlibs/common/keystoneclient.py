# Copyright 2010-2011 OpenStack Foundation
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

from keystoneclient.v3 import client
# from unittest import mock


def createKeystoneClientInstance(session):
    return client.Client(session=session)


# class FakeBaseClient:
#
#     def __init__(self):
#         print("FakeBaseClient.__init__()")
#
#     def request(self):
#         return {'response': True, 'isFake': True}
#
#
# def createFakeClientInstance():
#     return FakeBaseClient()


# class BaseClientTest():
#
#     def test_baseClient(self):
#         print("\ntest_baseClient():")
#         # TypeError: request() missing 2 required positional arguments:
#         # 'url' and 'method'
#         c = createKeystoneClientInstance(None)
#         print(c)
#         response = c.request()
#         print(response)
#
#     @mock.patch('__main__.createKeystoneClientInstance',
#                 side_effect=createFakeClientInstance)
#     def test_fakeBaseClient(self, create_function):
#         print("\ntest_fakeBaseClient():")
#         # TypeError: request() missing 2 required positional arguments:
#         # 'url' and 'method'
#         c = createKeystoneClientInstance(None)
#         print(c)
#         response = c.request()
#         print(response)
#
#
# test = BaseClientTest()
# test.test_baseClient()
# test.test_fakeBaseClient()
