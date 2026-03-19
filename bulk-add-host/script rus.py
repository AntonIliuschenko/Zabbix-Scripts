import pandas as pd
from pyzabbix import ZabbixAPI

# --- НАСТРОЙКИ ПОДКЛЮЧЕНИЯ ---
ZABBIX_URL = 'http://127.0.0.1/zabbix' # Замени на свой URL
USER = 'Admin'
PASSWORD = 'zabbix'

# Подключаемся к API
zapi = ZabbixAPI(ZABBIX_URL)
zapi.login(USER, PASSWORD)
print("Успешное подключение к Zabbix API")

# Читаем CSV
# Столбцы: host_name, host_ip, group_name, template_name
df = pd.read_csv('zabbixcam1.csv')

for index, row in df.iterrows():
    try:
        # 1. Получаем ID группы по имени
        group = zapi.hostgroup.get(filter={"name": row['group_name']})
        if not group:
            print(f"Группа {row['group_name']} не найдена!")
            continue
        group_id = group[0]['groupid']

        # 2. Получаем ID шаблона по имени
        template = zapi.template.get(filter={"host": row['template_name']})
        if not template:
            print(f"Шаблон {row['template_name']} не найден!")
            continue
        template_id = template[0]['templateid']

        # 3. Создаем хост
        zapi.host.create(
            host=row['host_name'],
            interfaces=[{
                "type": 1, # 1 - это Agent, для SNMP будет 2
                "main": 1,
                "useip": 1,
                "ip": row['host_ip'],
                "dns": "",
                "port": "10050"
            }],
            groups=[{"groupid": group_id}],
            templates=[{"templateid": template_id}]
        )
        print(f"Устройство {row['host_name']} успешно добавлено.")

    except Exception as e:
        print(f"Ошибка при добавлении {row['host_name']}: {e}")

zapi.logout()
