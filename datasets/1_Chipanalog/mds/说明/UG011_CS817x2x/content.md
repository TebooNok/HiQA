 # CS817x2x 超低功耗数字隔离器EVM 使用说明


#  1. 描述
该文档描述了由 Chipanalog 设计的 CS817x2x 系列产品的 EVM 的特性及使用。给客户提供了 EVM 的使
用配置，包括原理图，PCB 走线，BOM 及一些测试波形及特性曲线
CS817x2x 的 EVM 适用于 CS817x2x 系列的产品验证。
CS817x2x 的 EVM 使用简单，通过跳线可实现很多配置。在 EVM 上放置了很多检测点，易于测试。
通过一些元器件的修改，可以实现该系列产品料号的验证。
表 1 可订购料号表
---table begin---
Table tile:UG011_CS817x2x可订购料号表
| 料号         | 一侧输入通道数 | 二侧输入通道数 | 默认输出电压 | 封装     |
|--------------|----------------|----------------|--------------|----------|
| CS817x20LS   | 2              | 0              | 低           | SOIC8-NB |
| CS817x20HS   | 2              | 0              | 高           | SOIC8-NB |
| CS817x22LS   | 1              | 1              | 低           | SOIC8-NB |
| CS817x22HS   | 1              | 1              | 高           | SOIC8-NB |
---table end---


#  1. 1.不同料号 EVM 跳线配置
表 2 
---table begin---
Table tile:UG011_CS817x2x不同料号 EVM 跳线配置表
| 料号         | 跳线帽   | 输出电容上料 |
|--------------|----------|--------------|
| CS817x20LS   | J8, J10  | C11, C12     |
| CS817x20HS   | J8, J10  | C11, C12     |
| CS817x22LS   | J2, J10  | C5, C12      |
| CS817x22HS   | J2, J10  | C5, C12      |
---table end---

# 2. 特征
具有信号连接 SMA 端子以及电源接口方便连接。
具有跳线接口方便配置。
具有测试点方便测试。



# 3 .测试需要的仪器及配置
表 3 测试需要的仪器及配置
---table begin---
Table tile:UG011_CS817x2x测试需要的仪器及配置表
|名称: CS817x2x EVM

要求:
- 电源: 2.5V~5.5V 输入范围，可提供 200mA 的电源。
- 示波器: 4 通道，200MHz 带宽。
- 数字万用表（DMM）: 6.5 位数字万用表。
- 信号发生器（AFG）: 可产生 100kHz 方波型号。
---table end---


# 4 .EVM 配置及其注意事项
图 2 为 CS817x22HS EVM 的线路图。该线路图含有从 TP1 至 TP8 编号的测试点对以及从 J1 至 J12 的跳线
座，以支持在该板上对产品进行验证。
T1 至 T4 为连接香蕉头测试线的测试座。在验证芯片时，注意连接电源极性以及电源的电压范围，保证
施加电压不能超过最大承受值，否则会造成芯片损坏。
S1,S2,S5 和 S6 为测试 SMA 座，通过 BNC-SMA 线缆将信号发生器(AFG)和 EVM 的输入信号连接在一起。


# 5. EVM 的线路图


# 6. PCB 设计图


# 7. EVM 的元件清单
表 4 CS817x22HS EVM 的元件清单
---table begin---
Table tile:UG011_CS817x2xEVM 的元件清单表
| Item | 元件编号 | 数量 | 描述                                    | 封装              | MFR Part Number       |
|------|----------|------|-----------------------------------------|-------------------|------------------------|
| 1    | T1,T2,T3,T4 | 4  | CONN Banana Jack Solder                | -                 | Keystone 575-4        |
| 2    | FBL1,FBL2,,FBL3,,FBL4 | 4  | Beed 600Ohm 1206                      | FH CBG321609U601T | -                    |
| 3    | C1, C7   | 2  | Tantalum cap,22uF 7343                 | AVX TAJD226K025RNJ | -                  |
| 4    | C2,C8    | 2  | MLCC 10uF/10V, X7R 0603 - standard    | -                 | -                    |
| 5    | C3,C9    | 2  | MLCC 1uF/10V, X7R 0603 - standard    | -                 | -                    |
| 6    | C3-1,C4-1,C9-1,C10-1 | 0  | NC 0603 - standard                   | -                 | -                    |
| 7    | C4,C10   | 2  | MLCC 0.1F/10V, X7R 0603 - standard  | -                 | -                    |
| 8    | C5,C6,C11,C12 | 4  | MLCC 15pF/50V, X7R 0603 - standard  | -                 | -                    |
| 9    | R1,R2,R3,R4 | 4  | SMD resister 0R,1% 0603 - standard | -                 | -                    |
| 10   | S1,S2,S5,S6 | 4  | SMA connector -                       | Wurth Elektronik 60312202114509 | - |
| 11   | TP1,TP3,TP5,TP7 | 4  | Test Point, Red, 0.040"             | Keystone 5000     | -                    |
| 12   | TP2,TP4,TP6,TP8 | 4  | Test Point, Black, 0.040"           | Keystone 5001     | -                    |
| 13   | U1       | 1  | CS817x22HS SOP8                       | -                 | Chipanalog CS817x22HS |
| 14   | J1,J2,J3,J4,J7,J8,J9,J10 | 8  | Header, 3 pin, 100mil           | -                 | -                    |
| 15   | J5,J6,J11,J12 | 4  | Header, 2 pin, 100mil            | -                 | -                    |

---table end---


#  8. 快速使用说明
该 EVM 使用说明适用于 CS817x22HS。
硬件连接：
如图所示，可以将电源，信号发生器，示波器和 EVM 连接在一起。
1. 分别将电源连接至 EVM 的一侧和二测，接线端子对分别为 T1/T2 和 T3/T4。
2. 将信号发生器通过 BNC-SMA 线缆和 EVM 的输入信号连接在一起。S2 和 S5 为输入信号端子。
3. 将 S1 和 S6 连接至示波器观察隔离器输出波形。


#  10.重要声明
上述资料仅供参考使用，用于协助 Chipanalog 客户进行设计与研发。Chipanalog 有权在不事先通知
的情况下，保留因技术革新而改变上述资料的权利。

