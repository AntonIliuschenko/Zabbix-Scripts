from pyzabbix import ZabbixAPI

# ---------- SETTINGS ----------
ZABBIX_URL = "http://127.0.0.1/zabbix"
USER = "Admin" #Your Admin Login
PASSWORD = "PASSWORD" #Your Admin password 

GROUP_NAME = "Camera" #Group name hosts you want to delete

# ---------- Connection ----------
zapi = ZabbixAPI(ZABBIX_URL)
zapi.login(USER, PASSWORD)

print("Connected to Zabbix API")

# ---------- Find a Group ----------
group = zapi.hostgroup.get(filter={"name": GROUP_NAME})

if not group:
    print(f"Group {GROUP_NAME} not found.")
    exit()

group_id = group[0]['groupid']

print(f"Group found: {GROUP_NAME} (ID {group_id})")

# ---------- Get all hosts in the group ----------
hosts = zapi.host.get(groupids=group_id)

if not hosts:
    print("No hosts in this group.")
    exit()

print(f"Found {len(hosts)} hosts. Deleting...")

# ---------- Collecting HOST IDS ----------
host_ids = [host['hostid'] for host in hosts]

# ---------- Deleting----------
zapi.host.delete(*host_ids)

print(f"{len(host_ids)} hosts deleted from Zabbix.")

# ---------- LOGOUT ----------
zapi.logout()
print("Done.")
