# Table of Contents

-   [Prologue](#org6dc9402)
-   [Packages](#org37032fa)
-   [Development Process](#org1eb07f9)
    -   [Http Functions](#orgd862ea6)
        -   [Get](#orgb88fa50)
        -   [Post](#orgd091da7)
        -   [Bugs](#orga99911a)
            -   [Fix an error from inspect.Parameter which caused the function parallel down.](#orga7af803):err:1:
    -   [Docs](#orga5017d7)
        -   [Usage](#org21efc61)
-   [Epoligue](#org1e897d7)
    -   [History](#orgba8919d)
        -   [Version 1.0.0](#orgb21403b)
        -   [Version 0.1.2](#orgcd42135)
        -   [Version 0.1.1](#orgce6ff7d)
        -   [Version 0.1.0](#orgcc23226)



<a id="org6dc9402"></a>

# Prologue

Never had such a pure crawler like this `nacf`.

Although I often write crawlers, I don&rsquo;t like to use huge frameworks, such as scrapy, but prefer
simple `requests+bs4` or more general `requests_html`.  However, these two are inconvenient for a
crawler.  E.g. Places, such as error retrying or parallel crawling, need to be handwritten by
myself.  It is not very difficult to write it while writing too much can be tedious.  Hence I
started writing this nacf (Nasy Crawler Framework), hoping to simplify some error retrying or
parallel writing of crawlers.


<a id="org37032fa"></a>

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


<a id="org1eb07f9"></a>

# Development Process


<a id="orgd862ea6"></a>

## DONE Http Functions

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="orgb88fa50"></a>

### DONE Get

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Tue Dec 25 17:36:00 2018&gt;</span></span></p>


<a id="orgd091da7"></a>

### DONE Post

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:44:00 2019&gt;</span></span></p>


<a id="orga99911a"></a>

### DONE Bugs

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Thu Feb 28 20:51:00 2019&gt;</span></span></p>


<a id="orga7af803"></a>

#### DONE Fix an error from inspect.Parameter which caused the function parallel down.     :err:1:

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">&lt;Wed Dec 26 20:26:00 2018&gt;</span></span></p>


<a id="orga5017d7"></a>

## NEXT Docs


<a id="org21efc61"></a>

### NEXT Usage


<a id="org1e897d7"></a>

# Epoligue


<a id="orgba8919d"></a>

## History


<a id="orgb21403b"></a>

### Version 1.0.0

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Thu Feb 28, 2019&gt;</span></span>
-   **Changes:** Now, old HTTP methods (`get` and `post`) cannot accept multiple URLs. Instead, we can use `gets` and `posts`.
-   **Adds:** -   `nacf.html`
    -   `nacf.json`
    -   `nacf.gets`
    -   `nacf.posts`
-   **Includes:** -   `nalude`


<a id="orgcd42135"></a>

### Version 0.1.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Fixed:** `inspect.Parameter` error in last version.


<a id="orgce6ff7d"></a>

### Version 0.1.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Wed Dec 26, 2018&gt;</span></span>
-   **Ignored:** An error caused by `inspect.Parameter`
-   **Help Wanted:** Can someone help me about the Parameter?


<a id="orgcc23226"></a>

### Version 0.1.0

-   **Date:** <span class="timestamp-wrapper"><span class="timestamp">&lt;Sun Dec 23, 2018&gt;</span></span>
-   **Commemorate Version:** First Version
    -   Basic Functions.
