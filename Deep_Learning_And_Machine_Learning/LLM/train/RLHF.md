---
title: Reinforcement Learning from Human Feedback
tags:
- LLM
- deep-learning
- RLHF
- LLM-training-method
---


# Review: Reinforcement Learning Basics

![](Deep_Learning_And_Machine_Learning/LLM/train/attachments/Pasted%20image%2020230628145009.png)


Reinforcement learning is a mathematical framework. 

Demystify the reinforcement learning model, it's a open-ended model using reward function to optimize agent to solve complex task in target environment. 

<!---
# Origins of RLHF

## Pre Deep RL

![](Deep_Learning_And_Machine_Learning/LLM/train/attachments/Pasted%20image%2020230628160836.png)


Before, Deep RL don't use neural network to represent policy. What this system did was a machine learning system that created a policy by having humans label the actions that an agent took as being kind of correct or incorrect. This was just a simple decision rule where humans labeled every actions as good or bad.  This was essentially a reward model and a policy put together.

## For Deep RL

![](Deep_Learning_And_Machine_Learning/LLM/train/attachments/Pasted%20image%2020230628161627.png)

--->

# Step by Step

For RLHF training method, here are three core steps:

1. Pretraining a language model
2. Gathering data(问答数据) and training a reward model
3. Fine-tuning the LM with reinforcement learning

## Step 1. Pretraining Language Models



# Reference

* [Reinforcement Learning from Human Feedback: From Zero to chatGPT, YouTube, HuggingFace](https://www.youtube.com/watch?v=2MBJOuVq380)
* [Hugging Face blog, ChatGPT 背后的“功臣”——RLHF 技术详解](https://huggingface.co/blog/zh/rlhf)