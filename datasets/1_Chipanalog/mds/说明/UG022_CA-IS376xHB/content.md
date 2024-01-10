 # CA-IS376x HB 小封装高速六通道字隔离器测试板说明


# 1.描述
此份文件描述了 CA-IS376x 测试板的相关使用说明，其中有产品介绍、原理图、PCB 布线图、物料
清单等。CA-IS376x 测试板可以用来简单评估 CA-IS376x 数字隔离的参数性能。


# 2.芯片简介
CA-IS376x 是一款高性能四通道数字隔离器，具有精确的时序特性和低电源损耗。 在隔离 CMOS
数字 I/O 时， CA-IS376x 器件可提供高电磁抗扰度和低辐射。所有器件版本均具有施密特触发器输入，
可实现高抗噪性能。 每条隔离通道的逻辑输入和输出缓冲器均由二氧化硅 (SiO2) 绝缘栅隔离。
CA-IS3760/CA-IS3762 是六通道数字隔离器。CA-IS3760 六个通道都在同一个方向上，输出侧（B 侧）
具有输出使能； CA-IS3762 具有四个前向和两个反向通道，两侧都有输出使能。 所有设备都具有故障
安全模式选项。 如果输入侧电压或信号丢失，对于后缀为 L 的设备，默认输出为低，对于带有后缀 H
的设备，默认输出为高。
通过改变 BOM 表，CA-IS376xHB 测试板可以用于评估如下型号的高速四通道数字隔离器。
表 1 适用 CA_IS376x 测试板的高速四通道数字隔离器型号
---table begin---测试板的高速四通道数字隔离器型号物料清单表
| 型号 | 输入通道数 (A侧) | 输入通道数 (B侧) | 故障安全 | 输出状态 | 额定耐压 (kV) | 输出使能 | 封装     |
|------|--------------------|--------------------|----------|----------|----------------|----------|----------|
| CA-IS3760LB | 6 | 0 | 低 | 3.75 | 无 | SSOP16 |
| CA-IS3762LB | 4 | 2 | 低 | 3.75 | 无 | SSOP16 |
| CA-IS3762HB | 4 | 2 | 高 | 3.75 | 无 | SSOP16 |
---table end---


# 3.物料清单
---table begin---
Table tile:UG022_CA-IS376xHB 物料清单表
| Item | Ref Des | Qty | Description | Package | MFR PN |
|------|---------|-----|-------------|---------|--------|
| 1    | CON1, CON2 | 2 | CONN, 5.08mm, Rising Cage Clamp | - | Wurth Elektronik 691236510002 |
| 2    | C1, C12 | 2 | Tantalum cap, 22uF | 7343 | AVX TAJD226K025RNJ |
| 3    | C2, C13 | 2 | MLCC, 10uF/10V, X7R | 0805 | Standard |
| 4    | C3, C4, C14, C16 | 4 | MLCC, 1uF/10V, X7R | 0603 | Standard |
| 5    | C5, C15 | 2 | MLCC, 0.1uF/16V, X7R | 0603 | Standard |
| 6    | C6, C7, C8, C9, C10, C11, C17, C18, C19, C20, C21 | 0 | NA | 0603 | - |
| 7    | J1, J2, J3, J4, J5, J6, J7, J8, J9, J10, J11, J12 | 12 | Header 3 pin, 2.54mm | - | - |
| 8    | TP1, TP3, TP5, TP7, TP9, TP11, TP13, TP15, TP17, TP19, TP21, TP23, TP25, TP27 | 14 | Test Point, Red, Through Hole, 1mm | - | Keystone 5000 |
| 9    | TP2, TP4, TP6, TP8, TP10, TP12, TP14, TP16, TP18, TP20, TP22, TP24, TP26, TP28 | 14 | Test Point, Black, Through Hole, 1mm | - | Keystone 5009 |
| 10   | S1, S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12 | 12 | SMA Connect, 2.54mm | SMA | - |
| 11   | CA-IS3762HB | 1 | 6-Channel high-speed Digital Isolator | SSOP16 | Chipanalog CA-IS3762HB |
| 12   | PCB | 1 | Two Layers PCB, FR-4, PCB-A007-00, 1mm thickness | - | - |
---table end---


# 4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、高频信号发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1，CON2；
2. 函数发生器输出一定频率和幅值的方波信号，连接到各个通道的输入端；
3. 通过示波器测量各个通道输出端，用示波器观察各个通道信号。


#  重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

