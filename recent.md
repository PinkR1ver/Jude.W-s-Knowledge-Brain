---
title: Recent note
tags:
  - recent
  - readme
date: 2023-06-28
---

```dataview
table WITHOUT ID file.link AS "Title",file.mtime as "Edit Time"
from ""
sort file.mtime desc
limit 10
```

```chartsview
#-----------------#
#- chart type    -#
#-----------------#
type: WordCloud

#-----------------#
#- chart data    -#
#-----------------#
data: "wordcount:/"

#-----------------#
#- chart options -#
#-----------------#
options:
  wordField: "word"
  weightField: "count"
  colorField: "count"
  wordStyle:
    rotation: 30
```

