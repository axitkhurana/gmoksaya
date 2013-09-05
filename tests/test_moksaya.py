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
from gmoksaya import projects, settings


def __phase3_failed_cb(project, info):
    print '[FAILED] phase3: with %s' % str(info)
    loop.quit()


def __phase2_failed_cb(project, info):
    print '[FAILED] phase2: with %s' % str(info)
    loop.quit()


def __phase1_failed_cb(project, info):
    print '[FAILED] phase1: with %s' % str(info)
    loop.quit()


def __phase3_completed_cb(project, info):
    print '[OK] phase3: with %s' % str(info)
    loop.quit()


def __phase2_completed_cb(project, info):
    print '[OK] phase2: with %s' % info['projects']

    project = projects.Project()
    project.connect('completed', __phase3_completed_cb)
    project.connect('failed', __phase3_failed_cb)
    project.download(1)


def __phase1_completed_cb(project, info):
    print '[OK] phase1: with %s' % str(info)

    project = projects.Project()
    project.connect('completed', __phase2_completed_cb)
    project.connect('failed', __phase2_failed_cb)
    project.list(2)

settings.credentials['username'] = 'moksaya_username'
settings.credentials['api_key'] = 'moksaya_api_key'

project = projects.Project()
project.connect('completed', __phase1_completed_cb)
project.connect('failed', __phase1_failed_cb)
project.create(2, 'test_title', 'test_description', 'test_file1',
               'test_file2.jpg')

loop = GObject.MainLoop()
loop.run()
