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
import logging

from injector import singleton, inject

from gkraken.interactor import _run_and_get_stdout

_LOG = logging.getLogger(__name__)
_UDEV_RULE = 'SUBSYSTEMS=="usb", ATTRS{idVendor}=="1e71", ATTRS{idProduct}=="170e", MODE="0666"'
_UDEV_RULE_FILE_PATH = '/lib/udev/rules.d/60-gkraken.rules'
_UDEV_RULE_RELOAD_COMMANDS = 'udevadm control --reload-rules ' \
                             '&& udevadm trigger --subsystem-match=usb --attr-match=idVendor=1e71 --action=add'


@singleton
class UdevInteractor:
    @inject
    def __init__(self) -> None:
        pass

    @staticmethod
    def add_udev_rule() -> int:
        cmd = ['pkexec',
               'sh',
               '-c',
               f'echo \'{_UDEV_RULE}\' > {_UDEV_RULE_FILE_PATH} && {_UDEV_RULE_RELOAD_COMMANDS}']
        result = _run_and_get_stdout(cmd)
        if result[0] != 0:
            _LOG.warning(f"Error while creating rule file. Exit code: {result[0]}. {result[1]}")
        return result[0]

    @staticmethod
    def remove_udev_rule() -> int:
        cmd = ['pkexec',
               'sh',
               '-c',
               f'rm {_UDEV_RULE_FILE_PATH} && {_UDEV_RULE_RELOAD_COMMANDS}']
        result = _run_and_get_stdout(cmd)
        if result[0] != 0:
            _LOG.warning(f"Error while removing rule file. Exit code: {result[0]}. {result[1]}")
        return result[0]
