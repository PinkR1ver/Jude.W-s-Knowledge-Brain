---
title: How to deal with the error 35 by using proxy in curl
tags:
  - curl
  - web
  - terminal_command
date: 2024-12-27
---
error:

```
curl: (35) OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to 127.0.0.1:7890
```

We need to set the https proxy to http, not https


```zsh
export https_proxy=http://192.168.14.180:3128
```

# Reference

* https://codingman.cc/https-proxy-curl-error/