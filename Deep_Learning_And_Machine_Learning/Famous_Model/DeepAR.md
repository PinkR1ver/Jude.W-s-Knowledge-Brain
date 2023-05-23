---
title: DeepAR - Time Series Forcasting
tags:
- deep-learning
- model
- time-series-dealing
---

DeepAR, an autoregressive recurrent network developed by Amazon, is the first model that could natively work on multiple time-series. It's a milestone in time-series community.

# What is DeepAR

> [!quote] 
>  DeepAR is the first successful model to combine Deep Learning with traditional Probabilistic Forecasting.

* **Multiple time-series support**
* **Extra covariates**: *DeepAR* allows extra features, covariates. It is very important for me when I learn *DeepAR*, because in my task, I have corresponding feature for each time series.
* **Probabilistic output**:  Instead of making a single prediction, the model leverages [**quantile loss**](Deep_Learning_And_Machine_Learning/Trick/quantile_loss.md) to output prediction intervals.
* **“Cold” forecasting:** By learning from thousands of time-series that potentially share a few similarities, _DeepAR_ can provide forecasts for time-series that have little or no history at all.

# Block used in DeepAR

* [LSTM](Deep_Learning_And_Machine_Learning/Deep_Learning_Block_and_Machine_Learning_Block/LSTM.md)

# Reference

* [https://towardsdatascience.com/deepar-mastering-time-series-forecasting-with-deep-learning-bc717771ce85](https://towardsdatascience.com/deepar-mastering-time-series-forecasting-with-deep-learning-bc717771ce85)