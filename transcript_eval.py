import pandas as pd

# 文件路径常量定义
# 你需要更改为你自己的正确路径
INPUT_FILE = '成绩表.csv'
OUTPUT_FILE = '成绩表-历史均分.csv'

# 读取CSV文件，并处理空值
print(f"正在读取{INPUT_FILE}...")
df = pd.read_csv(INPUT_FILE).fillna(0)
print(f"成功读取 {len(df)} 条成绩记录")


df['学分'] = pd.to_numeric(df['学分'], errors='coerce').fillna(0)
df['最终成绩'] = pd.to_numeric(df['最终成绩'], errors='coerce').fillna(0)

# 计算加权成绩
df['加权成绩'] = df['学分'] * df['最终成绩']

# 初始化累计加权平均分列
df['累计加权平均分'] = 0.0

# 计算累计加权平均分
print("\n开始计算累计加权平均分...")
total_weighted_score = 0
total_credits = 0

for i in range(len(df) - 1, -1, -1):
    total_weighted_score += df.loc[i, '加权成绩']
    total_credits += df.loc[i, '学分']
    df.loc[i, '累计加权平均分'] = total_weighted_score / total_credits if total_credits != 0 else 0
print("累计加权平均分计算完成")

# 初始化累计算术平均分列
df['累计算术平均分'] = 0.0

# 计算累计算术平均分
print("\n开始计算累计算术平均分...")
total_final_score = 0
total_courses = 0

for i in range(len(df) - 1, -1, -1):
    total_final_score += df.loc[i, '最终成绩']
    total_courses += 1
    df.loc[i, '累计算术平均分'] = total_final_score / total_courses if total_courses != 0 else 0
print("累计算术平均分计算完成")

# print(df)

#保存结果到新的CSV文件
df.to_csv(OUTPUT_FILE, index=False)
print(f"处理完成！结果已保存到 '{OUTPUT_FILE}'")