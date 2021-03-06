# 计算机体系

计算机是一个很庞大的体系，主要的领域可以包括：计算机系统结构，程序设计，软件工程，人工智能，网络、数据库等辅助技术，算法理论等。

**计算机 = 硬件 + 软件**
计算机系统可以说是硬件与软件两部分组成。硬件包括 CPU、内存、硬盘、输入输出设备以及其他外部设备。这些硬件设备为软件的运行提供了物理基础，软件必须在硬件基础上才可以运行，计算机硬件的作用就是存储并运行软件。

计算机软件指的是计算机系统中的程序和数据。计算机系统展示给用户的各种强大功能都是由软件实现的.

软件：计算机系统的一系列计算机能识别和执行的指令，通过加载到计算机的内存中才可以运行。比如一个“计算器”软件，启动后首先运行在内存里，通过将用户的输入信息转成数字的加减乘除运算，并转换成计算机硬件能够明白的指令，然后将指令下发给 CPU 进行运算，最终结果输出给用户。

**操作系统**也是软件 计算机系统的运转需要很多软件来支撑，大体分为系统软件和应用软件，系统软件指的是我们通常用的各类操作系统，Unix/Mac os，Linux，Windows7 等。应用软件指操作系统上的各类程序，比如：Vim，Office 2003，QQ 等。为了能够开发出这些软件，我们需要计算机编程语言，这些语言是与计算机沟通的方法。

### 计算机硬件

### 计算机软件

- #### 操作系统

- #### 应用软件

### 编程

**将现实事物映射到计算机中，以解决特定的问题，带来效率的提升，创造新的需求**

```
现实事物映射到计算机：
	是指将现实事物抽象成程序给计算机下达特定的指令
例如：在线会议系统如何开发？
```

### 编程语言

**编程语言就是用来实现上述功能的工具。换言之，就是人如何和计算机交流让其帮我们实现这个功能**

### 代码

**代码就是编程语言具体表现形式，不同编程语言代码风格会有不同，就像人类语言一样**

### 人机交互

**假如我们的会议系统已经开发完成，那么这个程序是以什么形式和用户交流的，是用户一个眼神，系统就会执行特定操作（如果用人工智能的方式，这种体验可能会实现，但是背后并不是人类的智能）？不是，而是需要交互，交互就需要请求和反馈，用计算机语言来讲就是输入和输出，那我们做的程序一般会有哪些交互方式呢？**

- #### 图形化：触发事件

- #### 命令式：下达指令

### 编程语言种类

**编程语言有非常多，但是比较流行就20多种。这些流行的编程语言都有自己擅长的领域**

这里我们给这些编程语言分个类：

**机器语言：**喂给计算机的指令是以二级制(如：0b1001001)的形式，这个就是机器语言，但是由于过于繁琐和机器化了，人类是不愿意去学的，后面出现了**汇编语言**虽然有一些简单的单词符号去代替机器语言(如：ADD，MOD...)，但是写代码的过程还是没有脱离硬件，要时刻关注硬件的状态，这不是我们想要的

**高级语言：**

为了解决这种难题，高级语言出现了。不依赖于硬件，所以高级语言编写的代码都是**可移植**的。这里的代码我们称之为**源程序**(如：test.c,  test.java,  test.py)，总之，程序员设计程序框架，然后用高级语言编写实现，最终得到若干源程序文件。源程序通过编译或解释软件转化成机器语言（目标程序）。

- **编译型语言**

有些语言需要使用**编译程序**转换成二进制的机器语言，然后才可以在计算机上执行，这类语言称为**编译型**。例如C, C++，Java(有点不一样)

- **解释性语言**

有些语言不需要编译器，直接由**解释程序**直接解释运行，这类属于**解释型语言**，或**动态脚本语言**，例如 Python，Ruby，Javascript 等。

目前的高级编程语言基本都是**面向对象**语言。有些也是**函数式编程**语言（如：Lisp)，**python既是面向对象语言也支持函数式编程。**

