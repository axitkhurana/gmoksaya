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

from urllib import urlencode
from urlparse import urljoin


class Settings:
    paths = {}
    base_url = "http://127.0.0.1:8000/api/v1/"

    @classmethod
    def set_path(self, resource, path):
        self.paths[resource] = path

    @classmethod
    def set_credentials(self, credentials):
        ''' set_credentials sets credentials like api_key or username
        to be passed as GET params with the URL

        :param: credentials
        :type: dict
        '''
        self.credentials = credentials

    @classmethod
    def get_credentials(self):
        return self.credentials

    @classmethod
    def get_url(self, resource, resource_path='',
                add_credentials=True):
        if add_credentials:
            params = urlencode(self.credentials)
        else:
            params = ''

        path = '{0}{1}?{2}'.format(self.paths[resource], resource_path, params)
        return urljoin(self.base_url, path)
