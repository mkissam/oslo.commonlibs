# Copyright 2021 EagleSoft Bt.

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from api_services_common.tests.api.fake_keystone import mock_ks_data
from api_services_common.tests.api.fake_keystone.resources import User


class UserManager(object):

    def get(self, name_or_id):
        for user in mock_ks_data.mock_users:
            if name_or_id == user.name or name_or_id == user.id:
                return dict(user)

    def create(self, name, **kwargs):
        user = User(name, **kwargs)
        mock_ks_data.mock_users.append(user)
        return dict(user)

    def update(self, user_id, name=None, email=None, password=None,
               enabled=None):
        for user in mock_ks_data.mock_users:
            if user_id == user.id:
                user.name = name or user.name
                user.email = email or user.email
                user.password = password or user.password
                user.enabled = enabled or user.enabled
                return dict(user)

    def delete(self, id_or_obj):
        for user in mock_ks_data.mock_users:
            if id_or_obj == user.id or id_or_obj == user:
                mock_ks_data.mock_users.remove(user)
                return 204
