# Copyright 2013 Hewlett-Packard Development Company, L.P.
# Copyright 2013 Thierry Carrez <thierry@openstack.org>
# Copyright 2015 Marton Kiss <marton.kiss@gmail.com>
# Copyright 2021 EagleSoft Bt.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
SQLAlchemy Models for storing database objects
"""

from oslo_db.sqlalchemy import models
from sqlalchemy import Column
from sqlalchemy.ext import declarative
from sqlalchemy import Integer


class IdMixin(object):
    id = Column(Integer, primary_key=True)


class DbBase(models.TimestampMixin,
             IdMixin,
             models.ModelBase):
    metadata = None

    @declarative.declared_attr
    def __tablename__(cls):
        # NOTE(jkoelker) use the pluralized name of the class as the table
        return cls.__name__.lower() + 's'

    def as_dict(self):
        d = {}
        for c in self.__table__.columns:
            d[c.name] = self[c.name]
        return d


Base = declarative.declarative_base(cls=DbBase)


class ModelBuilder(object):
    def __init__(self, **kwargs):
        super(ModelBuilder, self).__init__()

        if kwargs:
            for key in kwargs:
                if key in self:
                    self[key] = kwargs[key]