'''import pandas as pd

def main():

    fp = 'C:\\Users\\giri.prasad\\Research\\data\\retail_db_json\\order_items\\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'
    df = pd.read_json(fp, lines=True)
    #print(df.count())
    #print(df.describe())
    #
    #print(df.columns)
    #
    #print(df.dtypes)
    #
    #
    #print(type(df[['order_items_order_id'and 'order_item_subtotal']]))
    #print(df[['order_items_order_id'and 'order_item_subtotal']])
    #print(df['order_item_order_id'] == 2)
    print(df[df['order_item_order_id'] == 2])

if __name__ == "__main__":
    main()'''''


'''''''# intigrate read and write lpogic'''
'''import os
from code import get_json_reader
from python_write import load_db_table

def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_name = os.environ.get('table_name')
    json_reader = get_json_reader(BASE_DIR, table_name)
    configs = dict(os.environ.items())
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'

    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])



if __name__ == '__main__':
    main()'''''


#develop logic for multiple tables

import os
import sys

from code import get_json_reader
from python_write import load_db_table


def process_table(BASE_DIR, conn, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    print(json_reader)
    for df in json_reader:
        load_db_table(df, conn, table_name, df.columns[0])


def main():
    BASE_DIR = os.environ.get('BASE_DIR')
    table_names = sys.argv[1].split(',')
    configs = dict(os.environ.items())
    print(configs)
    print(table_names)
    conn = f'postgresql://{configs["DB_USER"]}:{configs["DB_PASS"]}@{configs["DB_HOST"]}:{configs["DB_PORT"]}/{configs["DB_NAME"]}'
    print(conn)
    for table_name in table_names:
        process_table(BASE_DIR, conn, table_name)

if __name__ == '__main__':
    main()