# This file is part of gkraken.
#
# Copyright (c) 2018 Roberto Leinardi
#
# gsi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gsi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gsi.  If not, see <http://www.gnu.org/licenses/>.
from typing import Optional


class Status:
    def __init__(self,
                 liquid_temperature: float,
                 fan_rpm: int,
                 pump_rpm: int,
                 firmware_version: str
                 ) -> None:
        self.liquid_temperature: float = liquid_temperature
        self.fan_rpm: int = fan_rpm
        self.fan_duty: Optional[float] = None
        self.pump_rpm: int = pump_rpm
        self.firmware_version: str = firmware_version
