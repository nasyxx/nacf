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
date     : Dec 24, 2018
email    : Nasy <nasyxx+python@gmail.com>
filename : models.py
project  : nacf
license  : GPL-3.0+

There are more things in heaven and earth, Horatio, than are dreamt.
 --  From "Hamlet"
"""
# Standard Library
from inspect import Parameter
from functools import wraps
from itertools import chain, cycle
from multiprocessing.dummy import Pool

# Web Packages
from requests_html import HTMLSession as s

# Local Packages
from .tools import format_url, generate_sig
from .types import (RT, Ele, Res, Url, Data, Eles, Func, Json,
                    List, Urls, EFunc, Reses, RFunc, SFunc, Tuple,
                    Union, Callable, Iterable, Optional, a, b,)


def urls(urls_: Urls, **kwds: a) -> Callable[[Func], Func]:
    """Feed urls to next function."""

    def decorator(func: Func) -> Func:
        """Decorate function func."""

        @wraps(func)
        def wrapper() -> RT:
            """Wrap function func."""
            return func(_urls=urls_, **kwds)

        return wrapper

    return decorator


def parallel(n: Optional[int] = None, **kwds: a) -> Callable[[Func], Func]:
    """Run parallelly."""

    def decorator(func: Func) -> Func:
        """Decorate function func."""

        @wraps(func)
        def wrapper(
            _urls: Urls,
            _datas: Optional[Iterable[Data]] = None,
            _jsons: Optional[Iterable[Json]] = None,
            **_kwds: b,
        ) -> RT:
            """Wrap function func."""

            def runner(udj: Tuple[Url, Optional[Data], Optional[Json]]) -> RT:
                """Run func wrapper."""
                url, data, json = udj
                return (
                    func(url, _data=data, _json=json, **_kwds, **kwds)
                    if data or json
                    else func(url, **_kwds, **kwds)
                )

            with Pool(n) as pool:
                res = pool.map(
                    runner,
                    zip(
                        _urls,
                        _datas or cycle([None]),
                        _jsons or cycle([dict()]),
                    ),
                )
            return res

        setattr(
            wrapper,
            "__signature__",
            generate_sig(
                func,
                Parameter(
                    "_urls",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Urls",
                ),
                Parameter(
                    "_datas",
                    Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation="Optional[Iterable[Data]]",
                ),
                Parameter(
                    "_jsons",
                    Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation="Optional[Iterable[Json]]",
                ),
            ),
        )

        return wrapper

    return decorator


def get(
    url: Optional[Url] = None, *urls: Url, first: bool = False, **kwds: a
) -> Callable[[RFunc], RFunc]:
    """Get url."""

    def decorator(func: RFunc) -> RFunc:
        """Decorate function func."""

        @wraps(func)
        def wrapper(
            _url: Url = None,
            *,
            _urls: Optional[Urls] = None,
            _s: Optional[s] = None,
        ) -> Union[Res, Reses]:
            """Wrap function func."""
            return func(
                (lambda res: first and next(chain(res, (None,))) or res)(
                    map(
                        lambda u: (_s or s()).get(u, **kwds),
                        map(
                            format_url,
                            filter(
                                bool, chain((url,), urls, (_url,), _urls or [])
                            ),
                        ),
                    )
                )
            )

        setattr(
            wrapper,
            "__signature__",
            generate_sig(
                func,
                Parameter(
                    "_url",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Optional[Url]",
                ),
                Parameter(
                    "_urls",
                    Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation="Optional[Urls]",
                ),
                Parameter(
                    "_s",
                    Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation="Optional[HTMLSession]",
                ),
            ),
        )

        return wrapper

    return decorator


def post(
    url: Optional[Url] = None,
    *urls: Url,
    data: Data = None,
    json: Json = None,
    first: bool = False,
    **kwds: a,
) -> Callable[[RFunc], RFunc]:
    """Post url with data and json."""

    def decorator(func: RFunc) -> RFunc:
        """Decorate function func."""

        @wraps(func)
        def wrapper(
            _url: Optional[Url] = None,
            _data: Data = None,
            _json: Json = None,
            *,
            _urls: Optional[Urls] = None,
            _s: Optional[s] = None,
            **_kwds: b,
        ) -> Union[Res, Reses]:
            """Wrap function func."""

            return func(
                (lambda res: first and next(chain(res, (None,))) or res)(
                    map(
                        lambda u: (_s or s()).post(
                            u,
                            data=_data or data,
                            json=_json or json,
                            **kwds,
                            **_kwds,
                        ),
                        map(
                            format_url,
                            filter(
                                bool, chain((url,), urls, (_url,), _urls or [])
                            ),
                        ),
                    )
                )
            )

        setattr(
            wrapper,
            "__signature__",
            generate_sig(
                func,
                Parameter(
                    "_url",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Optional[Url]",
                ),
                Parameter(
                    "_data",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Optional[Data]",
                ),
                Parameter(
                    "_json",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Optional[Json]",
                ),
                Parameter(
                    "_urls",
                    Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation="Optional[Urls]",
                ),
                Parameter(
                    "_s",
                    Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation="Optional[HTMLSession]",
                ),
            ),
        )

        return wrapper

    return decorator


def css(
    selector: str = "*",
    *,
    containing: Union[str, List[str]] = None,
    clean: bool = False,
    first: bool = False,
    _encoding: str = None,
) -> Callable[[EFunc], EFunc]:
    """Css response."""

    def decorator(func: EFunc) -> EFunc:
        """Decorate function func."""

        @wraps(func)
        def wrapper(_res: Union[Res, Reses]) -> Union[Ele, Eles]:
            """Wrap function func."""
            return func(
                (
                    lambda eles: eles
                    if first or isinstance(_res, Res)
                    else chain.from_iterable(eles)
                )(
                    _res.html.find(
                        selector,
                        containing=containing,
                        clean=clean,
                        first=first,
                        _encoding=_encoding,
                    )
                    if isinstance(_res, Res)
                    else map(
                        lambda r: r.html.find(
                            selector,
                            containing=containing,
                            clean=clean,
                            first=first,
                            _encoding=_encoding,
                        ),
                        _res,
                    )
                )
            )

        setattr(
            wrapper,
            "__signature__",
            generate_sig(
                func,
                Parameter(
                    "_res",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Union[Res, Reses]",
                ),
            ),
        )

        return wrapper

    return decorator


def xpath(
    selector: str,
    *,
    clean: bool = False,
    first: bool = False,
    _encoding: str = None,
) -> Callable[[EFunc], EFunc]:
    """Css response."""

    def decorator(func: EFunc) -> EFunc:
        """Decorate function func."""

        @wraps(func)
        def wrapper(_res: Union[Res, Reses]) -> Union[Ele, Eles]:
            """Wrap function func."""
            return func(
                (
                    lambda eles: eles
                    if first or isinstance(_res, Res)
                    else chain.from_iterable(eles)
                )(
                    _res.html.xpath(
                        selector, clean=clean, first=first, _encoding=_encoding
                    )
                    if isinstance(_res, Res)
                    else map(
                        lambda r: r.html.find(
                            selector,
                            clean=clean,
                            first=first,
                            _encoding=_encoding,
                        ),
                        _res,
                    )
                )
            )

        setattr(
            wrapper,
            "__signature__",
            generate_sig(
                func,
                Parameter(
                    "_res",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Union[Res, Reses]",
                ),
            ),
        )

        return wrapper

    return decorator


def text(func: SFunc) -> SFunc:
    """Get text from response of css/xpath."""

    @wraps(func)
    def wrapper(_ele: Union[Ele, Eles]) -> Union[str, Iterable[str], None]:
        """Wrap function func."""
        return func(
            _ele.text if isinstance(_ele, Ele) else map(lambda e: e.text, _ele)
        )

    setattr(
        wrapper,
        "__signature__",
        generate_sig(
            func,
            Parameter(
                "_ele",
                Parameter.POSITIONAL_OR_KEYWORD,
                default=None,
                annotation="Union[Ele, Eles]",
            ),
        ),
    )

    return wrapper


if __name__ == "__main__":

    import time

    @urls(["python.org", "python.org", "python.org", "python.org"])
    @parallel(4)
    @get()
    @css(".widget-title")
    @text
    def crawler(res: Iterable[str]) -> None:
        """Crawler."""
        for r in res:
            print(r)

    @urls(["python.org", "python.org", "python.org", "python.org"])
    # @parallel(1)
    @get()
    @css(".widget-title")
    @text
    def crawler2(res: Iterable[str]) -> None:
        """Crawler."""
        for r in res:
            print(r)

    print("with parallel 4")
    pt = time.time()
    crawler()
    print("with parallel:", time.time() - pt)

    t = time.time()
    print("without parallel")
    crawler2()
    print("without parallel", time.time() - t)
