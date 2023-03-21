---
title: My Poem
tags:
- 文学
- Poem
---

  <style>
    .chinese-text {
      font-family: Source Sans Pro, SimSun;
      font-variant-east-asian: traditional;
    }
  </style>

  <script>

    document.addEventListener("DOMContentLoaded", function() {

        var paragraphs = document.querySelectorAll("p");
        paragraphs.forEach(function(p) {
            p.classList.add("chinese-text");
        });

    });

    if (location.href.indexOf("#reloaded") == -1) {
        location.href = location.href + "#reloaded";
        location.reload();
    }
  </script>
