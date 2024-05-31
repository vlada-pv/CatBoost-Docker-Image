import pandas as pd

drop_col = ['mrg_', 'регион', 'client_id', 'зона_1', 'зона_2', 'pack_freq', 'сумма', 'сегмент_arpu', 'частота', 'использование', 'pack', 'продукт_2', 'продукт_1']

def import_data(path_to_file):

    input_df = pd.read_csv(path_to_file).drop(columns=drop_col)

    return input_df

def run_preproc(input_df):

    output_df = input_df
    output_df['частота_пополнения'].fillna(0, inplace=True)
    output_df['объем_данных'].fillna(0, inplace=True)
    output_df['on_net'].fillna(0, inplace=True)
    output_df['доход'].fillna(output_df['доход'].mean(), inplace=True)

    return output_df