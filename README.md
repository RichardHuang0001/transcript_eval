# 学业成绩分析工具

一个基于Python的学业成绩分析工具，用于处理学业成绩数据并生成GPA历史可视化图表。该工具可以处理CSV格式的成绩单，计算加权平均分和算术平均分，并生成直观的成绩走势图。

## 快速开始
1.确保你的电脑上有安装python环境，检查方法：（Win+R,输入cmd；Mac/Linux打开终端）在命令行输入
python --version
如果输出3.x.x的版本号，则说明python环境已安装。

2.安装python包：pandas, matplotlib
命令行输入：
pip install pandas matplotlib

3.下载代码：
进入你想要放置代码的文件夹（例如/Desktop/Dir），复制该文件夹的路径，打开终端，输入：
cd /path/to/your/folder
然后
git clone https://github.com/RichardHuang0001/transcript_eval.git

4.准备好你的成绩表.CSV，以类似的格式覆盖掉示例文件，只需要确保有“学分”和“最终成绩”两列即可，其他列可以随意。
（HIT操作方法：从教务网站选择100条/页，直接复制表格到Office中，另存为CSV格式）

5.运行脚本：
确保终端当前路径为代码所在路径（transcript_eval），运行脚本：
建议成绩表放在transcript_eval文件夹下，运行：
python transcript_eval.py
你会看到生成了历史均分的csv文件

6.运行GPA走势图脚本：
python GPA_history_linegraph.py
你会看到生成了GPA走势图

## 主要功能

- 处理CSV格式的成绩记录
- 计算累计加权平均分（考虑学分权重）
- 计算累计算术平均分
- 生成GPA历史走势图
- 导出处理后的成绩数据
- 保存可视化图表

## 环境要求

- Python 3.x
- 需要安装的Python包：
  - pandas
  - matplotlib

可以使用pip安装所需包： 

pip install pandas matplotlib

## 文件结构

- `transcript_eval.py` - 成绩处理主脚本
- `GPA_history_linegraph.py` - GPA历史走势图生成脚本
- 输入文件：包含学业成绩的CSV文件（放在与代码同一目录下，则不需要修改代码）
- 输出文件：
  - 包含历史均分的处理后CSV文件
  - GPA走势图PNG文件

## 输入文件格式

输入的CSV文件需要包含以下列：
- 学分
- 最终成绩

## 使用方法

1. 准备包含学业成绩的CSV文件
2. 在两个脚本中更新文件路径
3. 运行成绩处理脚本：


### 输出效果：
- 生成包含历史均分的CSV文件
- 生成可视化走势图

## 注意事项

1. 使用前请确保更新脚本中的文件路径
2. 输入CSV文件需要包含必要的列（学分、最终成绩）
3. 确保输入数据格式正确，避免非数字内容

## 许可证

MIT License

## 问题反馈

如果您在使用过程中遇到任何问题，或有任何改进建议，欢迎提出issue。

## 作者

[HuangWei]
