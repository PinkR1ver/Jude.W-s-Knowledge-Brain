---
title: Maxwell's Equation
tags:
- physics
- electromagnetism
- nuclear-level-knowledge
---

# Equation


$$
\nabla \cdot E = \frac{\rho}{\epsilon_0}
$$

$$
\nabla \cdot B = 0
$$

$$
\nabla \times E = -\frac{\partial B}{\partial t}
$$

$$
\nabla \times B = \mu_0 (J + \epsilon_0 \frac{\partial E}{\partial t})
$$

# Vector field

Essentially a vector field is what you get if you associate each point in space with a vector, some magnitude and direction. Maybe those vectors represent the velocities of particles of fluid at each point in space or maybe they represent the force of gravity at many different points in space or maybe a magnetic field strength.

> [!note] 
>  If you were to draw the vectors to scale, the longer ones end up just cluttering the whole thing, so it's common to basically lie a little and artificially shorten ones that are too long. Maybe using **color to give some vague sense of length**.

![](Physics/Electromagnetism/attachments/Pasted%20image%2020230411151612.png)

## Divergence

![](Physics/Electromagnetism/attachments/my-life.gif)

Divergence $\cdot$ Vector filed是来衡量在(x, y)点你产生fluid的能力

所以上述图中，产生fluid的source点，他们的Divergence $\cdot$ Vector filed是positive的

那些fluid流入的sink端，他们的Divergence $\cdot$ Vector filed就是negative的

![](Physics/Electromagnetism/attachments/Pasted%20image%2020230411155711.png)

同时，如果点可以slow flow in变fast slow out，这个点位的divergence $\cdot$ vector filed也是positive的

![](Physics/Electromagnetism/attachments/my-life%201.gif)

Vector field input point得到的是一个多维的输出，指向一个方向并带有scale；divergence $\cdot$ vector field，它的输出depends on the behavior of the field in small neighborhood around that point。输出为一个数值，衡量这个point acts as a source or a sink

![](Physics/Electromagnetism/attachments/Pasted%20image%2020230411161346.png)

> [!note] 
>  For actual fluid flow: $\text{div} F = 0$ everywhere

## Curl

![](Physics/Electromagnetism/attachments/output%202.gif)

Curl是衡量fluid在point被rotate的程度，clockwise方向是positive curl，counterclockwise是negative curl。

![](Physics/Electromagnetism/attachments/curl.gif)

上图中这个点的curl也是非零的，因为fluid上快下慢，result in clockwise influence

# Understand Maxwell's Equation

学会vector filed中的divergence和curl，是理解Maxwell’s Equation的关键

## Gauss's Law

$$
\text{div} E = \frac{\rho}{\epsilon_0}
$$


![](Physics/Electromagnetism/attachments/Pasted%20image%2020230411163735.png)

* $\rho$是charge density
* $\epsilon_0$是Epsilon Naught，free space的介电常数，它决定free space空间中电场的强度

> [!note] 
> 形象的
> 
> Gauss's law stating that **divergence of an electric field at a given point is a proportional to the charge density at that point**. 
> 
> **Positively charged regions as acting like sources** of some imagined fluid and n**egatively charged regions as being the sinks** of that fluid.
> 
> Parts of space where there is on charge the fluid **would be flowing incompressively** just like water.


## Gauss's law for magnetism

$$
\text{div} B = 0
$$

![](Physics/Electromagnetism/attachments/Pasted%20image%2020230411165048.png)

磁场的divergence在任意地方为0，说明磁场的fluid是incompressible的，没有source也没有sinks，就像water一样。也有这样的interpretation，说明magnetic monopoles是不存在的

## Maxwell–Faraday equation (Faraday's law of induction)



# Reference

* [Fun fluid-flow illustrations - by 3B1B](https://anvaka.github.io/fieldplay/?cx=0&cy=0&w=8.5398&h=8.5398&dt=0.01&fo=0.998&dp=0.009&cm=1&vf=%2F%2F%20p.x%20and%20p.y%20are%20current%20coordinates%0A%2F%2F%20v.x%20and%20v.y%20is%20a%20velocity%20at%20point%20p%0Avec2%20get_velocity%28vec2%20p%29%20%7B%0A%20%20vec2%20v%20%3D%20vec2%280.%2C%200.%29%3B%0A%0A%20%20%2F%2F%20change%20this%20to%20get%20a%20new%20vector%20field%0A%20%20v.x%20%3D%20p.y%3B%0A%20%20v.y%20%3D%20%28max%28cos%28sin%28p.y%29%29%2Csin%28p.y%29%2Fp.y%29%2Bp.y%29%3B%0A%0A%20%20return%20v%3B%0A%7D&code=%2F%2F%20p.x%20and%20p.y%20are%20current%20coordinates%0A%2F%2F%20v.x%20and%20v.y%20is%20a%20velocity%20at%20point%20p%0Avec2%20get_velocity%28vec2%20p%29%20%7B%0A%20%20vec2%20v%20%3D%20vec2%280.%2C%200.%29%3B%0A%0A%20%20%2F%2F%20change%20this%20to%20get%20a%20new%20vector%20field%0A%20%20v.x%20%3D%20%28max%28p.x%2Cp.y%29%2Bmax%28p.y%2Cp.x%29%29%3B%0A%20%20v.y%20%3D%20p.y%3B%0A%0A%20%20return%20v%3B%0A%7D)
* [Divergence and curl: The language of Maxwell's equations, fluid flow, and more - YouTube vedio by 3b1b](https://www.youtube.com/watch?v=rB83DpBJQsE)
* [Let There Be Light: Maxwell's Equation EXPLAINED for BEGINNERS - YouTube vedio by Parth G](https://www.youtube.com/watch?v=0jW74lrpeM0)