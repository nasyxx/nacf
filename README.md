# Table of Contents

-   [Prologue](#org591fabd)
-   [Packages](#orgfab1ac5)
-   [Development Process](#orgf9ac559)
    -   [Http Functions](#org0c20f86)
        -   [Get](#org7d426ca)
        -   [Post](#org40e101b)
        -   [Bugs](#org2b33a0e)
            -   [Fix an error from inspect.Parameter which caused the function parallel down.](#orgb794b62)
-   [Epoligue](#org1b62763)
    -   [History](#org953eff6)
        -   [Version 0.1.1](#org40f41b8)
        -   [Version 0.1.0](#org18b1472)



<a id="org591fabd"></a>

# Prologue

Never had such a pure crawler like this `nacf`.

Although I often write crawlers, I don&rsquo;t like to use huge frameworks, such as scrapy, but prefer
simple `requests+bs4` or more general `requests_html`.  However, these two are inconvenient for a
crawler.  E.g. Places, such as error retrying or parallel crawling, need to be handwritten by
myself.  It is not very difficult to write it while writing too much can be tedious.  Hence I
started writing this nacf (Nasy Crawler Framework), hoping to simplify some error retrying or
parallel writing of crawlers.


<a id="orgfab1ac5"></a>

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


<a id="orgf9ac559"></a>

# Development Process


<a id="org0c20f86"></a>

## TODO Http Functions


<a id="org7d426ca"></a>

### DONE Get

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">[2018-12-25 Tue 17:36]</span></span></p>


<a id="org40e101b"></a>

### NEXT Post


<a id="org2b33a0e"></a>

### TODO Bugs


<a id="orgb794b62"></a>

#### TODO Fix an error from inspect.Parameter which caused the function parallel down.


<a id="org1b62763"></a>

# Epoligue


<a id="org953eff6"></a>

## History


<a id="org40f41b8"></a>

### Version 0.1.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;2018-12-26 Wed&gt;</span></span>
-   **Ignored:** An error caused by `inspect.Parameter`
-   **Help Wanted:** Can someone help me about the Parameter?


<a id="org18b1472"></a>

### Version 0.1.0

-   **Date:** <span class="timestamp-wrapper"><span class="timestamp">&lt;2018-12-23 Sun&gt;</span></span>
-   **Commemorate Version:** First Version
    -   Basic Functions.
