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
license  : LGPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""

# Standard Library
import unittest

# Prelude
from nalude import flatten

# Other Packages
from nacf import (css, get, gets, html, json, post, text,
                  urls, posts, xpath, parallel, __version__,)
from nacf.types import Res, Json, Iterable


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

    def test_get_css(self) -> None:
        """Test get and css."""

        @get("python.org")
        @css(".widget-title", first=True)
        @text
        def crawler(res: str) -> str:
            """Test crawler."""
            return res

        self.assertEqual(crawler(), "Get Started")

    def test_gets_xpath(self) -> None:
        """Test gets and xpath."""

        @gets(["python.org", "python.org"])
        @xpath("//*[@class='widget-title']", first=True)
        @text
        def crawler(res: str) -> str:
            """Test crawler."""
            return res

        self.assertEqual(
            list(flatten(crawler())), ["Get Started", "Get Started"]
        )

    def test_post_json(self) -> None:
        """Test post, posts and json."""

        @post(
            "https://app.fakejson.com/q",
            json={
                "token": "FOk7RjbecxtWJHljGjCNjg",
                "data": {
                    "colorText": "colorText",
                    "colorHex": "colorHex",
                    "colorRGB": "colorRGB",
                    "colorHSL": "colorHSL",
                },
            },
        )
        @json
        def crawler(res: Json) -> Json:
            """Test crawler."""
            return res

        self.assertEqual(
            crawler(),
            {
                "colorText": "tufts blue",
                "colorRGB": "rgb(22, 75, 56)",
                "colorHex": "colorHex",
                "colorHSL": "hsl(233, 14%, 14%)",
            },
        )

    def test_posts(self) -> None:
        """Test posts and json."""

        @posts(
            ["https://app.fakejson.com/q"] * 3,
            jsons=[
                {
                    "token": "FOk7RjbecxtWJHljGjCNjg",
                    "data": {
                        "colorText": "colorText",
                        "colorHex": "colorHex",
                        "colorRGB": "colorRGB",
                        "colorHSL": "colorHSL",
                    },
                }
            ]
            * 3,
        )
        def crawler(res: Res) -> Iterable[Json]:
            """Test crawler."""
            return map(lambda r: r.json(), res)

        self.assertEqual(
            list(flatten(crawler())),
            [
                {
                    "colorText": "tufts blue",
                    "colorRGB": "rgb(22, 75, 56)",
                    "colorHex": "colorHex",
                    "colorHSL": "hsl(233, 14%, 14%)",
                }
            ]
            * 3,
        )

    def test_urls_text(self) -> None:
        """Test urls and text."""

        @urls(["python.org", "python.org"])
        @gets()
        @css(".widget-title", first=True)
        @text
        def crawler(res: str) -> str:
            """Test crawler."""
            return res

        self.assertEqual(
            list(flatten(crawler())), ["Get Started", "Get Started"]
        )

    def test_parallel_html(self) -> None:
        """Test parallel."""

        @urls(["python.org", "python.org"])
        @parallel()
        @get()
        @html
        def crawler(res: Res) -> str:
            """Test crawler."""
            return res.find(".widget-title", first=True).text

        self.assertEqual(
            list(flatten(crawler())), ["Get Started", "Get Started"]
        )


def run() -> None:
    """Run test."""
    unittest.main()


if __name__ == "__main__":
    run()
