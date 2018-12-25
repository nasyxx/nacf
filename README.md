# Table of Contents

-   [Prologue](#orgefdab53)
-   [Packages](#orgc11b1dc)
-   [Development Process](#org6e3c1eb)
    -   [Http Functions](#org89395ee)
        -   [Get](#org063529e)
        -   [Post](#orge045e05)
-   [Epoligue](#org0f619c0)
    -   [History](#org90eabca)
        -   [Version 0.1.0](#org8af289f)



<a id="orgefdab53"></a>

# Prologue

Never had such a pure crawler like this `nacf`.

Although I often write crawlers, I don&rsquo;t like to use huge frameworks, such as scrapy, but prefer
simple `requests+bs4` or more general `requests_html`.  However, these two are inconvenient for a
crawler.  E.g. Places, such as error retrying or parallel crawling, need to be handwritten by
myself.  It is not very difficult to write it while writing too much can be tedious.  Hence I
started writing this nacf (Nasy Crawler Framework), hoping to simplify some error retrying or
parallel writing of crawlers.


<a id="orgc11b1dc"></a>

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
</tbody>
</table>


<a id="org6e3c1eb"></a>

# Development Process


<a id="org89395ee"></a>

## TODO Http Functions


<a id="org063529e"></a>

### DONE Get

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">[2018-12-25 Tue 17:36]</span></span></p>


<a id="orge045e05"></a>

### NEXT Post


<a id="org0f619c0"></a>

# Epoligue


<a id="org90eabca"></a>

## History


<a id="org8af289f"></a>

### Version 0.1.0

-   **Date:** <span class="timestamp-wrapper"><span class="timestamp">&lt;2018-12-23 Sun&gt;</span></span>
-   **Commemorate Version:** First Version
    -   Basic Functions.
