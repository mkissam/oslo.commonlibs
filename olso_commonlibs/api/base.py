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

from wsme import types as wtypes


class APIBase(wtypes.Base):

    id = int
    """This is a unique identifier used as a primary key in all Database
    models.
    """

    @classmethod
    def from_db_model(cls, db_model, skip_fields=None):
        """Returns the object from a given database representation."""

        skip_fields = skip_fields or []

        if db_model is None:
            return {}

        data = dict((k, v) for k, v in db_model.as_dict().items()
                    if k not in skip_fields)
        return cls(**data)

    def as_dict(self, omit_unset=False):
        """Converts this object into dictionary."""
        attribute_names = [a.name for a in self._wsme_attributes]

        if omit_unset:
            attribute_names = [n for n in attribute_names
                               if getattr(self, n) != wtypes.Unset]

        values = dict((name, self._lookup(name)) for name in attribute_names)

        # TODO(Refactor as a recursive function)

        return values

    def _lookup(self, key):
        """Looks up a key, translating WSME's Unset into Python's None.

        :return: value of the given attribute; None if it is not set
        """
        value = getattr(self, key)
        if value == wtypes.Unset:
            value = None
        return value
