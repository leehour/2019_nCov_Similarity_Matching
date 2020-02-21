import numpy as np
import pandas as pd

import configs

train_origin_file = pd.read_csv(configs.train_file)
test_process_df = pd.read_csv('datasets/dev.csv')

train_df = train_origin_file.dropna()

# 切分训练集和验证集，比例7:3，官方的验证集作为测试集
train_process_df = train_df[:int(0.7 * len(train_df))]
dev_process_df = train_df[int(0.7 * len(train_df)):]

train_df.to_csv(configs.train_process_file, header=None, index=None)
dev_process_df.to_csv(configs.dev_process_file, header=None, index=None)
test_process_df.to_csv(configs.test_process_file, header=None, index=None)