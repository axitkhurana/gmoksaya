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

import sys

from gi.repository import GObject

sys.path.append("..")
from gmoksaya import users, settings


def __phase1_failed_cb(user, info):
    print '[FAILED] phase1: with %s' % str(info)
    loop.quit()


def __phase1_completed_cb(user, info):
    print '[OK] phase1: with %s' % str(info)
    loop.quit()

settings.credentials['username'] = 'moksaya_username'
settings.credentials['api_key'] = 'moksaya_api_key'

user = users.User()
user.connect('completed', __phase1_completed_cb)
user.connect('failed', __phase1_failed_cb)
user.info('test_user')

loop = GObject.MainLoop()
loop.run()
