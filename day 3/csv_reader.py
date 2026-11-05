import csv
def read_csv(file_path):
    data=[]
    with open(file_path,mode='r')as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            yield row

data=read_csv(r"C:\Users\vasu1\OneDrive\Desktop\Internship\day 3\large_dataset.csv")
for row in data:
    print(row)

records=data

def filter_orders(records):
    for row in records:
        if row['order_status']=='Completed':
            yield row

filtered_orders=filter_orders(records)
for order in filtered_orders:
    print(order)