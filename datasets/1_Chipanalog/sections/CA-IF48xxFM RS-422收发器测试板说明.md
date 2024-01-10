 # CA-IF48xxFM RS-422收发器测试板说明


# 1.描述
此份文件描述了 CA-IF48xxFM 系列 RS-422 收发器评估板的使用方法。使用户可以评估芯片性能且
系统进行系统性分析，从而提高开发速度。


# 2.芯片简介
CA-IF4805FM、CA-IF4820FM、CA-IF4850FM RS-422 收发器。CA-IF4805FM、CA-IF4820FM、CA￾IF4850FM 收发器工作于全双工模式。
CA-IF4805FM、CA-IF4820FM、CA-IF4850FM RS-422 收发器采用 8 引脚 MSOP8 封装最高传输速率可
达 50Mbps。
该 EVM 可以用于 CA-IF4805FM、CA-IF4820FM、CA-IF4850FM 的验证。
主要区别如下表所示：
---table begin---
Table tile:UG025_CA-IF48xxFM RS-422EVM 可以用于 CA-IF4805FM、CA-IF4820FM、CA-IF4850FM 的验证表
| 型号         | 传输速度 (Mbps) | 封装    |
|--------------|-----------------|---------|
| CA-IF4805FM | 0.5             | MSOP8   |
| CA-IF4820FM | 20              | MSOP8   |
| CA-IF4850FM | 50              | MSOP8   |
---table end---


# 3.物料清单
---table begin---
Table tile:UG025_CA-IF48xxFM RS-422物料清单表
| Item Ref Des | Qty | Description                                        | Package                | MFR PN                         |
|--------------|-----|----------------------------------------------------|-------------------------|--------------------------------|
| 1 U1         | 1   | RS-422 transceiver                                | MSOP8                   | Chipanalog CA-IF4805FM        |
| 2 C1         | 1   | Tantalum cap, 22uF                               | 7343                    | AVX TAJD226K025RNJ            |
| 3 C2         | 1   | MLCC, 10uF/10V, X7R                              | 0805                    | - Standard                    |
| 4 C3         | 1   | MLCC, 1uF/10V, X7R                               | 0603                    | - Standard                    |
| 5 C4         | 1   | MLCC, 100nF/10V, X7R                            | 0603                    | - Standard                    |
| 6 C5         | 1   | MLCC, 50pF/10V, X7R                              | 0603                    | Standard                       |
| 7 C6         | 0   | NC                                                 | 0603                    | - Standard                    |
| 8 R1, R2     | 2   | SMD res, 1206, 1%, 27R                           | 1206                    | - Standard                    |
| 9 S1, S2, S3, S4, S5, S6 | 6 | SMA Connector                           | -  | - Standard                  |
| 10 TP1, TP3, TP5, TP7, TP9, TP11, TP13 | 7 | Test Point, Red, Through Hole, 1mm | Keystone 5005  | -                |
| 11 TP2, TP4, TP6, TP8, TP10, TP12, TP14 | 7 | Test Point, Black, Through Hole, 1mm | Keystone 5006 | -             |
| 12 CON1       | 1   | CONN, 5.08mm, Rising Cage Clamp                 | Wurth Elektronik 691236510002 | - |
| 13 J1, J2    | 2   | Header, 3 pin, 2.54mm                            | -                       | - Standard                    |
| 14 J3        | 1   | Header, 2 pin, 2.54mm                            | -                       | - Standard                    |
| 15 PCB-A32-00 | 1  | Two layers PCB, FR-4, 1.6mm thickness           | -                       | - Standard                    |
---table end---


#  4.测试仪器
直流电源、500MHz 带宽示波器安捷伦 DSOX3054T、高频信号发生器等。


# 5.硬件连接
1. 将直流电压源连接到 CON1；注意隔离 RS-422 供电电压不能超过 5.5V。
2. 函数发生器输出一定频率和 5.0V 幅值的方波信号，连接输入端 DI；注意该频率不能超过
250kHz。
3. 通过示波器测量 DI，A，B，RO 的信号。



# 6.测试示例
图 为在评估板上所测的 CA-IF4805FM 典型输入和输出波形。输入电源电源电压 VCC =5.0 V。输入信
号 DI 频率为 250kHz，幅度为 5.0V，占空比为 50%的方波。将引脚 A 和 Y 短接在一起，将引脚 B 和 Z 短
接在一起。DI，Y，Z，RO 信号如下图所示。


# 7. 重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。
http://www.chipanalog.com
