# Copyright (c) 2013 Akshit Khurana - axitkhurana@gmail.com
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA.

from urlparse import urlparse

import settings
from helpers import url_for

from grestful.object import Object
from grestful.helpers import param_upload
from grestful.decorators import (asynchronous, check_is_created,
                                 check_is_not_created)


class Project(Object):
    def __init__(self):
        Object.__init__(self)
        settings.path['project'] = 'projects/'
        settings.path['profile'] = 'profile/'

    @asynchronous
    @check_is_not_created
    def create(self, profile_id, title, description, project_file, screenshot):
        profile_url = url_for('profile', profile_id, False)
        user = urlparse(profile_url).path
        params = [
            ('user', user),
            ('title', title),
            ('desc', description),
        ]

        project_url = url_for('project')
        files = [param_upload('src', project_file),
                 param_upload('screenshot', screenshot)]

        self._post(project_url, params, files)

    @asynchronous
    @check_is_created
    def list(self, profile_id):
        profile_url = url_for('profile', profile_id)
        # extract projects from profile dict
        self._get(profile_url)

    @asynchronous
    @check_is_created
    def download(self, project_id):
        project_url = url_for('project', project_id)
        self._get(project_url)
