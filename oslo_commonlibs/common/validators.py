#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""
API JSON validator base.
"""

import abc
import jsonschema as schema

from oslo_commonlibs.common import exception


def get_invalid_property(validation_error):
    # we are interested in the second item which is the failed propertyName.
    if validation_error.schema_path and len(validation_error.schema_path) > 1:
        return validation_error.schema_path[1]


class ValidatorBase(object, metaclass=abc.ABCMeta):
    """Base class for validators."""

    name = ''

    @abc.abstractmethod
    def validate(self, json_data, parent_schema=None):
        """Validate the input JSON.

        :param json_data: JSON to validate against this class' internal schema.
        :param parent_schema: Name of the parent schema to this schema.
        :returns: dict -- JSON content, post-validation and
        :                 normalization/defaulting.
        :raises: schema.ValidationError on schema violations.
        """

    def _full_name(self, parent_schema=None):
        """Validator schema name accessor

        Returns the full schema name for this validator,
        including parent name.
        """
        schema_name = self.name
        if parent_schema:
            schema_name = _(
                "{schema_name}' within '{parent_schema_name}").format(
                    schema_name=self.name,
                    parent_schema_name=parent_schema)
        return schema_name

    def _assert_schema_is_valid(self, json_data, schema_name):
        """Assert that the JSON structure is valid for the given schema.

        :raises: InvalidObject exception if the data is not schema compliant.
        """
        try:
            schema.validate(json_data, self.schema)
        except schema.ValidationError as e:
            if e.validator == "pattern":
                e.message = e.schema_path[1]
            raise exception.InvalidObject(schema=schema_name,
                                          reason=e.message,
                                          property=get_invalid_property(e))

    def _assert_validity(self, valid_condition, schema_name, message,
                         property):
        """Assert that a certain condition is met.

        :raises: InvalidObject exception if the condition is not met.
        """
        if not valid_condition:
            raise exception.InvalidObject(schema=schema_name, reason=message,
                                          property=property)