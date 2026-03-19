# ZabbixMassUpdate
Adding a large number of hosts  
Иногда встает задача по добавлению большого количества хостов в Zabbix по определенному признаку (группа- UPS, Cameras, WS, Network etc.), и руками создавать каждый хост, добавлять его в группу, и добавлять ему шаблон совсем не хочеться!
После длительных поисков в сети интернет, ничего нормального не нашел и слепил простой скрипт на Python, который из вашего файла csv добавит хосты в Zabbix, сразу добавит их в группу и натянет шаблон.
В этом репозитории будут 2 файла. 1- образец файла csv, я делал так, сначала собрал Excel таблицу по образцу, названия полей должны четко соответствовать названиям в скрипте, далее сохранил файл Excel как .csv файл с разделителем запятой. В скрипте я  все поправил(соответствие столбцов названиям групп в zabbix) и у меня последний раз благополучно добавилось 1300 хостов и раскидалось по группам. Но каждому надо проверить и подкорректировать под себя.  
2- это сам файл скрипта, сделаю на 2 х языках комментарии, чтоб было всем понятно. Естественно нужно будет установить Python и проверить что он заработал, эти 2 файла положить в ону папку и запустить скрипт.

---

# Zabbix Bulk Host Import Script

Sometimes there is a need to add a large number of hosts to Zabbix based on a specific attribute (for example: **UPS, Cameras, Workstations, Network devices, etc.**).

Creating each host manually, assigning it to a group, and linking templates can be very time-consuming.

After searching the internet for a suitable solution and not finding anything that worked well for my case, I created a **simple Python script** that imports hosts from a **CSV file**, automatically adds them to Zabbix, assigns them to the correct **host groups**, and links the required **templates**.

## Repository Contents

This repository contains **two files**:

### 1. CSV Example File

A sample **CSV file** showing the required structure.

Recommended workflow:

1. Create an **Excel spreadsheet** using the same column structure as in the sample file.
2. Make sure the **column names exactly match the names used in the script**.
3. When finished, save the spreadsheet as a **CSV file (comma-separated)**.

The script maps the CSV columns to the corresponding **Zabbix host groups and templates**.

In my last run, the script successfully added **over 1300 hosts** and distributed them automatically across the correct groups.

⚠️ You will likely need to **adjust the script for your own environment** (group names, templates, API settings, etc.).

### 2. Python Script

The **Python script** that performs the import.

Features:

* Reads hosts from a CSV file
* Creates hosts in Zabbix
* Assigns hosts to groups automatically
* Links templates automatically

The script contains **comments in two languages** to make it easier to understand and modify.

## Requirements

* Python installed on your system
* Access to the **Zabbix API**
* CSV file prepared according to the provided example

## Usage

1. Install Python and verify that it is working.
2. Place the following files in the **same directory**:

   * the CSV file
   * the Python script
3. Adjust the script parameters if necessary (API URL, credentials, group names, etc.).
4. Run the script:

```bash
python script_name.py
```

The script will read the CSV file and automatically create the hosts in Zabbix.

## Notes

* Always **test with a small number of hosts first** before importing large datasets.
* Make sure your **group names and templates exist in Zabbix**.
* Adapt the script to match your infrastructure if necessary.

---
