 # CA-IS364x 带电源的数字隔离器测试板说明


#  1.描述
此份文件描述了 CA-IS364x 测试板的相关使用说明，其中有产品介绍、原理图、PCB 布线图、物料
清单以及部分测试数据等。CA-IS364x 评估板可以用来简单评估 CA-IS364x 内置的隔离电源以及数字隔离
的参数性能等。


#  2.芯片简介
CA-IS364x 是数字隔离器系列中，增强隔离耐压并集成 DC-DC 转换器的一款芯片。CA-IS364x 的出
现可替代传统用分立器件组建的隔离电源方案，并且新方案使得外形尺寸更小，能够实现完全隔离。
CA-IS3640/CA-IS3641/CA-IS3642/CA-IS3643/CA-IS3644 是四通道数字隔离器。
CA-IS3640 芯片具有四个前向通道，CA-IS3641 芯片具有三个前向通道和一个反向通道，CA-IS3642
芯片具有两个前向通道和两个反向通道，CA-IS3643 芯片具有一个前向通道和三个反向通道，CA￾IS3644 具有四个反向通道。所有器件都具有故障安全模式选项，如果输入信号丢失，则以 L 为后缀的
芯片默认输出为低电平，以 H 为后缀的芯片默认输出为高电平。
下面以 CA-3641H 为例，介绍 CA-IS364x 系列的测试说明。



# 3.物料清单
---table begin---
Table tile:UG002_CA-IS364x物料清单表
| Item Ref Des | Qty | Description | Package | MFR PN |
|--------------|-----|-------------|---------|--------|
| 1            | CON1 | 1 | CONN, 5.08mm, Rising Cage Clamp - | Wurth Elektronik 691236510002 |
| 2            | FBL1,FBL2 | 2 | Beed 600Ω 0805 Linekey | FBG2912-601Y |
| 3            | C1 | 1 | Tantalum cap, 22uF 7343 | AVX TAJD226K025RNJ |
| 4            | C2,C5,C12 | 3 | MLCC, 10μF/10V, X7R 0805 - Standard |
| 5            | C3 | 1 | MLCC, 1μF /10V, X7R 0603 - Standard |
| 6            | C4, C6, C13 | 3 | MLCC , 100nF/10V, X7R 0603 - Standard |
| 7            | C7,C14 | 2 | MLCC, 10nF/10V, X7R 0603 - Standard |
| 8            | C8,C9,C10,C11,C15,C16,C17,C18 | 8 | No Connect 0603 - Standard |
| 9            | U1 | 1 | CA-IS3641HW SOP16WB | Chipanalog CA-IS3641HW |
| 10           | S1,S2,S3,S4,S5,S6,S7,S8 | 8 | SMA Connect, 2.54mm - - Standard |
| 11           | L1 | 1 | 24uH, 0.7mm, 4.5mm*12mm - | Wurth Elektronik 7447043 |
| 12           | TP9,TP21 | 2 | Test Point, Red, Through Hole, 1mm - | Keystone 5000 |
| 13           | TP1,TP3,TP5,TP7,TP11,TP13,TP15,TP17,TP19 | 9 | Test Point, Yellow, Through Hole, 1mm - | Keystone 5009 |
| 14           | TP2,TP4,TP6,TP8,TP10,TP12,TP14,TP16,TP18,TP20,TP22 | 11 | Test Point, Black, Through Hole, 1mm - | Keystone 5001 |
| 15           | J1,J2,J3,J4,J5,J6,J7,J8,J9 | 9 | Header, 3 pin, 2.54mm - - Standard |
| 16           | PCB | 1 | Four layers PCB, FR-4, PCB-A004-01, 1.0mm thickness, 100mm*100mm, The distance between Inner Layer1 and Inner Layer2 should be greater than 0.4mm. | - - - |
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信号
发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1；
2. 函数发生器输出一定频率和幅值的信号，连接到各个通道的输入端；
3. 通过示波器测量各个通道输出端，用示波器观察各个通道信号。


# 6.测试示例
下面是以 CA-IS3641H 为例，测试一些典型波形，包括启动波形、输出短路波形、输出纹波、输出
动态响应、各个通道的信号传输眼图等。



# 7.PCB 布线建议
1. CA-IS364x 内置开关电源，为副边侧和外部模块提供稳压电源。输入侧VDD和输出侧VISO的旁路电容和
供电电容的位置放尽可能摆放在靠近芯片的管脚，距离应控制在2mm以内，如下图18和图19所示。
当需要在供电电源线和地线中放置过孔，应放置在电容相对于芯片管脚的外侧，而非放置在电容和
芯片之间，以减少过孔寄生电感的影响，如下图20和图21所示。
2. CA-IS364x 集成隔离开关电源，存在一定的传导噪声和辐射噪声。适当的PCB拼接电容，对改善传导
干扰和辐射干扰有一定的作用。如在PCB原边GNDA和副边GNDB之间的拼接电容以及VDD/VISO对
GNDA/GNDB的拼接电容，如下图22，图23。此外，在PCB边缘处放置一系列间隔距离不大于3mm至
4mm的地过孔，形成边缘防护，如下图24所示。


# 8. 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
