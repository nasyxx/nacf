# Table of Contents

-   [Prologue](#orga5fa671)
-   [Packages](#org99f6108)
-   [Development Process](#orga625a17)
    -   [Http Functions](#org9f91f69)
        -   [Get](#org8ac6e65)
        -   [Post](#org76b915f)
        -   [Bugs](#org79fb5be)
            -   [Fix an error from inspect.Parameter which caused the function parallel down.](#org98f1363):err:1:
    -   [Docs](#org3ec466e)
        -   [Usage](#orga834857)
-   [Epoligue](#org3eb4602)
    -   [History](#org2c9000c)
        -   [Version 1.0.2](#org0016de0)
        -   [Version 1.0.1](#orgfb04da4)
        -   [Version 1.0.0](#orgf141119)
        -   [Version 0.1.2](#orgac86302)
        -   [Version 0.1.1](#org4ad6a9a)
        -   [Version 0.1.0](#org5979091)



<a id="orga5fa671"></a>

# Prologue

Never had such a pure crawler like this `nacf`.

Although I often write crawlers, I don&rsquo;t like to use huge frameworks, such as scrapy, but prefer
simple `requests+bs4` or more general `requests_html`.  However, these two are inconvenient for a
crawler.  E.g. Places, such as error retrying or parallel crawling, need to be handwritten by
myself.  It is not very difficult to write it while writing too much can be tedious.  Hence I
started writing this nacf (Nasy Crawler Framework), hoping to simplify some error retrying or
parallel writing of crawlers.


<a id="org99f6108"></a>

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


<a id="orga625a17"></a>

# Development Process


<a id="org9f91f69"></a>

## DONE Http Functions

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="org8ac6e65"></a>

### DONE Get

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Tue Dec 25 17:36:00 2018&gt;</span></span></p>


<a id="org76b915f"></a>

### DONE Post

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:44:00 2019&gt;</span></span></p>


<a id="org79fb5be"></a>

### DONE Bugs

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="org98f1363"></a>

#### DONE Fix an error from inspect.Parameter which caused the function parallel down.     :err:1:

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Wed Dec 26 20:26:00 2018&gt;</span></span></p>


<a id="org3ec466e"></a>

## NEXT Docs


<a id="orga834857"></a>

### NEXT Usage


<a id="org3eb4602"></a>

# Epoligue


<a id="org2c9000c"></a>

## History


<a id="org0016de0"></a>

### Version 1.0.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Mar 10, 2019&gt;</span></span>
-   **Changes:** Update nalude.


<a id="orgfb04da4"></a>

### Version 1.0.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Mar 10, 2019&gt;</span></span>
-   **Changes:** Update requests-html.


<a id="orgf141119"></a>

### Version 1.0.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Thu Feb 28, 2019&gt;</span></span>
-   **Changes:** Now, old HTTP methods (`get` and `post`) cannot accept multiple URLs. Instead, we can use `gets` and `posts`.
-   **Adds:** -   `nacf.html`
    -   `nacf.json`
    -   `nacf.gets`
    -   `nacf.posts`
-   **Includes:** -   `nalude`


<a id="orgac86302"></a>

### Version 0.1.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Fixed:** `inspect.Parameter` error in last version.


<a id="org4ad6a9a"></a>

### Version 0.1.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Ignored:** An error caused by `inspect.Parameter`
-   **Help Wanted:** Can someone help me about the Parameter?


<a id="org5979091"></a>

### Version 0.1.0

-   **Date:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Dec 23, 2018&gt;</span></span>
-   **Commemorate Version:** First Version
    -   Basic Functions.
