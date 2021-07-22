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

_FATAL_EXCEPTION_FORMAT_ERRORS = False


class APICommonException(Exception):
    """Base APICommon Exception

    To correctly use this class, inherit from it and define
    a 'message' property. That message will get printf'd
    with the keyword arguments provided to the constructor.
    """

    message = "An unknown exception occurred"

    def __init__(self, message_arg=None, *args, **kwargs):
        if not message_arg:
            message_arg = self.message
        try:
            self.message = message_arg % kwargs
        except Exception as e:
            if _FATAL_EXCEPTION_FORMAT_ERRORS:
                raise e
            else:
                # at least get the core message out if something happened
                pass
        super(APICommonException, self).__init__(self.message)


class APICommonHTTPException(APICommonException):
    """Base APICommon Exception to handle HTTP responses
    To correctly use this class, inherit from it and define the following
    properties:
    - message: The message that will be displayed in the server log.
    - client_message: The message that will actually be outputted to the
                      client.
    - status_code: The HTTP status code that should be returned.
                   The default status code is 500.
    """

    client_message = "failure seen - please contact site administrator."
    status_code = 500

    def __init__(self, message_arg=None, client_message=None, *args, **kwargs):
        if not client_message:
            client_message = self.client_message
        try:
            self.client_message = client_message % kwargs
        except Exception as e:
            if _FATAL_EXCEPTION_FORMAT_ERRORS:
                raise e
            else:
                # at least get the core message out if something happened
                pass
        super(APICommonHTTPException, self).__init__(
            message_arg, self.client_message, *args, **kwargs)


class ColumnError(APICommonException):
    message = "No column or an invalid column is found."


class NotFound(APICommonException):
    message = "Object not found"

    def __init__(self, message=None):
        super(NotFound, self).__init__(message, 404)


class DBDeadlock(APICommonException):
    message = """Database dead lock error.
    Two or more different database
    sessions have some data locked, and each database session requests a lock
    on the data that another, different, session has already locked.
    """

    def __init__(self, message=None):
        super(DBDeadlock, self).__init__(message)


class DBException(APICommonException):
    # Base exception for database errors

    message = "Database Exception"

    def __init__(self, message=None, status_code=None):
        """Constructor for base exception class

        :param: message: exception message.
        :param: status_code: code of exception.
        """

        if not status_code:
            status_code = 400

        super(DBException, self).__init__(message=message,
                                          status_code=status_code)


class DBDuplicateEntry(DBException):
    """Duplicate entry exception

    This exception wraps the same exception from database.
    """

    message = "Database object already exists."

    def __init__(self, message=None, object_name=None, value=None,
                 status_code=None):
        """Constructor for duplicate entry exception

        :param : message: This message will be shown after exception raised.
        :param : object_name: This parameter is name of object, in which
        exception was raised.
        :param: value: Invalid value.
        :param: status_code: code of exception.

        If object_name or value is not 'None', to message will be appended with
        new message with information about object name or invalid value
        """

        super(DBDuplicateEntry, self).__init__(message=message,
                                               status_code=status_code)
        db_message = None

        if object_name or value:
            db_message_list = ["Database object"]

            if object_name:
                db_message_list.append(f"\'{object_name}\'")

            if value:
                db_message_list.append(f"with field value \'{value}\'")
            else:
                db_message_list.append("with some of unique fields")

            db_message_list.append("already exists.")
            db_message = " ".join(db_message_list)

        if db_message:
            message_list = []

            if message:
                message_list.append(message)

            message_list.append(db_message)
            self.msg = " ".join(message_list)


class DBConnectionError(DBException):
    """Connection error exception

    This exception wraps the same exception from database.
    """

    message = "Connection to database failed."


class DBDeadLock(DBException):
    """Deadlock exception

    This exception wraps the same exception from database.
    """

    message = "Database in dead lock"


class DBInvalidUnicodeParameter(DBException):
    """Invalid unicode parameter exception

    This exception wraps the same exception from database.
    """

    message = """Unicode parameter is passed to
                 a database without encoding directive"""


class DBMigrationError(DBException):
    """Migration error exception

    This exception wraps the same exception from database.
    """

    message = "migrations could not be completed successfully"


class DBReferenceError(DBException):
    """Reference error exception

    This exception wraps the same exception from database.
    """

    message = "Foreign key error."

    def __init__(self, message=None, object_name=None, value=None,
                 key=None, status_code=None):
        """Constructor for duplicate entry exception

        :param : message: This message will be shown after exception raised.
        :param : object_name: This parameter is name of object, in which
        exception was raised.
        :param: value: Invalid value.
        :param : key: Field with invalid value.
        :param : status_code: code of exception.

        If object_name or value or key is not 'None', to message will be
        appended with new message with information about object name or
        invalid value or field with invalid value.
        """

        super(DBReferenceError, self).__init__(message=message,
                                               status_code=status_code)
        db_message = None

        if object_name or value or key:
            db_message_list = []

            if object_name:
                db_message_list.append("Error in object")
                db_message_list.append(f"\'{object_name}\'.")

            if value or key:
                db_message_list.append("Field")

                if key:
                    db_message_list.append(f"\'{key}\'")

                if value:
                    db_message_list.append("value")
                    db_message_list.append(f"\'{value}\'")

                db_message_list.append("is invalid.")

            db_message = " ".join(db_message_list)

        if db_message:
            message_list = []

            if message:
                message_list.append(message)
            else:
                message_list.append(self.message)

            message_list.append(db_message)
            self.msg = " ".join(message_list)


class DBInvalidSortKey(DBException):
    """Invalid sortkey error exception

    This exception wraps the same exception from database.
    """

    message = "Invalid sort field"


class DBValueError(DBException):
    """Value error exception

    This exception wraps standard ValueError exception.
    """

    message = "Unknown value."


class InvalidObject(APICommonHTTPException):
    status_code = 400

    def __init__(self, *args, **kwargs):
        self.invalid_property = kwargs.get('property')
        self.message = "Failed to validate JSON information: "
        self.client_message = ("Provided object does not match",
                               "schema '{schema}':".format(*args),
                               "{reason}".format(**kwargs))
        self.message = self.message + self.client_message
        super(InvalidObject, self).__init__(*args, **kwargs)
