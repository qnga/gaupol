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

"""
Names and codes for locales and conversions between them.

Locale codes are of form ``aa[_BB][@Cccc]``, where ``aa`` is a language code,
``BB`` a country code and ``Cccc`` a script. See :mod:`aeidon.languages`,
:mod:`aeidon.countries` and :mod:`aeidon.scripts` for the details.
"""

import aeidon
import os

from aeidon.i18n import _


def code_to_country(code):
    """
    Convert locale `code` to localized country name or ``None``.

    Raise :exc:`LookupError` if `code` not found.
    """
    if len(code) < 5: return None
    return aeidon.countries.code_to_name(code[-2:])

def code_to_language(code):
    """
    Convert locale `code` to localized language name.

    Raise :exc:`LookupError` if `code` not found.
    """
    return aeidon.languages.code_to_name(code[:2])

def code_to_name(code):
    """
    Convert locale `code` to localized name.

    Raise :exc:`LookupError` if `code` not found.
    Return localized ``LANGUAGE (COUNTRY)``.
    """
    language = code_to_language(code)
    country = code_to_country(code)
    if country is None: return language
    return _("{language} ({country})").format(**locals())

@aeidon.deco.once
def get_system_code():
    """Return the locale code preferred by system or ``None``."""
    import locale
    language, encoding = locale.getdefaultlocale()
    return language

@aeidon.deco.once
def get_system_modifier():
    """Return the script modifier of system or ``None``."""
    for name in ("LANGUAGE", "LC_ALL", "LC_MESSAGES", "LANG"):
        value = os.environ.get(name, None)
        if value is not None and value.count("@") == 1:
            i = value.index("@")
            return value[i+1:i+5]
    return None
