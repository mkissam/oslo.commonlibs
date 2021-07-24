# Copyright 2010 Jacob Kaplan-Moss
# Copyright 2011 OpenStack Foundation
# Copyright 2013 OpenStack Foundation
# All Rights Reserved.
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

class Project(object):
    id_counter = 0

    def __init__(self, name, **kwargs):
        self.name = name
        self.domain_id = kwargs.get('domain_id', 'default')

        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            Project.id_counter += 1
            self.id = Project.id_counter

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'domain_id', self.domain_id


class RoleAssignment(object):

    def __init__(self, role, user, **kwargs):
        self.role = role
        self.user = user
        self.project = kwargs.get('project', None)
        self.domain = kwargs.get('domain', 'default')

    def __iter__(self):
        yield 'role', self.role
        yield 'user', self.user
        yield 'project', self.project
        yield 'domain', self.domain


class Role(object):
    id_counter = 0

    def __init__(self, name, **kwargs):
        self.name = name
        self.domain_id = kwargs.get('domain_id', 'default')

        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            Role.id_counter += 1
            self.id = Role.id_counter

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'domain_id', self.domain_id


class User(object):
    id_counter = 0

    def __init__(self, name, **kwargs):
        self.name = name

        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            User.id_counter += 1
            self.id = User.id_counter

        self.email = kwargs.get('email', None)
        self.domain_id = kwargs.get('domain_id', 'default')
        self.default_project_id = kwargs.get('default_project_id', None)
        self.enabled = kwargs.get('enabled', False)
        self.password = kwargs.get('password', None)

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'email', self.email
        yield 'domain_id', self.domain_id
        yield 'default_project_id', self.default_project_id
        yield 'enabled', self.enabled
