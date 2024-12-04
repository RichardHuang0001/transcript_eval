import pandas as pd
import matplotlib.pyplot as plt

# 读取 CSV 文件
# 你需要更改为你自己的正确路径
file_path = '成绩表-历史均分.csv'
data = pd.read_csv(file_path)

# Reverse the data
data = data.iloc[::-1].reset_index(drop=True)

# 提取需要的数据
x = range(len(data))  # 行号
weighted_avg = data['累计加权平均分']
arithmetic_avg = data['累计算术平均分']

# 绘制图表
plt.figure(figsize=(15, 6))
plt.plot(x, weighted_avg, label='Cumulative Weighted Average', marker='o')
plt.plot(x, arithmetic_avg, label='Cumulative Arithmetic Average', marker='s')

# 设置纵轴刻度为1分间隔
y_min = min(min(weighted_avg), min(arithmetic_avg))
y_max = max(max(weighted_avg), max(arithmetic_avg))
plt.yticks(range(int(y_min), int(y_max) + 1, 1))

# 添加标题和标签
plt.title('Cumulative GPA Line Graph')
plt.xlabel('Curriculum')
plt.ylabel('Score')
plt.legend()

# 显示图表
plt.grid(True)

# 保存图表到当前目录
plt.savefig('GPA_history_linegraph.png')

# 显示图表
plt.show()