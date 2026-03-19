import pandas as pd
from pyzabbix import ZabbixAPI

# --- CONNECTION SETTINGS ---
ZABBIX_URL = 'http://127.0.0.1/zabbix' # Your zabbix server url URL
USER = 'Admin' # Admin Login
PASSWORD = 'zabbix'  #Admin Password

# Connect to API
zapi = ZabbixAPI(ZABBIX_URL)
zapi.login(USER, PASSWORD)
print("successfully connected to Zabbix API")

# READ YOUR PREPARED CSV
# raw: host_name, host_ip, group_name, template_name
df = pd.read_csv('zabbix_dev_list.csv') # your file .csv with devices

for index, row in df.iterrows():
    try:
        # 1. Get group ID using name
        group = zapi.hostgroup.get(filter={"name": row['group_name']})
        if not group:
            print(f"Group {row['group_name']} not found!")
            continue
        group_id = group[0]['groupid']

        # 2. Get template ID  by name
        template = zapi.template.get(filter={"host": row['template_name']})
        if not template:
            print(f"Template {row['template_name']} not found")
            continue
        template_id = template[0]['templateid']

        # 3. Creating a host
        zapi.host.create(
            host=row['host_name'],
            interfaces=[{
                "type": 1, # 1 -  Agent, 2 - SNMP 
                "main": 1,
                "useip": 1,
                "ip": row['host_ip'],
                "dns": "",
                "port": "10050"
            }],
            groups=[{"groupid": group_id}],
            templates=[{"templateid": template_id}]
        )
        print(f"Device {row['host_name']} successfully added.")

    except Exception as e:
        print(f"Error adding {row['host_name']}: {e}")

zapi.logout()
