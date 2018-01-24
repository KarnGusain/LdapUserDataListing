$ cat check_ldapUserdata2.py
#!/usr/bin/python3
import re
import subprocess
from beautifultable import BeautifulTable
table = BeautifulTable()
table.column_headers = ["User", "Manager"]

def CheckUid(user):
    proc = subprocess.Popen("ldapsearch -h ldapserver  -D 'cn=directory manager' -w pass123 -LLLb 'ou=people,o=rraka.com' 'uid=%s' managerlogin" % (user), shell=True, stdout=subprocess.PIPE)
    info_str = proc.stdout.read().decode('utf8')
    pat_match = re.match(".*uid=(.*?)\,.*\nmanagerlogin:\s+(.*)",info_str)
    if pat_match:
        table.append_row([pat_match.group(1), pat_match.group(2)])

def CallUid():
  input_file=input("Please enter the file name : ")
  with open(input_file, mode='rt', encoding='utf-8') as f:
    for line in f.readlines():
      CheckUid(line)
  print(table)

if __name__ == '__main__':
  CallUid()

Result Output as as below....

$ ./check_ldapUserdata2.py
Please enter the file name : testu
+----------+----------+
|   User   | Manager  |
+----------+----------+
|   karn   | benjamin |
+----------+----------+
|  niraj   | vikashg  |
+----------+----------+
| vaithees | benjamin |
+----------+----------+
|   mauj   | benjamin |
+----------+----------+
