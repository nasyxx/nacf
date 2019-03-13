# Table of Contents

-   [Prologue](#org0e50bf5)
-   [Packages](#org8d83637)
-   [Development Process](#org3c2b122)
    -   [Http Functions](#org65f19c4)
        -   [Get](#orgc37419a)
        -   [Post](#orgbddf88e)
        -   [Bugs](#org9d69720)
            -   [Fix an error from inspect.Parameter which caused the function parallel down.](#org91e1850):err:1:
    -   [Docs](#org878a65f)
        -   [Usage](#orgd655d3f)
-   [Epoligue](#org3ee3f8d)
    -   [History](#orge615d48)
        -   [Version 1.0.2](#org556c914)
        -   [Version 1.0.1](#orga986377)
        -   [Version 1.0.0](#org09b91fe)
        -   [Version 0.1.2](#org7b65082)
        -   [Version 0.1.1](#org4cdc978)
        -   [Version 0.1.0](#org8e20622)



<a id="org0e50bf5"></a>

# Prologue

Never had such a pure crawler like this `nacf`.

Although I often write crawlers, I don&rsquo;t like to use huge frameworks, such as scrapy, but prefer
simple `requests+bs4` or more general `requests_html`.  However, these two are inconvenient for a
crawler.  E.g. Places, such as error retrying or parallel crawling, need to be handwritten by
myself.  It is not very difficult to write it while writing too much can be tedious.  Hence I
started writing this nacf (Nasy Crawler Framework), hoping to simplify some error retrying or
parallel writing of crawlers.


<a id="org8d83637"></a>

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


<a id="org3c2b122"></a>

# Development Process


<a id="org65f19c4"></a>

## DONE Http Functions

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="orgc37419a"></a>

### DONE Get

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Tue Dec 25 17:36:00 2018&gt;</span></span></p>


<a id="orgbddf88e"></a>

### DONE Post

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:44:00 2019&gt;</span></span></p>


<a id="org9d69720"></a>

### DONE Bugs

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="org91e1850"></a>

#### DONE Fix an error from inspect.Parameter which caused the function parallel down.     :err:1:

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Wed Dec 26 20:26:00 2018&gt;</span></span></p>


<a id="org878a65f"></a>

## NEXT Docs


<a id="orgd655d3f"></a>

### NEXT Usage


<a id="org3ee3f8d"></a>

# Epoligue


<a id="orge615d48"></a>

## History


<a id="org556c914"></a>

### Version 1.0.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Mar 10, 2019&gt;</span></span>
-   **Changes:** Update nalude.


<a id="orga986377"></a>

### Version 1.0.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Mar 10, 2019&gt;</span></span>
-   **Changes:** Update requests-html.


<a id="org09b91fe"></a>

### Version 1.0.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Thu Feb 28, 2019&gt;</span></span>
-   **Changes:** Now, old HTTP methods (`get` and `post`) cannot accept multiple URLs. Instead, we can use `gets` and `posts`.
-   **Adds:** -   `nacf.html`
    -   `nacf.json`
    -   `nacf.gets`
    -   `nacf.posts`
-   **Includes:** -   `nalude`


<a id="org7b65082"></a>

### Version 0.1.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Fixed:** `inspect.Parameter` error in last version.


<a id="org4cdc978"></a>

### Version 0.1.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Ignored:** An error caused by `inspect.Parameter`
-   **Help Wanted:** Can someone help me about the Parameter?


<a id="org8e20622"></a>

### Version 0.1.0

-   **Date:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Dec 23, 2018&gt;</span></span>
-   **Commemorate Version:** First Version
    -   Basic Functions.
