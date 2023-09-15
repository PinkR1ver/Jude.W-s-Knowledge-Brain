---
title: Spanning Tree
tags:
  - graph
  - data-structure
---

# What is Spanning Tree?

树上再加一条边使之存在环，就称为**基环树**

Example:

![](computer_sci/data_structure_and_algorithm/graph/attachments/Pasted%20image%2020230915111826.png)


# Why do we need Spanning Tree

* **Network design**: Spanning trees are used to create efficient and redundant networks, such as in Ethernet networks or telecommunications.
* **Routing protocols**: Spanning trees are employed in protocols like Spanning Tree Protocol (STP) and Rapid Spanning Tree Protocol (RSTP) for loop prevention and redundancy in network switches.
* [Minimum Spanning Tree (MST)](computer_sci/data_structure_and_algorithm/graph/MST.md): Spanning trees can be used to find the minimum-weighted spanning tree in a weighted graph. This is particularly useful in **optimizing costs in transportation networks or electrical power distribution grids**.
* **Broadcast algorithms**: Spanning trees are used in broadcasting messages or data packets efficiently within a network, ensuring that each node receives the message exactly once.

> [!summary] 
>  Spanning trees provide **a simplified view of the graph**, which **eliminates unnecessary edges** while **preserving connectivity**. This simplification helps in various graph-related algorithms, network design, and optimization problems.

# More about Spanning Tree

## Inward Spanning Tree, 内向基环树

一个基环树的拓展概念，没有在英文资料里查到很多相关资料，但是中文资料和chatgpt明白这个词，表达的概念一致

![](computer_sci/data_structure_and_algorithm/graph/attachments/Pasted%20image%2020230915114049.png)

内向基环树类似于基环树的结构，在有向图中，每个点有且只有一条出边，即every node out-degree = 1。$k$个点有$k$条边，那么必然存在有且只有一个环，其它点均指向这个环。
# Reference

* [_$Note$-内向基环树 - AcWing_. https://www.acwing.com/blog/content/23513/. Accessed 15 Sept. 2023.](https://www.acwing.com/blog/content/23513/)