 # CA-IS362x 带电源的数字隔离器测试板说明


# 1. 描述
此份文件描述了 CA-IS362x 测试板的相关使用说明，其中有产品介绍、原理图、PCB 布线图、物料
清单以及部分测试数据等。CA-IS362x 评估板可以用来简单评估 CA-IS362x 内置的隔离电源以及数字隔离
的参数性能等。


#  2.芯片简介
CA-IS362x 是数字隔离器系列中，增强隔离耐压并集成 DC-DC 转换器的一款芯片。CA-IS362x 的出
现可替代传统用分立器件组建的隔离电源方案，并且新方案使得外形尺寸更小，能够实现完全隔离。
CA-IS3620/CA-IS3621/CA-IS3622 是双通道数字隔离器。
CA-IS3620 芯片有两个同向的通道，CA-IS3621 和 CA-IS3622 芯片具有一个前向的和一个反向的通
道。所有器件都具有故障安全模式选项，如果输入信号丢失，则以 L 为后缀的芯片默认输出为低电平，
以 H 为后缀的芯片默认输出为高电平。
下面以 CA-3621H 为例，介绍 CA-IS362x 系列的测试说明。


# 3.物料清单
---table begin---
Table tile:UG001_CA-IS362x物料清单表
Item Ref Des** | Qty** | Description** | Package** | MFR PN**
--- | --- | --- | --- | ---
1 | T1,T2 | 2 | CONN Banana Jack | Solder - Keystone 575-4
2 | FBL1,FBL2 | 2 | Beed 600Ω 0805 Linekey | FBG2912-601Y
3 | C1 | 1 | Tantalum cap, 22uF 7343 | AVX TAJD226K025RNJ
4 | C2,C5,C10 | 3 | MLCC, 10μF/10V, X7R 0805 | Standard
5 | C3 | 1 | MLCC, 1μF /10V, X7R 0603 | Standard
6 | C4, C6, C11 | 3 | MLCC, 100nF/10V, X7R 0603 | Standard
7 | C7,C12 | 2 | MLCC, 10nF/10V, X7R 0603 | Standard
8 | C8,C9,C13,C14 | 4 | No Connect | 0603 | -
9 | U1 | 1 | CA-IS3621HW SOP16WB | Chipanalog CA-IS3621HW
10 | S1,S2,S3,S4 | 4 | SMA Connect, 2.54mm | - | Standard
11 | L1 | 1 | 24uH, 0.7mm, 4.5mm*12mm | Wurth Elektronik 7447043
12 | TP5,TP13 | 2 | Test Point, Red, Through Hole, 1mm | Keystone 5000
13 | TP1,TP3,TP7,TP9,TP11 | 5 | Test Point, Yellow, Through Hole, 1mm | Keystone 5009
14 | TP2,TP4,TP6,TP8,TP10,TP12,TP14 | 7 | Test Point, Black, Through Hole, 1mm | Keystone 5001
15 | J1,J2,J3,J4,J5 | 5 | Header, 3 pin, 2.54mm | - | Standard
16 | PCB | 1 | Four layers PCB, FR-4, PCB-A002-01, 1.0mm thickness, 99mm*99mm, The distance between Inner Layer1 and Inner Layer2 should be greater than 0.4mm. | - | -  
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信号发
生器等。


# 5. 硬件连接
1. 将直流电压源连接到 T1 和 T2；
2. 函数发生器输出一定频率和幅值的信号，连接到各个通道的输入端；
3. 通过示波器测量各个通道输出端，用示波器观察各个通道信号。


# 6.测试示例
下面是以 CA-IS3621H 为例，测试一些典型波形，包括启动波形、输出短路波形、输出纹波、输出
动态响应、各个通道的信号传输眼图等。


# 7.PCB 布线建议
1. CA-IS362x内置开关电源，为副边侧和外部模块提供稳压电源。输入侧VDD和输出侧VISO的旁路电容
和供电电容的位置放尽可能摆放在靠近芯片的管脚，距离应控制在2mm以内，如下图17和图18所
示。当需要在供电电源线和地线中放置过孔，应放置在电容相对于芯片管脚的外侧，而非放置在电
容和芯片之间，以减少过孔寄生电感的影响，如下图19和图20所示。
2. CA-IS362x集成隔离开关电源，存在一定的传导噪声和辐射噪声。适当的PCB拼接电容，对改善传导
干扰和辐射干扰有一定的作用。如在PCB原边GNDA和副边GNDB之间的拼接电容以及VDD/VISO对
GNDA/GNDB的拼接电容，如下图21，图22。此外，在PCB边缘处放置一系列间隔距离不大于3mm至
4mm的地过孔，形成边缘防护，如下图23所示。


# 8. 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

