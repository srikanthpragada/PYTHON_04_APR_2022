data = ['Steve,9898776653', 'Scott,8788887764','Steve,7676767676',
        'Tom,87987999999', 'Bill,7367373733','Bill,8788888777']

customers = {}

for entry in data:
        name, mobile = entry.split(",")
        customers[name] = mobile


for name, mobile in customers.items():
        print(f"{name:15} {mobile}")

