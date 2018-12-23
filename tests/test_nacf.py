#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Life's pathetic, have fun ("▔□▔)/hi~♡ Nasy.

Excited without bugs::

    |             *         *
    |                  .                .
    |           .
    |     *                      ,
    |                   .
    |
    |                               *
    |          |\___/|
    |          )    -(             .              ·
    |         =\ -   /=
    |           )===(       *
    |          /   - \
    |          |-    |
    |         /   -   \     0.|.0
    |  NASY___\__( (__/_____(\=/)__+1s____________
    |  ______|____) )______|______|______|______|_
    |  ___|______( (____|______|______|______|____
    |  ______|____\_|______|______|______|______|_
    |  ___|______|______|______|______|______|____
    |  ______|______|______|______|______|______|_
    |  ___|______|______|______|______|______|____

author   : Nasy https://nasy.moe
date     : Dec 23, 2018
email    : Nasy <nasyxx+python@gmail.com>
filename : test_nacf.py
project  : tests
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""

# Standard Library
import unittest

from nacf import __version__


class NacfTest(unittest.TestCase):
    """Nasy crawler framework test."""

    def test_version(self) -> None:
        """Test version of nacf."""
        with open("pyproject.toml") as f:
            for line in f:
                if "version" in line:
                    version = line.split()[-1].replace('"', "")
                    break
        self.assertEqual(__version__, version)


def run() -> None:
    """Run test."""
    unittest.main()


if __name__ == "__main__":
    run()
