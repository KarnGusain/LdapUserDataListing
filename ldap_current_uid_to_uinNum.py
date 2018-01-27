#!/usr/bin/python3
# mytest.py
import subprocess

def CheckUid():
    proc = subprocess.Popen("ldapsearch -h ldapserver -xLLLb 'ou=people,o=example.com' uid uidNumber", shell=True, stdout=subprocess.PIPE)
    info_str = proc.stdout.read().decode('utf8')
    str_info = info_str.splitlines()
    prefixes = ["uid:", "uidNumber"]
    for line in str_info:
        if line.startswith(tuple(prefixes)):
            lines = line
            for line in lines.splitlines():
                     print(line, end=' ' if line.startswith("uid:")  else "\n")

CheckUid()

$ ./mytest.py
uid: nkulkarn uidNumber: 257589
uid: karn uidNumber: 258018
uid: pkulkarn uidNumber: 258787
uid: testkarn uidNumber: 263402
------- output snipped -------------

