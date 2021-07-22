# Copyright (c) 2013-2014 Rackspace, Inc.
#
# Copyright 2021 EagleSoft Bt.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import mimetypes
from oslo_config import cfg
from oslo_log import log
from oslo_utils import uuidutils
import pecan
from urllib import parse


CONF = cfg.CONF


def _do_allow_certain_content_types(func, content_types_list=[]):
    # Allows you to bypass pecan's content-type restrictions
    cfg = pecan.util._cfg(func)
    cfg.setdefault('content_types', {})
    cfg['content_types'].update((value, '')
                                for value in content_types_list)
    return func


def allow_certain_content_types(*content_types_list):
    def _wrapper(func):
        return _do_allow_certain_content_types(func, content_types_list)
    return _wrapper


def allow_all_content_types(f):
    return _do_allow_certain_content_types(f, mimetypes.types_map.values())


def getLogger(name):
    return log.getLogger(name)


def get_base_url_from_request():
    """Derive base url from wsgi request if CONF.host_href is not set
    Use host.href as base URL if its set in barbican.conf.
    If its not set, then derives value from wsgi request. WSGI request uses
    HOST header or HTTP_X_FORWARDED_FOR header (in case of proxy) for host +
    port part of its url. Proxies can also set HTTP_X_FORWARDED_PROTO header
    for indicating http vs https.
    Some of unit tests does not have pecan context that's why using request
    attr check on pecan instance.
    """
    if not CONF.host_href and hasattr(pecan.request, 'url'):
        p_url = parse.urlsplit(pecan.request.url)
        if p_url.path:
            base_url = '%s://%s%s' % (p_url.scheme, p_url.netloc, p_url.path)
        else:
            base_url = '%s://%s' % (p_url.scheme, p_url.netloc)
        return base_url
    else:  # when host_href is set or flow is not within wsgi request context
        return CONF.host_href


def generate_uuid():
    return uuidutils.generate_uuid()

