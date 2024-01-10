 # CA-IS372x 高性能双通道增强型数字隔离器测试板说明


#  1.描述
此份文件描述了 CA-IS372x 系列双通道数字隔离器评估板的使用方法。使用户可以评估芯片性能且
对隔离系统进行系统性分析，从而提高开发速度。该评估板可以兼容该系列双通道的 SOIC8-G 宽体封装
的数字隔离器。


# 2.芯片简介
CA-IS372x 系列数字隔离器芯片是通过 VDE 和 CSA 认证的增强绝缘隔离器芯片。该系列芯片具有高
抗电磁干扰以及低干扰特性。该系列芯片具有低功耗特性，适用于 CMOS 或者 LVMOS 的数字 IO 口。
CA-IS372x 系列芯片采用片上二氧化硅（SiO2）电容作为隔离层将输入和输出接口隔离，输出还具有缓
冲特性。通过使用隔离电源供电，芯片可以防止一侧信号高电压以及噪音干扰到另外一侧信号，避免高
压引起电压敏感器件的损坏，也可以防止一侧地上的噪音干扰到另一侧的信号。
下面以 CA-IS372x SOIC8-G 宽体为例，介绍 CA-IS372x 系列的测试说明。


# 3.物料清单
---table begin---
Table tile:UG009_CA-IS372xG 物料清单表
| Item Ref Des | Qty | Description | Package | MFR PN |
|--------------|-----|-------------|---------|--------|
| 1            | CON1,CON2 | 2 | CONN, 5.08mm, Rising Cage Clamp - | Wurth Elektronik 691236510002 |
| 2            | FBL1,FBL2,FBL3,FBL4 | 2 | Beed 600Ω 0805 - | FBG2912-601Y |
| 3            | C1,C8 | 2 | Tantalum cap,22uF 7343 | AVX TAJD226K025RNJ |
| 4            | C2,C9 | 2 | MLCC, 10μF/10V, X7R 0805 - Standard |
| 5            | C3,C4,C10,C12 | 4 | MLCC, 1μF /10V, X7R 0603 - Standard |
| 6            | C5,C11 | 2 | MLCC, 100nF/10V, X7R 0603 - Standard |
| 7            | C6,C7,C13,C14 | 4 | No Connect 0603 - Standard |
| 8            | U1 | 1 | CA-IS3722HG SOIC8-G | Chipanalog CA-IS3722HG |
| 9            | S1,S2,S3,S4 | 4 | SMA Connect, 2.54mm - - Standard |
| 10           | TP5,TP7 | 2 | Test Point, Red, Through Hole, 1mm - | Keystone 5000 |
| 11           | TP1,TP3,TP9,TP11 | 4 | Test Point, Yellow, Through Hole, 1mm - | Keystone 5009 |
| 12           | TP2,TP4,TP6,TP8,TP10,TP12 | 6 | Test Point, Black, Through Hole, 1mm - | Keystone 5001 |
| 13           | J1,J2,J3,J4 | 4 | Header, 3 pin, 2.54mm - - Standard |
| 14           | PCB | 1 | Two layers PCB, FR-4, PCB-A012-01, 1.6mm thickness | - - - |
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、6.5 位多功能万用表安捷伦 34465A、高频信号
发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1 和 CON2；
2. 函数发生器输出一定频率和幅值的信号，连接到各个通道的输入端；
3. 通过示波器测量各个通道输出端，用示波器观察各个通道信号。




# 6.测试示例
图 为在评估板上所测的数字隔离器 CA-IS372x 的典型输入和输出波形。输入信号频率为 0.5MHz，
幅度为 3.3V，占空比为 50%的方波。示波器第一通道黄色波形为输入端 VI1 的电压，第二通道绿色波形
为输出端 VO1 的电压。



#  重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

