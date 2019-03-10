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
update   : Feb 28, 2019
email    : Nasy <nasyxx+python@gmail.com>
filename : models.py
project  : nacf
license  : LGPL-3.0+

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
from .types import (RT, HTML, Ele, Res, Url, Data, Eles, Func, Json,
                    List, Urls, EFunc, Reses, RFunc, SFunc, Tuple,
                    Union, RsFunc, Callable, Iterable, Optional, a, b,)


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
            *,
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


def get(url: Url = None, **kwds: a) -> Callable[[RFunc], RFunc]:
    """Get url."""

    def decorator(func: RFunc) -> RFunc:
        """Decorate function func."""

        @wraps(func)
        def wrapper(
            _url: Optional[Url] = None, *, _s: Optional[s] = None
        ) -> Res:
            """Wrap function func."""
            return func((_s or s()).get(format_url(_url or url), **kwds))

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
                    "_s",
                    Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation="Optional[HTMLSession]",
                ),
            ),
        )

        return wrapper

    return decorator


def gets(urls: Urls = None, **kwds: a) -> Callable[[RsFunc], RsFunc]:
    """Get url."""

    def decorator(func: RsFunc) -> RsFunc:
        """Decorate function func."""

        @wraps(func)
        def wrapper(
            _urls: Optional[Urls] = None, *, _s: Optional[s] = None
        ) -> Reses:
            """Wrap function func."""
            return func(
                map(
                    lambda u: (_s or s()).get(format_url(u)),
                    _urls or urls or [""],
                ),
                **kwds,
            )

        setattr(
            wrapper,
            "__signature__",
            generate_sig(
                func,
                Parameter(
                    "_urls",
                    Parameter.POSITIONAL_OR_KEYWORD,
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
    *,
    data: Data = None,
    json: Json = None,
    **kwds: a,
) -> Callable[[RFunc], RFunc]:
    """Post url with data and json."""

    def decorator(func: RFunc) -> RFunc:
        """Decorate function func."""

        @wraps(func)
        def wrapper(
            _url: Optional[Url] = None,
            _data: Optional[Data] = None,
            _json: Optional[Json] = None,
            *,
            _s: Optional[s] = None,
        ) -> Res:
            """Wrap function func."""
            return func(
                (_s or s()).post(format_url(url), data=data, json=json, **kwds)
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
                    "_s",
                    Parameter.KEYWORD_ONLY,
                    default=None,
                    annotation="Optional[HTMLSession]",
                ),
            ),
        )

        return wrapper

    return decorator


def posts(
    urls: Optional[Urls] = None,
    *,
    datas: Optional[Iterable[Data]] = None,
    jsons: Optional[Iterable[Json]] = None,
    **kwds: a,
) -> Callable[[RsFunc], RsFunc]:
    """Post url with data and json."""

    def decorator(func: RsFunc) -> RsFunc:
        """Decorate function func."""

        @wraps(func)
        def wrapper(
            _urls: Optional[Urls] = None,
            *,
            _datas: Optional[Iterable[Data]] = None,
            _jsons: Optional[Iterable[Json]] = None,
            _s: Optional[s] = None,
        ) -> Res:
            """Wrap function func."""

            def _post(udj: Tuple[Url, Data, Json]) -> Res:
                """Make a post."""
                url, data, json = udj
                return (_s or s()).post(
                    format_url(url), data=data, json=json, **kwds
                )

            return func(
                map(
                    _post,
                    zip(
                        _urls or urls or [""],
                        _datas or datas or cycle([None]),
                        _jsons or jsons or cycle([dict()]),
                    ),
                )
            )

        setattr(
            wrapper,
            "__signature__",
            generate_sig(
                func,
                Parameter(
                    "_urls",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Optional[Urls]",
                ),
                Parameter(
                    "_datas",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Optional[Iterable[Data]]",
                ),
                Parameter(
                    "_jsons",
                    Parameter.POSITIONAL_OR_KEYWORD,
                    default=None,
                    annotation="Optional[Iterable[Json]]",
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
            return (
                func(
                    _res.html.find(
                        selector,
                        containing=containing,
                        clean=clean,
                        first=first,
                        _encoding=_encoding,
                    )
                )
                if isinstance(_res, Res)
                else func(
                    (lambda ele: ele if first else chain.from_iterable(ele))(
                        map(
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
                    annotation="Res",
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
                _res.html.xpath(
                    selector, clean=clean, first=first, _encoding=_encoding
                )
                if isinstance(_res, Res)
                else (lambda ele: ele if first else chain.from_iterable(ele))(
                    map(
                        lambda r: r.html.xpath(
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
                    annotation="Res",
                ),
            ),
        )

        return wrapper

    return decorator


def html(func: SFunc) -> SFunc:
    """Get html from response."""

    @wraps(func)
    def wrapper(_res: Union[Res, Reses]) -> Union[HTML, Iterable[HTML]]:
        """Wrap function func."""
        return (
            func(_res.html)
            if isinstance(_res, Res)
            else map(lambda r: r.html, _res)
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
                annotation="Res",
            ),
        ),
    )

    return wrapper


def json(
    func: Callable[..., Union[Json, Iterable[Json]]]
) -> Callable[[Union[Res, Reses]], Union[Json, Iterable[Json]]]:
    """Get json from response."""

    @wraps(func)
    def wrapper(_res: Union[Res, Reses]) -> Union[Json, Iterable[Json]]:
        """Wrap function func."""
        return (
            func(_res.json())
            if isinstance(_res, Res)
            else map(lambda r: r.json(), _res)
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
                annotation="Res",
            ),
        ),
    )

    return wrapper


def text(func: SFunc) -> SFunc:
    """Get text from response or element(s) from css/xpath."""

    @wraps(func)
    def wrapper(_ele: Union[Res, Ele, Eles]) -> Union[str, Iterable[str]]:
        """Wrap function func."""
        return func(
            _ele.text
            if isinstance(_ele, Ele) or isinstance(_ele, Res)
            else map(lambda e: e.text, _ele)
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
                annotation="Union[Res, Ele, Eles]",
            ),
        ),
    )

    return wrapper
