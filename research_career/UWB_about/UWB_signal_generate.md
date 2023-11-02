---
title: How to generate UWB signal
tags:
  - UWB
  - signal-processing
---
# Actual Signals which find use in UWB systems

* Gaussian-derived pulses
* Edge-derived pulses
* Sinc pulses
* Truncated sine pulses
* Chirp signals (frequency sweep)

## Gaussian-derived pulses

Time-domain function:

$$
T_n(t) = \frac{\tau^n (\frac{n}{2})! d^n}{n!} \frac{d^n}{d t^n} e^{-\frac{t^2}{\tau^2}}
$$
Frequency-domain function:


$$
F_n(\omega) = \frac{{\tau^n} (\frac{n}{2})!}{n!} (j\omega)^n \sqrt{\pi \tau^2} e^{-\frac{\pi^2 \omega^2}{4}}
$$


# Methods of generating UWB signals


There are two methods to generate UWB signals. 

1. Radio Frequency (RF)/ microwave analogue techniques
2. Digital synthesis methods such as direct digital synthesis (DSS).


## RF, micro analogue techniques


Modern analogue techniques make use of solid-state devices such as diodes and transistors. 

Diodes:
* Step recovery diodes (SRDs)
* Tunnel diodes
* Schottky diodes


# Reference

* [Papers Read in 2023.11](research_career/papers_read/papers_2023_11.md)