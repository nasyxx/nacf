# Table of Contents

-   [Prologue](#org5a5b482)
-   [Packages](#org5162ade)
-   [Usage](#org8f95840)
-   [Development Process](#org500bff6)
    -   [Http Functions](#orgea60df6)
        -   [Get](#orgc53178d)
        -   [Post](#org4816e1a)
        -   [Bugs](#orgf07ea04)
            -   [Fix an error from inspect.Parameter which caused the function parallel down.](#org8cb169d):err:1:
    -   [Docs](#org471c09e)
        -   [Usage](#orgdd40ced)
-   [Epoligue](#org7d09938)
    -   [History](#org9b25ed6)
        -   [Version 1.0.2](#orgd045e62)
        -   [Version 1.0.1](#orgf937241)
        -   [Version 1.0.0](#org73249ca)
        -   [Version 0.1.2](#org872c4cb)
        -   [Version 0.1.1](#orga13def9)
        -   [Version 0.1.0](#org94f75db)



<a id="org5a5b482"></a>

# Prologue

Never had such a pure crawler like this `nacf`.

Although I often write crawlers, I don&rsquo;t like to use huge frameworks, such as scrapy, but prefer
simple `requests+bs4` or more general `requests_html`.  However, these two are inconvenient for a
crawler.  E.g. Places, such as error retrying or parallel crawling, need to be handwritten by
myself.  It is not very difficult to write it while writing too much can be tedious.  Hence I
started writing this nacf (Nasy Crawler Framework), hoping to simplify some error retrying or
parallel writing of crawlers.


<a id="org5162ade"></a>

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
<td class="org-right">0.10.0</td>
<td class="org-left">HTML Parsing for Humans.</td>
</tr>


<tr>
<td class="org-left">nalude</td>
<td class="org-right">0.3.0</td>
<td class="org-left">A standard module.  Inspired by Haskell&rsquo;s Prelude.</td>
</tr>
</tbody>
</table>


<a id="org8f95840"></a>

# Usage

see [tests](https://github.com/nasyxx/nacf/blob/master/tests/test_nacf.py).


<a id="org500bff6"></a>

# Development Process


<a id="orgea60df6"></a>

## DONE Http Functions

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="orgc53178d"></a>

### DONE Get

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Tue Dec 25 17:36:00 2018&gt;</span></span></p>


<a id="org4816e1a"></a>

### DONE Post

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:44:00 2019&gt;</span></span></p>


<a id="orgf07ea04"></a>

### DONE Bugs

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="org8cb169d"></a>

#### DONE Fix an error from inspect.Parameter which caused the function parallel down.     :err:1:

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Wed Dec 26 20:26:00 2018&gt;</span></span></p>


<a id="org471c09e"></a>

## NEXT Docs


<a id="orgdd40ced"></a>

### NEXT Usage


<a id="org7d09938"></a>

# Epoligue


<a id="org9b25ed6"></a>

## History


<a id="orgd045e62"></a>

### Version 1.0.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Mar 10, 2019&gt;</span></span>
-   **Changes:** Update nalude.


<a id="orgf937241"></a>

### Version 1.0.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Mar 10, 2019&gt;</span></span>
-   **Changes:** Update requests-html.


<a id="org73249ca"></a>

### Version 1.0.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Thu Feb 28, 2019&gt;</span></span>
-   **Changes:** Now, old HTTP methods (`get` and `post`) cannot accept multiple URLs. Instead, we can use `gets` and `posts`.
-   **Adds:** -   `nacf.html`
    -   `nacf.json`
    -   `nacf.gets`
    -   `nacf.posts`
-   **Includes:** -   `nalude`


<a id="org872c4cb"></a>

### Version 0.1.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Fixed:** `inspect.Parameter` error in last version.


<a id="orga13def9"></a>

### Version 0.1.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Ignored:** An error caused by `inspect.Parameter`
-   **Help Wanted:** Can someone help me about the Parameter?


<a id="org94f75db"></a>

### Version 0.1.0

-   **Date:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Dec 23, 2018&gt;</span></span>
-   **Commemorate Version:** First Version
    -   Basic Functions.
