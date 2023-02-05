import pandas as pd
import math


def get_dataframe(filepath):
    df = pd.read_csv(filepath)
    grouped = df.groupby(["date", "member_number"]).agg({"item_name": lambda x: ",".join(x)})
    grouped = grouped.rename(columns={'item_name': 'item_list'})
    grouped['order_id'] = range(1, len(grouped) + 1)
    result = grouped.reset_index()
    result = result[['order_id', 'date', 'member_number', 'item_list']]
    result['month'] = pd.to_datetime(result['date']).dt.month
    result.to_csv("./output/result.csv")
    return result


def form_number_table(result, min_support_percentage = 5):
    support = dict()
    for i in range(len(result)):
        for item in result.loc[i,'item_list'].split(','):
            if item not in support:
                support[item] = 1
            else:
                support[item] += 1

    min_support_count = math.floor(len(result)*min_support_percentage/100)

    items = [ (item, count) for (item, count) in support.items() if count >= min_support_count]
    items = sorted(items, key = lambda x: x[1])

    number_table = dict() # Sorted frequent number table (Mapping)
    for i, (item, count) in enumerate(items):
        number_table[item] = (i+1)
    
    return number_table


def get_sfd_list(result, number_table):
    SFD_list = dict()

    grouped = result.groupby(by='month')
    for month, data in grouped:
        #TODO: decide data.to_csv(f'./output/dataset_{month}.csv', index=False)
        SFD = dict()
        for i in data.index:
            itemset = list()
            item_list = data['item_list'][i].split(',')
            for (item, item_number) in number_table.items():
                if item in item_list:
                    itemset.append(item_number)
            SFD['T'+str(data['order_id'][i])] = itemset
        SFD_list[str(month)] = SFD

    return SFD_list


if __name__ == '__main__':
    df = get_dataframe("./input/groceries_dataset.csv")
    number_table = form_number_table(df, 5)
    sfd_list = get_sfd_list(df, number_table)

