 # CA-IS3105W 隔离电源测试板说明


# 1.描述
此份文件描述了 CA-IS3105W 测试板的相关使用说明，其中有产品介绍、原理图、PCB 布线图、物
料清单以及部分测试数据等。CA-IS3105W 评估板可以用来简单评估 CA-IS3105W 内置的隔离电源的参数
性能等。


# 2.芯片简介
CA-IS3105W 是一款支持 5kVRMS 隔离耐压的 DC-DC 转换器芯片，集成片上变压器，能够高效率传输
大于 650mW 功率到副边输出。该芯片采用特有控制架构，能够快速响应负载变化，并且精确调节输出
电压。CA-IS3105W 的出现可替代传统分立器件组建的隔离电源方案。该方案物理尺寸更小，且能够实
现完全隔离。
CA-IS3105W 集成软启动、短路保护、过温保护等多种保护功能以更好地增强系统的可靠性。CA￾IS3105W 具有 EN 使能管脚，当 EN 为低电时，输出电压为零，此时电源仅有微安级待机输入电流。
可通过管脚 SEL 选择 4 种输出电压，分别为 5V、3.3V、5.4V、3.7V，支持输出端接 LDO，以方便用
户不同的电压需求。CA-IS3105W 器件采用 16 脚宽体 SOIC 封装，绝缘耐压高达 5kVRMS。

# 3.物料清单
---table begin---
Table tile:UG007_CA-IS3105W物料清单表
| Item Ref Des | Qty | Description | Package | MFR PN |
|--------------|-----|-------------|---------|--------|
| 1            | CON1,CON2 | 2 | CONN, 5.08mm, Rising Cage Clamp - | Wurth Elektronik 691236510002 |
| 2            | FBL1,FBL2 | 2 | Beed 600Ω 0805 Linekey | FBG2912-601Y |
| 3            | C1 | 1 | Tantalum cap,22uF 7343 | AVX TAJD226K025RNJ |
| 4            | C2,C5,C8 | 3 | MLCC, 10μF/10V, X7R 0805 - Standard |
| 5            | C3 | 1 | MLCC, 1μF /10V, X7R 0603 - Standard |
| 6            | C4, C6, C9 | 3 | MLCC, 100nF/10V, X7R 0603 - Standard |
| 7            | C7,C10 | 2 | MLCC, 10nF/10V, X7R 0603 - Standard |
| 9            | U1 | 1 | CA-IS3105W SOP16WB | Chipanalog CA-IS3105W |
| 10           | L1 | 1 | 24uH, 0.7mm, 4.5mm*12mm - | Wurth Elektronik 7447043 |
| 11           | TP3,TP7 | 2 | Test Point, Red, Through Hole, 1mm - | Keystone 5000 |
| 12           | TP1,TP5 | 2 | Test Point, Yellow, Through Hole, 1mm - | Keystone 5009 |
| 13           | TP2,TP4,TP6,TP8 | 4 | Test Point, Black, Through Hole, 1mm - | Keystone 5001 |
| 14           | J1,J2,J3 | 3 | Header, 3 pin, 2.54mm - - Standard |
| 15           | PCB | 1 | Four layers PCB, FR-4, PCB-A008-02, 1.0mm thickness, 100mm*100mm, The distance between Inner Layer1 and Inner Layer2 should be greater than 0.4mm. | - - - |
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信号
发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1 和 CON2；
2. 将 EN 置高电平，通过跳线帽将 SEL1/SEL2 分别置高或者置低电平，选择不同的输出电压；
3. 通过示波器或者万用表测量输出电压。



# 6.测试示例
下面是以 CA-IS3105W 测试一些典型波形，包括启动波形、输出短路波形、输出纹波、输出动态响
应、效率等。





# 7.PCB 布线建议
1. CA-IS3105W 内置开关电源，为副边侧和外部模块提供稳压电源。输入侧VINP和输出侧VISO的旁路电
容和供电电容的位置放尽可能摆放在靠近芯片的管脚，距离应控制在2mm以内，如下图17和图18所
示。当需要在供电电源线和地线中放置过孔，应放置在电容相对于芯片管脚的外侧，而非放置在电
容和芯片之间，以减少过孔寄生电感的影响，如下图19和图20所示。
2. CA-IS3105W 集成隔离开关电源，存在一定的传导噪声和辐射噪声。适当的PCB拼接电容，对改善传
导干扰和辐射干扰有一定的作用。如在PCB原边GNDP和副边GNDS之间的拼接电容以及VINP/VISO对
GNDP/GNDS的拼接电容，如下图21，图22。此外，在PCB边缘处放置一系列间隔距离不大于3mm至
4mm的地过孔，形成边缘防护，如下图23所示。





# 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
