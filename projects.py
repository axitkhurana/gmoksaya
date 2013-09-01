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

import json
import urlparse
from settings import Settings

from grestful.object import Object
from grestful.helpers import param_upload


class Project(Object):
    def __init__():
        # TODO Use endpoints returned by API
        # GET request to host/api/v3
        Settings.set_path('project', 'projects/')
        Settings.set_path('profile', 'profile/')

    def create(self, profile_id, title, description, project_file, screenshot):
        profile_url = Settings.get_url('profile', profile_id, False)
        user = urlparse.urlparse(profile_url).path
        params = [
            ('user', user),
            ('title', title),
            ('desc', description),
        ]
        url = Settings.get_url('project')
        files = [param_upload('src', project_file),
                 param_upload('screenshot', screenshot)]
        self._post(url, params, files)

    def list(self, profile_id):
        url = Settings.get_url('profile', profile_id)
        result = json.loads(self._get(url))
        projects = result['projects']
        return projects

    def download(self, project_id):
        url = Settings.get_url('project', project_id)
        result = json.loads(self._get(url))
        return {k: result[k] for k in ('title', 'desc', 'user')}
