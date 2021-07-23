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

from api_services_common.tests.api.fake_keystone import projects
from api_services_common.tests.api.fake_keystone import roles
from api_services_common.tests.api.fake_keystone import users


class Client(object):

    def __init__(self, **kwargs):
        self.projects = projects.ProjectManager()
        self.roles = roles.RoleManager()
        self.users = users.UserManager()
