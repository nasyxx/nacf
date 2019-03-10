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
filename : tools.py
project  : nacf
license  : LGPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
from inspect import Parameter, Signature, signature

# Prelude
from nalude import flatten

# Local Packages
from .types import Url, Func, Optional


def format_url(url: Optional[Url]) -> Optional[Url]:
    """Add schema to url."""
    return (
        url if url and url.startswith("http") else url and ("https://" + url)
    )


def generate_sig(func: Func, *params: Parameter) -> Signature:
    """Generate signature with param from func."""
    return signature(func).replace(
        parameters=list(signature(func).parameters.values()) + list(params)
    )


__all__ = ["format_url", "flatten"]
