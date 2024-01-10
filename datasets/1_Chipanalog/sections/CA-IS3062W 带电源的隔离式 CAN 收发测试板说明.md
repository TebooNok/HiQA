 # CA-IS3062W 带电源的隔离式 CAN 收发测试板说明


#  1.描述
此份文件描述了 CA-IS3062W 测试板的相关使用说明，其中有产品介绍、原理图、PCB 布线图、物
料清单以及部分测试数据等。CA-IS3062W 评估板可以用来简单评估 CA-IS3062W 内置的隔离电源以及
CAN 收发器的参数性能等。


# 2.芯片简介
CA-IS3062W 是一款隔离式控制区域网络（CAN）物理层收发器，同时内部集成隔离式 DC-DC 转换
器。符合 ISO11898-2 标准的技术规范。此器件采用片上二氧化硅（SiO2）电容作为隔离层，在 CAN 协
议控制器和物理层总线之间创建一个完全隔离的接口，配合内部集成的隔离式 DC-DC，可隔绝噪声和
干扰并防止损坏敏感电路。
CA-IS3062W 采用 SOIC 表面贴片封装形式，将 2 通道数字隔离器，CAN 收发器以及隔离式 DC-DC
集成化，芯片全局仅需要逻辑侧一个 5V 电源，实现了全隔离式 CAN 收发器方案。
CA-IS3062W 可为 CAN 协议控制器和物理层总线分别提供差分接收和差分发射能力，信号传输速率
最高可达 1 Mbps。该器件具有限流、过压和总线故障保护（ -40 V 至 40 V）以及热关断功能，可防止
输出短路，共模电压范围为 -12 V 至 12 V。CA-IS3062 额定温度范围为 -40°C 至 125°C，提供宽体 SOIC16
封装。


# 3.物料清单
---table begin---
Table tile:UG001_UG003_CA-IS3062W物料清单表
| Item Ref Des | Qty | Description | Package | MFR PN |
|--------------|-----|-------------|---------|--------|
| 1            | CON1 | 1 | CONN, 5.08mm, Rising Cage Clamp - | Wurth Elektronik 691236510002 |
| 2            | FBL1,FBL2 | 2 | Beed 600Ohm 0805 Linekey | FBG2912-601Y |
| 3            | C1 | 1 | Tantalum cap, 22uF 7343 | AVX TAJD226K025RNJ |
| 4            | C2,C5,C9 | 3 | MLCC, 10μF/10V, X7R 0805 - Standard |
| 5            | C3 | 1 | MLCC, 1μF /10V, X7R 0603 - Standard |
| 6            | C4, C6, C10 | 3 | MLCC, 100nF/10V, X7R 0603 - Standard |
| 7            | C7,C11 | 2 | MLCC, 10nF/10V, X7R 0603 - Standard |
| 8            | C8, C13 | 0 | No Connect - - - |
| 9            | C12 | 1 | MLCC, 47pF/10V, X7R 0603 - Standard |
| 10           | R1,R2 | 2 | Resistor , 22Ω, 1% 1206 - Standard |
| 11           | S1,S2,S3,S4 | 4 | SMA Connect, 2.54mm - - Standard |
| 12           | L1 | 1 | 24uH, 0.7mm, 4.5mm*12mm - | Wurth Elektronik 7447043 |
| 13           | U1 | 1 | CA-IS3062W SOP16WB | Chipanalog CA-IS3062W |
| 14           | TP5, TP11 | 2 | Test Point, Red, Through Hole, 1mm - | Keystone 5000 |
| 15           | TP1,TP3,TP7,TP9 | 4 | Test Point, Yellow, Through Hole, 1mm - | Keystone 5009 |
| 16           | TP2,TP4,TP6,TP8,TP10,TP12 | 6 | Test Point, Black, Through Hole, 1mm - | Keystone 5001 |
| 17           | J1,J2 | 2 | Header, 3 pin, 2.54mm - - Standard |
| 18           | J3,J4 | 2 | Header, 2pin, 2.54mm - - Standard |
| 19           | PCB | 1 | Four layers PCB, FR-4, PCB-A006-01, 1.0mm thickness, 100mm*100mm, The distance between Inner Layer1 and Inner Layer2 should be greater than 0.4mm. | - - - |
---table end---


# 4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信号
发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1；
2. 函数发生器输出一定频率和幅值的信号，连接到信号的输入端 TXD；
3. 通过示波器测量各个通道输出端，用示波器观察 CANH、CANL、RXD 等管脚的波形。



# 6.测试示例
下面测试一些典型波形，包括启动波形、输出短路波形、输出纹波、输出动态响应、各个信号的传
输等。


# 7.PCB 布线建议
1. CA-IS3062W内置开关电源，为副边侧和外部模块提供稳压电源。输入侧VCC和输出侧VISO的旁路电容
和供电电容的位置放尽可能摆放在靠近芯片的管脚，距离应控制在2mm以内，如下图17和图18所
示。当需要在供电电源线和地线中放置过孔，应放置在电容相对于芯片管脚的外侧，而非放置在电
容和芯片之间，以减少过孔寄生电感的影响，如下图19和图20所示。
2. CA-IS3062W集成隔离开关电源，存在一定的传导噪声和辐射噪声。适当的PCB拼接电容，对改善传
导干扰和辐射干扰有一定的作用。如在PCB原边GNDA和副边GNDB之间的拼接电容以及VCC/VISO对
GNDA/GNDB的拼接电容，如下图21，图22。此外，在PCB边缘处放置一系列间隔距离不大于3mm至
4mm的地过孔，形成边缘防护，如下图23所示。





#  8.重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

