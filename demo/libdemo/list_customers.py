import re

f = open("customers.txt", "rt")

customers = {}
for line in f.readlines():
    m_name = re.search('[A-Za-z ]+', line)
    if m_name is None:
        continue

    name = m_name.group(0).strip()
    if len(name) == 0:
        continue

    m_mobile = re.search(r'\d+', line)
    if m_mobile is None:
        continue

    mobile = m_mobile.group(0)

    customers[name] = mobile

f.close()

for name, mobile in sorted(customers.items()):
    print(f"{name:30} {mobile}")
