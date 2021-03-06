# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# A SmartQ 7 modRana device-specific module.
# It is a basic modRana module, that has some special features
# and is loaded only on the correpsponding device.
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
from core.constants import DEVICE_TYPE_TABLET


def getModule(*args, **kwargs):
    return DeviceQ7(*args, **kwargs)


class DeviceQ7(DeviceModule):
    """A SmartQ 7 modRana device-specific module"""

    def __init__(self, *args, **kwargs):
        DeviceModule.__init__(self, *args, **kwargs)

    def getDeviceIDString(self):
        return "q7"

    def getDeviceName(self):
        return "Smart Devices SmartQ 7 MID"

    def getWinWH(self):
        return 800, 480

    def simpleMapDragging(self):
        return True

    def startInFullscreen(self):
        return True

    def getSupportedGUIModuleIds(self):
        return ["GTK"]

    def getDeviceType(self):
        return DEVICE_TYPE_TABLET