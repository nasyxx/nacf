# Table of Contents

-   [Prologue](#orgf6129f3)
-   [Packages](#orgc58973f)
-   [Development Process](#orga10dcfb)
    -   [Http Functions](#orge0f891c)
        -   [Get](#orge2461c0)
        -   [Post](#org31f2827)
        -   [Bugs](#orgbdc9f28)
            -   [Fix an error from inspect.Parameter which caused the function parallel down.](#org496c94b):err:1:
    -   [Docs](#org84a0c46)
        -   [Usage](#org14e5d82)
-   [Epoligue](#orga2a136d)
    -   [History](#org787c477)
        -   [Version 1.0.1](#orgd26f397)
        -   [Version 1.0.0](#orgeb83aa0)
        -   [Version 0.1.2](#orgd54d625)
        -   [Version 0.1.1](#orgc5fc33b)
        -   [Version 0.1.0](#org1fa11b1)



<a id="orgf6129f3"></a>

# Prologue

Never had such a pure crawler like this `nacf`.

Although I often write crawlers, I don&rsquo;t like to use huge frameworks, such as scrapy, but prefer
simple `requests+bs4` or more general `requests_html`.  However, these two are inconvenient for a
crawler.  E.g. Places, such as error retrying or parallel crawling, need to be handwritten by
myself.  It is not very difficult to write it while writing too much can be tedious.  Hence I
started writing this nacf (Nasy Crawler Framework), hoping to simplify some error retrying or
parallel writing of crawlers.


<a id="orgc58973f"></a>

# Packages

<table>
<caption class="t-above"><span class="table-number">Table 1:</span> Packages</caption>

<colgroup>
<col  class="org-left">

<col  class="org-right">

<col  class="org-left">
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">Package</th>
<th scope="col" class="org-right">Version</th>
<th scope="col" class="org-left">Description</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">requests-html</td>
<td class="org-right">0.9.0</td>
<td class="org-left">HTML Parsing for Humans.</td>
</tr>


<tr>
<td class="org-left">nalude</td>
<td class="org-right">0.2.0</td>
<td class="org-left">A standard module.  Inspired by Haskell&rsquo;s Prelude.</td>
</tr>
</tbody>
</table>


<a id="orga10dcfb"></a>

# Development Process


<a id="orge0f891c"></a>

## DONE Http Functions

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="orge2461c0"></a>

### DONE Get

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Tue Dec 25 17:36:00 2018&gt;</span></span></p>


<a id="org31f2827"></a>

### DONE Post

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:44:00 2019&gt;</span></span></p>


<a id="orgbdc9f28"></a>

### DONE Bugs

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="org496c94b"></a>

#### DONE Fix an error from inspect.Parameter which caused the function parallel down.     :err:1:

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Wed Dec 26 20:26:00 2018&gt;</span></span></p>


<a id="org84a0c46"></a>

## NEXT Docs


<a id="org14e5d82"></a>

### NEXT Usage


<a id="orga2a136d"></a>

# Epoligue


<a id="org787c477"></a>

## History


<a id="orgd26f397"></a>

### Version 1.0.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Mar 10, 2019&gt;</span></span>
-   **Changes:** Update requests-html.


<a id="orgeb83aa0"></a>

### Version 1.0.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Thu Feb 28, 2019&gt;</span></span>
-   **Changes:** Now, old HTTP methods (`get` and `post`) cannot accept multiple URLs. Instead, we can use `gets` and `posts`.
-   **Adds:** -   `nacf.html`
    -   `nacf.json`
    -   `nacf.gets`
    -   `nacf.posts`
-   **Includes:** -   `nalude`


<a id="orgd54d625"></a>

### Version 0.1.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Fixed:** `inspect.Parameter` error in last version.


<a id="orgc5fc33b"></a>

### Version 0.1.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Ignored:** An error caused by `inspect.Parameter`
-   **Help Wanted:** Can someone help me about the Parameter?


<a id="org1fa11b1"></a>

### Version 0.1.0

-   **Date:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Dec 23, 2018&gt;</span></span>
-   **Commemorate Version:** First Version
    -   Basic Functions.
