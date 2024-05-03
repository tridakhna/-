# загрузка библиотек
import pandas as pd
#открытие файла тхт
with open (f'LLP_Genomed_Ayr_OVNG50V02_20230213_FinalReport.txt') as data:
    #построчное чтение файла
    dataset = [line for line in data.readlines()]
    #cоздание списка, в котором удален знак переноса строки 
    n = len(dataset)
    dataset_n = [dataset[i].replace('\n', '') for i in range(n)]
    ind = dataset_n.index('[Data]')
    dataset_n = dataset_n[ind+1:]
    n = len(dataset_n)
    dataset_t = [dataset_n[i].split('\t') for i in range(n)]
    # представление элемента как таблицу pandas
    dataset_df = pd.DataFrame(dataset_t[1:], columns=dataset_t[0])
    dataset_df = dataset_df[['SNP Name', 'Sample ID', 'Allele1 - AB', 'Allele2 - AB']]
    #объединение столбцов с аллелями генов
    dataset_df['Allele - AB'] = dataset_df[['Allele1 - AB', 'Allele2 - AB']].agg(''.join, axis=1)
    dataset_df = dataset_df.drop(['Allele1 - AB', 'Allele2 - AB'], axis=1)
    #создание таблицы с нужными параметрами
    pivot_dataset = pd.pivot_table(dataset_df,
                                   values='Allele - AB',
                                   index='Sample ID',
                                   columns = 'SNP Name',
                                   aggfunc = lambda x: ''.join(x))
    #создание таблицы в json
    dataset_json = pivot_dataset.to_json(f'LLP_Genomed_Ayr_OVNG50V02_20230213_FinalReport_Mod.json', orient='index', indent=4)

    
    

