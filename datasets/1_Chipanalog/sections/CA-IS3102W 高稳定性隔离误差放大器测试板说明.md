 # CA-IS3102W 高稳定性隔离误差放大器测试板说明


# 1.描述
此份文件描述了 CA-IS3102W 测试板的相关使用说明，其中有产品介绍、原理图、PCB 布线图、物
料清单以及部分测试数据等。CA-IS3102W 评估板可以用来简单评估 CA-IS3102W 参数性能。


# 1.1芯片简介
CA-IS3102W 是高稳定度的隔离运算放大器，被广泛应用于电源系统。该系列芯片在二次侧继承了
高性能高带宽的运算放大器，用来回馈和放大误差信号。被放大的误差信号被传送至一次侧通过缓冲
输出。CA-IS3102W 具有宽的输入电源电压范围，可达到 3V~20V。
CA-IS3102W 在一次侧和二次侧将输入电压转换出 3V 输出用于芯片供电。同时转换出高精度
1.225V 分别输出给一次侧和二次侧作为参考电压使用。


# 2.物料清单
---table begin---
Table tile:UG010_CA-IS3102W 物料清单表
| Item Ref Des | Qty | Description | Package | MFR PN |
|--------------|-----|-------------|---------|--------|
| 1            | C1, C2 | 2 | Ceramic cap 1uF/25V,X7R,0603 | 0603 - Standard |
| 2            | C3, C4 | 2 | Ceramic cap 1uF/10V,X7R,0603 | 0603 - Standard |
| 3            | C5, C6 | 2 | Ceramic cap 15pF/50V,X7R,0603 | 0603 - Standard |
| 4            | C7 | 1 | Ceramic cap 2.2nF/50V,X7R,0603 | 0603 - Standard |
| 5            | C8, C9 | 2 | Ceramic cap 10uF/5V,X7R,0805 | 0805 - Standard |
| 6            | J1, J2 | 2 | Connector, Screw Terminal, 5.08, 2P | 5.08-2P Wurth Elektronik 69123651002 |
| 7            | R1 | 1 | SMD res,42kOhm,1%,0603 | 0603 - Standard |
| 8            | R2, R6 | 2 | SMD res,0R,1%,0603 | 0603 - Standard |
| 9            | R3 | 1 | SMD res,10kOhm,1%,0603 | 0603 - Standard |
| 10           | R4, R8 | 0 | SMD res,0R,1%,0603 | 0603 - Standard |
| 11           | R5, R7 | 2 | THD res,680R,1%,1/4W | R, 1/4W, THT - Standard |
| 12           | TP1, TP2, TP3, TP4, TP5, TP6, TP7, TP11, TP15, TP16 | 0 | TEST POINT PC COMPACT .063"D RED | Keystone 5001 |
| 13           | TP8, TP9, TP10, TP12, TP13, TP14 | 0 | TEST POINT PC COMPACT .063"D BLK | Keystone 5000 |
| 14           | PCB-A017-01 | 1 | PCB - - - |
| 15           | U1 | 1 | Isolated OPAMP SOIC16-W | Chipanalog CA-IS3102W |
---table end---


#  3.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信号
发生器等。


# 3.1. 硬件连接
1. 将直流电压源连接到 J1 和 J2；注意 J1 和 J2 的极性。
注意输入电压范围：3.0V~20V。
2. 函数发生器输出一定频率和幅值的信号，连接到信号的输入端+IN 引脚；
3. 通过示波器测量各个通道输出端，可以看 VREG1、VREG2、REFOUT1、REFOUT2 电压。
用示波器观察 EAOUT、EAOUT2 管脚的波形。


# 4.测试示例
图为测试的一些典型波形及特性曲线。


# 5.PCB 布线建议
1. 输入侧VDD1和VDD2旁路电容尽可能摆放在靠近芯片的管脚，距离应控制在2mm以内，如图 27和图
28所示。当需要在供电电源线和地线中放置过孔，应放置在电容相对于芯片管脚的外侧，而非放置
在电容和芯片之间，以减少过孔寄生电感的影响，如图 29和图 30所示。
2. CA-IS3102W被广泛应用于隔离开关电源以及电机控制，这些应用中存在高￾￾
￾￾和高￾￾
￾￾的情况。由于
+IN，-IN，COMP引脚为反馈及环路控制引脚，容易受到干扰。设计PCB时，这些信号远离干扰信
号。图 31中开关电源路径中存在高￾￾
￾￾和高￾￾
￾￾，为强干扰源。控制环路路径易受到干扰。PCB走线时应
特别注意，远离强干扰源。




# 6. 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
 http://www.chipanalog.com
