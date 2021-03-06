# -*- coding: utf-8 -*-

# Copyright (C) 2005 Osmo Salomaa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import gaupol

from gi.repository import Gtk


class _TestPositionShiftDialog(gaupol.TestCase):

    def run_dialog(self):
        self.dialog.run()
        self.dialog.destroy()

    def setup_method(self, method):
        raise NotImplementedError

    def test__on_response(self):
        self.dialog._current_radio.set_active(True)
        self.dialog._amount_spin.spin(Gtk.SpinType.STEP_FORWARD, 1)
        self.dialog.response(Gtk.ResponseType.OK)


class TestFrameShiftDialog(_TestPositionShiftDialog):

    def setup_method(self, method):
        self.application = self.new_application()
        self.dialog = gaupol.FrameShiftDialog(
            self.application.window, self.application)
        self.dialog.show()


class TestTimeShiftDialog(_TestPositionShiftDialog):

    def setup_method(self, method):
        self.application = self.new_application()
        self.dialog = gaupol.TimeShiftDialog(
            self.application.window, self.application)
        self.dialog.show()
