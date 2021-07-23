# Copyright 2021 EagleSoft Bt.
#
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


from api_services_common.tests.api.fake_keystone.resources import (
    RoleAssignment)
from api_services_common.tests.api.fake_keystone.resources import Project
from api_services_common.tests.api.fake_keystone.resources import Role
from api_services_common.tests.api.fake_keystone.resources import User


mock_projects = [
    Project('x-project-admin'),
    Project('x-project-member')]


mock_roles = [
    Role('X-Admin-Role'),
    Role('X-Org-Admin-Role'),
    Role('X-Member-Role')]


mock_users = [
    User('testuser0001', id='x-user-id-0001', enabled=True,
         default_project_id='x-project-admin'),
    User('testuser0002', id='x-user-id-0002', enabled=True,
         default_project_id='x-project-member'),
    User('testuser0003', enabled=True, default_project_id='x-project-member')]


mock_role_assignments = [
    RoleAssignment(mock_roles[0].id, mock_users[0].id),
    RoleAssignment(mock_roles[1].id, mock_users[1].id),
    RoleAssignment(mock_roles[2].id, mock_users[2].id)]
