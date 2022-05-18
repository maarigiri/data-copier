import pandas as pd
import os

# GETTING THE ABSOLUTE FILE PATH
dir_path = 'C:\\Users\\giri.prasad\\Research\\data\\retail_db_json\\'
table_name = 'orders\\'
file_path = dir_path + table_name
list_dir = os.listdir(file_path)[0]
absolute_path = file_path + '\\' + list_dir
print(absolute_path)
# getting connection of the database
conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'

# reading the data from the json file
df = pd.read_json(absolute_path, lines=True, chunksize=1000)


# inserting the data to the database
for index in df:
    min_value = index['order_id'].min()
    max_value = index['order_id'].max()
    print('inserting the data from values ' + str(min_value) + ' to values ' + str(max_value))
    index.to_sql('orders', conn, if_exists='append', index=False)

# validating if the data got inserted or not
print(pd.read_sql('select count(1) from orders', conn))

