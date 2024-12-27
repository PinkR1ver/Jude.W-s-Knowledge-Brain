---
title: oh-my-zsh theme powerlevel10k set conda env
tags:
  - tool
  - python
  - conda
  - anaconda
date: 2024-12-27
---
# Method

After `conda init`

we need to set in the `~/.p10k/zsh`

```zsh
vim ~/.p10k/zsh
```

Add this two sentences in this file, this two sentences are designed for the color and env format.

```p10k
# Anaconda environment color.
typeset -g POWERLEVEL9K_ANACONDA_FOREGROUND=37
typeset -g POWERLEVEL9K_ANACONDA_CONTENT_EXPANSION='${${${${CONDA_PROMPT_MODIFIER#\(}% }%\)}:-${CONDA_PREFIX:t}}'
```

And then add `anaconda` to `POWERLEVEL9K_LEFT_PROMPT_ELEMENTS` or `POWERLEVEL9K_RIGHT_PROMPT_ELEMENT` to show.

# Reference

* https://blog.csdn.net/qq_44640931/article/details/130353515