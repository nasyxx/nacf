#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
filename : types.py
project  : nacf
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
from typing import (
    IO,
    Dict,
    List,
    Tuple,
    Union,
    TypeVar,
    Callable,
    Iterable,
    Optional,
    ByteString,
    overload,
)

# Web Packages
from requests_html import Element as Ele
from requests_html import HTMLResponse as Res

# Normal
a = TypeVar("a")
b = TypeVar("b")

# function
RT = TypeVar("RT")
Func = Callable[..., RT]

Reses = Iterable[Res]
RFunc = Callable[..., Union[Res, Reses]]

Eles = Iterable[Ele]
EFunc = Callable[..., Union[Ele, Eles]]

SFunc = Callable[..., Union[str, Iterable[str], None]]

# request
Data = Optional[Union[Dict[str, a], ByteString, IO]]
Json = Dict[str, a]
Url = str
Urls = List[Url]

__all__ = [
    "Res",
    "Reses",
    "a",
    "b",
    "RT",
    "Func",
    "RFunc",
    "SFunc",
    "Data",
    "Json",
    "Url",
    "Urls",
]
