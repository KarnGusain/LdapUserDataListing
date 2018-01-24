$ cat check_table_working1.py
#!/usr/bin/python3
import subprocess

def CheckUid(user):
    proc = subprocess.Popen("ldapsearch -h ldapserver -D 'cn=directory manager' -w pass123 -LLLb 'ou=people,o=rraka.com' 'uid=%s' managerlogin" % (user), shell=True, stdout=subprocess.PIPE)
    info_str = proc.stdout.read().decode('utf8')
    split_str = info_str.split()
    if len(split_str) > 1:
      raw_data = {split_str[1].split(',')[0].split('=')[1] :  split_str[-1]}
      #raw_data = {'UserID': split_str[1].split(',')[0].split('=')[1], 'Manger': split_str[-1]}
      for key, value in raw_data.items():
        #print(key, ":", value)
        print('{} : {}'.format(key, value))
    else:
      split_str = 'null'

def CallUid():
  with open('hh', mode='rt', encoding='utf-8') as f:
    for line in f.readlines():
      CheckUid(line)

if __name__ == '__main__':
  CallUid()

Result output of the above is as below...

$ ./check_table_working1.py
aashishp : rpudota
abaillie : davem
abishek : kalyang
adik : venky
adithya : jagi
