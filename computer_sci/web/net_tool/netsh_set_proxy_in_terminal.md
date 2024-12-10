---
title: Windows set http proxy in terminal
tags:
  - net
  - tool
  - terminal_command
date: 2024-12-10
---
```PowerShell
netsh winhttp set proxy proxy-server="http://your.proxy.server:port" bypass-list="*.example.com"

netsh winhttp reset proxy
```
