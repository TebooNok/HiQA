 # CA-IF4023 AISG 测试板说明


#  1. 芯片产品特性
• 单电源电压范围： 3V 至 5.5V 
• 独立逻辑电源：1.6V 至 5.5V 
• 接收机具有 –15dBm 至 +5dBm 的宽输入动态范围
• 发射机输出功率可在 5.4dBm 至 12dBm 范围内调节
• 符合 AISG 3.0 标准的发射特性
• 低功耗待机模式
• 针对 RS-485 总线仲裁的方向控制
• 支持所有 AISG 信号速率：9.6kbps、38.4kbps、
115.2kbps 
• 片上集成中心频率 2.176MHz 的有源带通滤波器
• 3mm × 3mm 16 引脚四方扁平无引线 (QFN) 封装
• -55℃~125℃的工作温度范围


# 2. 芯片应用
• AISG-针对天线线路器件的接口
• 塔顶放大器 (TMA)
• 通用调制解调器 (Modem) 接口


# 3. 芯片概述
CA-IF4023 是一款符合 AISG 3.0 标准的全集成收发
机。
CA-IF4023 接收机具有 20dB 的输入动态范围，集成
一个中心频率为 2.176MHz 的窄带有源带通滤波器，保
证即使在有干扰信号的情况下，接收机仍然有能力解调
出有用信号。
CA-IF4023 发射机同样集成了中心频率为 2.176MHz
的窄带有源带通滤波器，保证输出频谱满足 AISG 3.0 标
准，输出功率在 5.4dBm 至 12dBm 范围内可通过片外电
阻调节以补偿同轴电缆上的功率损失。
CA-IF4023 支持针对 RS-485 总线仲裁的方向控制功
能，支持片外晶体、振荡器或其他片外时钟源输入。
器件信息
---table begin---
Table tile:UG027_CA-IF4023 AISG器件信息表
| 零件号     | 封装类型  | 封装尺寸（标称值） |
| ---------- | --------- | ------------------ |
| CA-IF4023  | QFN16     | 3mm x 3mm          |

---table end---


# 4. 芯片引脚功能描述
表 4-1 CA-IF4023 引脚功能描述
---table begin---
Table tile:UG027_CA-IF4023 AISG引脚功能描述表
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


# 5. 测试电路板
CA-IF4023 测试评估板提供测试评估 CA-IF4023 使用。
评估板有两颗 CA-IF4023 芯片，当一个作为发射机时，另一个就是接收机
# 5.1. 元器件列表
表 5-1 元器件 BOM
---table begin---
Table tile:UG027_CA-IF4023 AISG元器件 BOM表
| Designator  | Footprint | DESCRIPTION                                     |
|-------------|-----------|-------------------------------------------------|
| C1,C2,C3,C4 | 0805    | 10μF±10%, 10V X5R ceramic capacitors          |
| C5,C7,C11,C13 | 0603  | 0.1μF±10%, 16V X7R ceramic capacitors        |
| C6,C8,C9,C10 | 0603  | 39pF ±5%, 50V C0G ceramic capacitors          |
| C12,C14     | 0603    | 470pF±10%, 16V X7R ceramic capacitors        |
| C15,C16     | 0603    | 1μF±10%, 16V X7R ceramic capacitors         |
| C17,C18     | 0603    | NO CONNECT                                     |
| H1,H2,H3,H4 | TH158D80 | 支撑铜柱，连接 GND                           |
| J1,J2,J3,J4 | SMA_5   | SMA 连接器，直角                               |
| JP1, JP2, JP3, JP4, JP5, JP6, JP7, JP8 | JCON2 | 2-pin headers，间距 2.54mm         |
| JU1, JU2, JU3, JU4, JU5, JU6, JU7, JU8 | JUCON3 | 3-pin headers，间距 2.54mm      |
| L1,L2       | R0805   | 实际焊接，100nF±10%的隔直电容                  |
| OS1, OS2    | CYSTAL_8M | 香港晶振，频率 8.704M                           |
| R1, R2      | 0603    | 1k±5% resistors                                |
| R3,R5,R15,R16 | 0603 | 10k±1% resistors                               |
| R4,R8       | 0603    | 49.9R ±1% resistors                            |
| R7,R10      | 0603    | NO CONNECT                                     |
| R11,R13     | 0603    | 4.12k±1% resistors                             |
| R12,R14     | VR      | 直插 50K±1%，变阻器                          |
| TP1,TP2,TP3,TP4,TP5,TP6,TP7,TP8,TP9,TP10,TP11,TP12,TP13,TP14,TP15,TP16 | TP | 测试点  |
| U1, U2      | QFN16   | CA–IF4023                                      |
---table end---


# 5.2. 快速测试需求仪器
表 5-2 硬件仪器列表
---table begin---
Table tile:UG027_CA-IF4023 AISG硬件仪器列表
1. CA-IF4023**：测试评估板，用于测试评估芯片。
2.3.3V/5V 直流电源**：测试开发板提供激励的直流电源。
3. 信号发生器**：用于提供信号激励。
4. 双通道示波器**：用于测试时序、输入输出信号，并监测信号的波形和特性。
5. 频谱仪**：用于测试发射输出的频谱，以分析输出信号的频率分布和特性。
---table end---


# 5.3. 电路板原理图
# 5.4. 电路板叠层
# 5.5. 测试元器件功能说明
表 5-1 元器件功能说明
---table begin---
Table tile:UG027_CA-IF4023 AISG元器件功能说明表
- U1, U2**：CA-IF4023 AISG 器件
- TP1, TP3**：SYNCOUT 测试端子
-JP4, JP6**：SYNCOUT 上拉 1K 电阻跳线（上拉到 VCC），默认短接
- R1, R2**：SYNCOUT 1kΩ 上拉电阻
- TP2, TP5**：TXIN 测试端子
- TP6, TP9**：RXOUT 测试端子
- TP8, TP10**：DIR 测试端子
- JU3, JU5**：DIRMOD 上拉或下拉跳线，默认跳线的 1 脚和 2 脚短接，设置数据速率见表 8-2 真值表。
- JU4, JU7**：DIRMOD 上拉或下拉跳线，默认跳线的 1 脚和 2 脚短接，设置数据速率见表 8-2 真值表。
- R15, R16**：RES 到地之间的 10kΩ 电阻
- JU6, JU8**：RES 到 BIAS 之间电阻选择跳线，跳线 1 脚和 2 脚短接，接入 4.12kohm 固定电阻，跳线 2 脚和 3 脚短接，接入可变电阻，默认跳线的 1 脚和 2 脚短接，RES 输出 1.064V
- R12, R14**：RES 和 BIAS 之间可变电阻器
- C15, C16**：BIAS 和地之间 1μF 电容
- R4, R8**：TXOUT 和 RXIN 之间 49.9ohm 电阻
- C17, C18**：TXOUT 和地之间 470pF 滤波电容
- L1, L2**：RXIN 和线缆之间 100nF 交流耦合电容
- C12, R7, C14, R10**：未安装元件
- TP17, TP18**：TXOUT 测试端子
- JU1，JU2**：选择晶振和外部时钟跳线，默认跳线 1 脚和 2 脚短接，选择板上晶振提供时钟
- J1, J2**：外部时钟输入 SMA 接口
- R3, R5**：外部时钟和 XTAL1 之间串联 10kohm 电阻
- OS1, OS2**：板上晶振
- C9, C10**：XTAL1 和地之间 39pF 电容
- C6, C8**：XTAL2 和地之间 39pF 电容
- JP3, JP5**：XTAL2 和地之间跳线。默认当使用板上晶振时，跳线开路，如果使用外部时钟，跳线短接
- JP1, JP2**：VCC 和 VL 之间跳线，默认短接使用同一个直流电源
- C5, C7**：VCC 管脚 0.1μF 去耦电容
- C11, C13**：VL 管脚 0.1μF 去耦电容
- C2, C4**：VCC 电源 10μF 去耦电容
- C1, C3**：VL 电源 10μF 去耦电源
- JP7**：U1 和 U2 之间线缆跳线，默认短接，此时不需要外接线缆
- H1,H2,H3,H4**：U1 GND 测试端子
- JU14**：U1 和 U2 之间地跳线，默认短接共
---table end---


# 5.6. 真值表
表 5-2 DIRMD1 和 DIRMD2 功能定义
---table begin---
Table tile:UG027_CA-IF4023 AISG DIRMD1 和 DIRMD2 功能定义 表
| DIRMD2 | DIRMD1 | AISG 数据速率 (kbps) | 单位位时间 (us) |
| ------ | ------ | --------------------- | ---------------- |
| 0      | 0      | 9.6                   | 104.16           |
| 0      | 1      | 38.4                  | 26.04            |
| 1      | 0      | 115.2                 | 8.68             |
| 1      | 1      | Standby2              | Standby2         |

备注:
1. DIRMD1 和 DIRMD2 管脚在芯片内部下拉到地。
2. Standby 模式下 RXOUT 置高，TXOUT 静默态，不响应任何输入信号。
---table end---


# 6.  重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

