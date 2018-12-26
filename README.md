# Table of Contents

-   [Prologue](#orge8b2d63)
-   [Packages](#org2d6e4f2)
-   [Development Process](#orgcdb2d25)
    -   [Http Functions](#org2562d26)
        -   [Get](#org268a91b)
        -   [Post](#org39534ac)
        -   [Bugs](#org60b0f47)
            -   [Fix an error from inspect.Parameter which caused the function parallel down.](#org5f07c18):err:1:
-   [Epoligue](#orga79b864)
    -   [History](#orgd2e0e7c)
        -   [Version 0.1.2](#org1180830)
        -   [Version 0.1.1](#org3b9e479)
        -   [Version 0.1.0](#orga1b8a28)



<a id="orge8b2d63"></a>

# Prologue

Never had such a pure crawler like this `nacf`.

Although I often write crawlers, I don&rsquo;t like to use huge frameworks, such as scrapy, but prefer
simple `requests+bs4` or more general `requests_html`.  However, these two are inconvenient for a
crawler.  E.g. Places, such as error retrying or parallel crawling, need to be handwritten by
myself.  It is not very difficult to write it while writing too much can be tedious.  Hence I
started writing this nacf (Nasy Crawler Framework), hoping to simplify some error retrying or
parallel writing of crawlers.


<a id="org2d6e4f2"></a>

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


<a id="orgcdb2d25"></a>

# Development Process


<a id="org2562d26"></a>

## TODO Http Functions


<a id="org268a91b"></a>

### DONE Get

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">[2018-12-25 Tue 17:36]</span></span></p>


<a id="org39534ac"></a>

### NEXT Post


<a id="org60b0f47"></a>

### TODO Bugs


<a id="org5f07c18"></a>

#### DONE Fix an error from inspect.Parameter which caused the function parallel down.     :err:1:

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">CLOSED:</span> <span class="timestamp">[2018-12-26 Wed 20:26]</span></span></p>


<a id="orga79b864"></a>

# Epoligue


<a id="orgd2e0e7c"></a>

## History


<a id="org1180830"></a>

### Version 0.1.2

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;2018-12-26 Wed&gt;</span></span>
-   **Fixed:** `inspect.Parameter` error in last version.


<a id="org3b9e479"></a>

### Version 0.1.1

-   **Data:** <span class="timestamp-wrapper"><span class="timestamp">&lt;2018-12-26 Wed&gt;</span></span>
-   **Ignored:** An error caused by `inspect.Parameter`
-   **Help Wanted:** Can someone help me about the Parameter?


<a id="orga1b8a28"></a>

### Version 0.1.0

-   **Date:** <span class="timestamp-wrapper"><span class="timestamp">&lt;2018-12-23 Sun&gt;</span></span>
-   **Commemorate Version:** First Version
    -   Basic Functions.
