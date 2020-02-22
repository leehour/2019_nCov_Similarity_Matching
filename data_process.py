import numpy as np
import pandas as pd

import configs


def process_file(data_df, target_dir):
    """
    将数据中的每一列用"\t"连接起来保存，方便之后读取
    :param data_df:
    :param target_dir:
    :return:
    """
    train_df = data_df.dropna()
    text_line = []
    for i in range(len(train_df)):
        temp = []
        line = train_df.iloc[i]
        if len(line.index) != 4:
            continue
        temp = "\t".join([str(i) for i in line.values])
        text_line.append(temp)
    with open(target_dir, 'w', encoding='utf-8') as f:
        for line in text_line:
            f.write(line)
            f.write("\n")


if __name__ == '__main__':
    # 切分训练集和验证集，比例7:3，官方的验证集作为测试集
    train_df = pd.read_csv(configs.train_file)
    df_train = train_df[:int(0.7 * len(train_df))]
    df_dev = train_df[int(0.7 * len(train_df)):]
    df_test = pd.read_csv(configs.dev_file)

    process_file(df_train, configs.train_process_file)
    process_file(df_dev, configs.dev_process_file)
    process_file(df_test, configs.test_process_file)

