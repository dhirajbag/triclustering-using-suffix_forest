import pandas as pd
import math


def get_dataframe(filepath: str):
    df = pd.read_csv(filepath)
    grouped = df.groupby(["date", "member_number"]).agg({"item_name": lambda x: ",".join(x)})
    grouped = grouped.rename(columns={'item_name': 'item_list'})
    grouped['order_id'] = range(1, len(grouped) + 1)
    result = grouped.reset_index()
    result = result[['order_id', 'date', 'member_number', 'item_list']]
    # result['month'] = pd.to_datetime(result['date']).dt.month
    result['month'] = [ date.split('-')[1] for date in result['date']]
    result.to_csv("./output/preprocessed_datset.csv")
    return result


def form_number_table(result, min_support_count):
    support = dict()
    for i in range(len(result)):
        for item in set(result.loc[i,'item_list'].split(',')):
            if item not in support:
                support[item] = 1
            else:
                support[item] += 1

    items = [ (item, count) for (item, count) in support.items() if count >= min_support_count]
    items = sorted(items, key = lambda x: x[1])

    number_table = dict() # Sorted frequent number table (Mapping)
    for i, (item, count) in enumerate(items):
        number_table[item] = (i+1)
    
    return number_table


def get_sfd_list_from_processed_dataframe(result, number_table: dict):
    SFD_list = dict()

    grouped = result.groupby(by='month')
    for month, data in grouped:
        #TODO: decide data.to_csv(f'./output/dataset_{month}.csv', index=False)
        SFD = dict()
        for i in data.index:
            itemset = list()
            item_list = set(data['item_list'][i].split(','))
            for (item, item_number) in number_table.items():
                if item in item_list:
                    itemset.append(item_number)
            SFD['T'+str(data['order_id'][i])] = itemset
        SFD_list[str(month)] = SFD

    return SFD_list

def get_single_sfd(result, number_table):
    SFD = dict()
    for i in result.index:
        itemset = list()
        item_list = set(result['item_list'][i].split(','))
        for (item, item_number) in number_table.items():
            if item in item_list:
               itemset.append(item_number)
        SFD['T'+str(result['order_id'][i])] = itemset
    
    return SFD


def get_number_table_sfd_list_min_sup_count_datatset_size(input_file_path: str, min_sup_percentage = 5):
    df = get_dataframe(input_file_path)
    min_sup_count = math.ceil((len(df)*min_sup_percentage)/100)
    number_table = form_number_table(df, min_sup_count)
    sfd_list = get_sfd_list_from_processed_dataframe(df, number_table)
    return (number_table, sfd_list, min_sup_count, len(df))


if __name__ == '__main__':
    (number_table, sfd_list, dataset_size) = get_number_table_sfd_list_min_sup_count_datatset_size("./input/groceries_dataset.csv", min_sup_percentage=5)

    print(str(sfd_list['1']))
