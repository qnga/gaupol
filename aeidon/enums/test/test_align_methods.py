# -*- coding: utf-8 -*-

# Copyright (C) 2008-2009 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# Gaupol is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# Gaupol. If not, see <http://www.gnu.org/licenses/>.

import aeidon


class TestModule(aeidon.TestCase):

    def test_attributes(self):
        for align_method in aeidon.align_methods:
            assert hasattr(align_method, "label")

    def test_items(self):
        assert hasattr(aeidon.align_methods, "NUMBER")
        assert hasattr(aeidon.align_methods, "POSITION")
