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
from api_services_common.tests.api.fake_keystone.resources import Project


class ProjectManager(object):

    def create(self, name, **kwargs):
        project = Project(name, **kwargs)
        mock_ks_data.mock_projects.append(project)
        return dict(project)

    def delete(self, id_or_obj):
        for project in mock_ks_data.mock_projects:
            if id_or_obj == project.id or id_or_obj == project:
                mock_ks_data.mock_projects.remove(project)
                return 204
