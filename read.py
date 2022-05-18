''''import pandas as pd

query = 'select * from orders'
conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
df = pd.read_sql(
    query,
    conn
)
print(type(df))
print(df)
print(df.columns)
print(df.dtypes)
print(df.count())
print(df.describe())'''''


import os

def main():
    DB_NAME = os.environ.get('DB_NAME')
    print(f'hello world from {DB_NAME}')

if __name__ == '__main__':
    main()
