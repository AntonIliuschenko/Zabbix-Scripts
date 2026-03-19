from pyzabbix import ZabbixAPI

# ---------- НАСТРОЙКИ ----------
ZABBIX_URL = "http://127.0.0.1/zabbix"
USER = "Admin" #Ваш логин админа
PASSWORD = "PASSWORD" #Ваш пароль к учетной записи 

GROUP_NAME = "Camera" #Ваше название группы

# ---------- ПОДКЛЮЧЕНИЕ ----------
zapi = ZabbixAPI(ZABBIX_URL)
zapi.login(USER, PASSWORD)

print("Connected to Zabbix API")

# ---------- НАЙТИ ГРУППУ ----------
group = zapi.hostgroup.get(filter={"name": GROUP_NAME})

if not group:
    print(f"Group {GROUP_NAME} not found.")
    exit()

group_id = group[0]['groupid']

print(f"Group found: {GROUP_NAME} (ID {group_id})")

# ---------- ПОЛУЧИТЬ ВСЕ ХОСТЫ ----------
hosts = zapi.host.get(groupids=group_id)

if not hosts:
    print("No hosts in this group.")
    exit()

print(f"Found {len(hosts)} hosts. Deleting...")

# ---------- СОБИРАЕМ HOST IDS ----------
host_ids = [host['hostid'] for host in hosts]

# ---------- УДАЛЯЕМ ----------
zapi.host.delete(*host_ids)

print(f"{len(host_ids)} hosts deleted from Zabbix.")

# ---------- LOGOUT ----------
zapi.logout()
print("Done.")
