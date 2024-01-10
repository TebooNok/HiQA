 # CA-IS1044S隔离式CAN收发器测试板说明


# 1.描述
此份文件描述了 CA-IS1044S 隔离式 CAN 收发器评估板的使用方法。使用户可以评估芯片性能且对
隔离系统进行系统性分析，从而提高开发速度。


# 2.芯片简介
CA-IS1044S 是一款隔离式控制区域网络(CAN)物理层收发器，符合 ISO11898-2 标准的技术规范。此
器件采用片上二氧化硅(SiO2)电容作为隔离层，在 CAN 协议控制器和物理层总线之间创建一个完全隔离
的接口，与隔离电源一起使用，可隔绝噪声和干扰并防止损坏敏感电路。
CA-IS1044S 可为 CAN 协议控制器和物理层总线分别提供差分接收和差分发射能力，信号传输速率
最高可达 5 Mbps。该器件具有限流、过压和接地损耗保护(–58 V 至 58 V)以及热关断功能，可防止输出
短路，共模电压范围为–30 V 至 30 V。
CA-IS1044S 额定温度范围为–40°C 至 125°C，提供窄体 SOIC8-NB 封装。


#  3.物料清单
---table begin---
Table tile:UG015_CA-IS1044S物料清单表
| Item | Ref Des       | Qty | Description                         | Package | MFR PN                       |
|------|---------------|-----|-------------------------------------|---------|------------------------------|
| 1    | CON1,CON2     | 2   | CONN, 5.08mm, Rising Cage Clamp     | -       | Wurth Elektronik 691236510002 |
| 2    | C1, C6        | 2   | Tantalum cap, 22uF 7343            | -       | AVX TAJD226K025RNJ            |
| 3    | C2, C7, C4, C9| 2   | MLCC, 100nF/10V, X7R 0603           | Standard| -                            |
| 4    | C3, C8        | 2   | MLCC, 1μF/10V, X7R 0603            | Standard| -                            |
| 5    | C5            | 1   | MLCC, 15pF/10V, X7R 0603           | Standard| -                            |
| 6    | C10           | 1   | MLCC, 50pF/10V, X7R 0603           | Standard| -                            |
| 7    | C11           | 1   | MLCC, 4.7nF/10V, X7R 0603          | Standard| -                            |
| 8    | J1, J2        | 2   | Header, 3 pin, 2.54mm              | -       | Standard                     |
| 9    | J3, J4        | 2   | Header, 3 pin, 2.54mm              | -       | Standard                     |
| 10   | R1, R2        | 2   | SMD resister, 30Ω, 1% 1206         | Standard| -                            |
| 11   | S1, S2, S3, S4| 4   | SMA Connect, 2.54mm                | -       | Standard                     |
| 12   | TP1, TP3, TP7,| 4   | Test Point, Yellow,                | -       | Keystone 5009                |
|      | TP9           |     | Through Hole, 1mm                 |         |                              |
| 13   | TP2, TP4, TP6,| 6   | Test Point, Black,                 | -       | Keystone 5001                |
|      | TP8, TP10, TP12|     | Through Hole, 1mm                 |         |                              |
| 14   | TP5, TP11     | 2   | Test Point, Red,                   | -       | Keystone 5005                |
|      |               |     | Through Hole, 1mm                 |         |                              |
| 15   | S1, S2, S3, S4| 4   | SMA Connector, 2.54mm              | -       | Standard                     |
| 16   | U1            | 1   | Isolated CAN transceiver           | -       | Chipanalog CA-IS1044S         |
| 17   | PCB           | 1   | Two layers PCB, FR-4,              | -       | PCB-A010-02, 1.6mm thickness  |
|      |               |     | -                                   |         |                              |
---table end---


# 4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、高频信号发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1 和 CON2；注意隔离 CAN 两侧供电电压不能超过 5.5V。
2. 函数发生器输出一定频率和幅值的信号，连接输入端 TXD；注意该频率不能超过 1MHz。
3. 通过示波器测量 CANH，CANL，TXD，RXD 的信号。


# 6.测试示例
图 为在评估板上所测的数字隔离器 CA-IS1044S 的典型输入和输出波形。输入电源电源电压
VCC1=VCC2=5.0 V。输入信号 TXD 频率为 1MHz，幅度为 3.3V，占空比为 50%的方波。
TXD,CANH,CANL,RXD 信号如下图所示。


#  重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

