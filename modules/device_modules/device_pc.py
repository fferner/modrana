# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# A PC modRana device-specific module.
# This is currently used mainly to make modRana
# development & debugging on the PC easier.
#----------------------------------------------------------------------------
# Copyright 2010, Martin Kolman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#---------------------------------------------------------------------------
from modules.device_modules.base_device_module import DeviceModule
from core.constants import DEVICE_TYPE_DESKTOP

def getModule(*args, **kwargs):
    return DevicePC(*args, **kwargs)


class DevicePC(DeviceModule):
    """A modRana device-specific module for PC"""

    def __init__(self, *args, **kwargs):
        DeviceModule.__init__(self, *args, **kwargs)

    def getDeviceIDString(self):
        return "pc"

    def getDeviceName(self):
        return "A generic Personal Computer"

    def getWinWH(self):
        return 800, 480

    def simpleMapDragging(self):
        return False

    def startInFullscreen(self):
        return False

    def getSupportedGUIModuleIds(self):
        return ["GTK", "QML:indep"]

    def getDeviceType(self):
        return DEVICE_TYPE_DESKTOP
