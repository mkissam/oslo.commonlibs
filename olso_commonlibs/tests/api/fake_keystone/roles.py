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
from api_services_common.tests.api.fake_keystone.resources import (
    RoleAssignment)


class RoleManager(object):

    def get(self, name_or_id):
        for role in mock_ks_data.mock_roles:
            if name_or_id == role.name or name_or_id == role.id:
                return dict(role)

    def grant(self, role, user, **kwargs):
        r, u = None, None
        for i in mock_ks_data.mock_roles:
            if role == i.name:
                r = i
                break
        for i in mock_ks_data.mock_users:
            if user == i.name:
                u = i
                break
        if r is None or u is None:
            return 0
        roleAssingment = RoleAssignment(r.id, u.id)
        mock_ks_data.mock_role_assignments.append(roleAssingment)
        return dict(roleAssingment)
