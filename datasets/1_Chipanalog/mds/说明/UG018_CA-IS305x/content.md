 # CA-IS305x隔离式CAN收发器测试板说明


# 1.描述
此份文件描述了 CA-IS305x 隔离式 CAN 收发器评估板的使用方法。使用户可以评估芯片性能且对隔
离系统进行系统性分析，从而提高开发速度。


# 2.芯片简介
CA-IS305x 是一款隔离式控制区域网络(CAN)物理层收发器，符合 ISO11898-2 标准的技术规范。此器
件采用片上二氧化硅(SiO2)电容作为隔离层，在 CAN 协议控制器和物理层总线之间创建一个完全隔离的
接口，与隔离电源一起使用，可隔绝噪声和干扰并防止损坏敏感电路。
CA-IS305x 可为 CAN 协议控制器和物理层总线分别提供差分接收和差分发射能力，信号传输速率最
高可达 1 Mbps。该器件具有限流、过压和接地损耗保护(–58 V 至 58 V)以及热关断功能，可防止输出短
路，共模电压范围为–30 V 至 30 V。
CA-IS305x 额定温度范围为–40°C 至 125°C，提供宽体 DUB8(U)封装。
本 EVM 的 PCB 可适用于 CA-IS3050U，CA-IS3052U，CA-IS3050EU，CA-IS3052EU。当安装上
CA-IS3052U，CA-IS3052EU 时，信号侧 TXD 实际为 RXD 输出信号，RXD 实际为 TXD 输入信号。


# 3.物料清单
---table begin---
Table tile:UG018_CA-IS305x 物料清单表
| Item | Ref Des             | Qty | Description                            | Package   | MFR          PN        |
|------|---------------------|-----|----------------------------------------|-----------|-----------------------|
| 1    | B1, B2, B3, B4      | 4   | Banana Connector                        | -         | Keystone  575-4     |
| 2    | C1, C2,C4, C6       | 4   | Ceramic Cap, 1uF/10V, X7R, 0603       | 0603      | -                   |
| 3    | C3,C5               | 2   | Ceramic Cap, 0.1uF/50V, X7R, 0603    | 0603      | -                   |
| 4    | C7                  | 1   | Ceramic Cap, 4.7nF/50V, X7R, 0603    | 0603      | -                   |
| 5    | J1, J2, J3, J4       | 4   | Standard SMA Connector                 | SMA       | -                   |
| 6    | J5, J6              | 2   | Header, Unshrouded, 2.54, Male, 3P    | Con,hdr,  | -                   |
|      |                     |     |                                      | 254-3p    |                     |
| 7    | R1, R2              | NA  | SMD Res, NA                            | R1206     | -                   |
| 8    | R3, R4              | 2   | SMD Res, 30R, 1%, 1206                 | R1206     | -                   |
| 9    | TP1, TP3, TP5, TP7   | 4   | Test Point PC Mini .040"D Red          | tpt,      | Keystone  5000       |
|      |                     |     |                                      | keystone- |                     |
| 10   | TP2, TP4, TP6, TP8   | 4   | Test Point PC Mini .040"D Black        | tpt,      | Keystone  5001       |
|      |                     |     |                                      | keystone- |                     |
| 11   | U1                  | 1   | Isolated CAN Transceiver               | DUB8      | Chipanalog  CA-IS3050U |
| 12   | PCB                 | 1   | Two Layers PCB, FR-4, 1.6mm thickness | -         | PCB-A007-01           |
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、高频信号发生器等。


# 5.硬件连接
1. 将直流电压源连接到 B1/B2 和 B3/B4；注意隔离 CAN 两侧供电电压不能超过 5.5V。连接时注意
电源电压极性，否则会造成芯片损坏。
2. 函数发生器输出一定频率和幅值的信号，连接输入端 TXD；注意该频率不能超过 500kHz。
3. 通过示波器测量 CANH，CANL，TXD，RXD 的信号。


# 6.测试示例
图 为在评估板上所测的数字隔离器 CA-IS3050U 的典型输入和输出波形。输入电源电源电压
VCC1=VCC2=5.0 V。输入信号 TXD 频率为 1MHz，幅度为 3.3V，占空比为 50%的方波。
TXD,CANH,CANL,RXD 信号如下图所示。


#  重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

