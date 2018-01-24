1) The First code is using the padas module:

$ cat check_ldapUserdata.py
#!/usr/bin/python3
import pandas as pd
import subprocess

user_list = []
mngr_list = []

def CheckUid(user):
    proc = subprocess.Popen("ldapsearch -h ldapserver -D 'cn=directory manager' -w JatetRE3 -LLLb 'ou=people,o=rraka.com' 'uid=%s' managerlogin" % (user), shell=True, stdout=subprocess.PIPE)
    info_str = proc.stdout.read().decode('utf8')
    split_str = info_str.split()
    if len(split_str) > 1:
      user = split_str[1].split(',')[0].split('=')[1]
      manager = split_str[-1]
      user_list.append(user)
      mngr_list.append(manager)
    else:
      split_str = 'null'

def DataList():
      df = pd.DataFrame({'User':user_list, 'Manager':mngr_list})
      df = df[['User', 'Manager']]  # To keep the order of columns
      #return df
      print(df)

def CallUid():
  with open('testu', mode='rt', encoding='utf-8') as f:
    for line in f.readlines():
      CheckUid(line)

if __name__ == '__main__':
  CallUid()
  DataList()

Result Output is as Follows...

$ ./check_ldapUserdata.py
       User   Manager
0      karn  benjamin
1     niraj   vikashg
2  vaithees  benjamin
3      mauj  benjamin
