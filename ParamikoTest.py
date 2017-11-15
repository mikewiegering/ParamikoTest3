
#!/usr/bin/env python
import sys
import paramiko
import os
import time
from getpass import getpass




def main():

        os.chdir('/home/wwt/WWT_Automation_Lab/ParamikoTest3/ParamikoTest3')
        establishConnection()


def establishConnection():
#       ip_addr = getIP
#       username = getUsername
#       password = getPassword
#       port = getPort

#       #ip_addr = '192.168.30.1'
#       #username = 'wwt'
#       #password = getpass()
#       #port = 22

#       getIP = raw_input("Please enter the IP address")
#       getPort = input("Please enter the port for the connection")
#       getUsername = raw_input("Please enter the admin username")
#       getPassword = getpass()

        ip_addr = raw_input("Please enter the IP address ")
        port = input("Please enter the port for the connection ")
        username = raw_input("Please enter the admin username ")
        password = getpass()

        remote_conn_pre=paramiko.SSHClient()
        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
        remote_conn=remote_conn_pre.invoke_shell()

        output = remote_conn.recv(5000)



#       remote_conn.send("en\n")
#       output1 = remote_conn.recv(5000)

#       remote_conn.send("show ip int brief\n")
        remote_conn.send("terminal length 0\n")
        time.sleep(10)
        remote_conn.send("show run brief\n")
        time.sleep(10)
        output2 = remote_conn.recv(5000)

        remote_conn_pre.close

        f=open(ip_addr, "w+")
        f.write(output2)
        f.close
        print("a new config file as been created named "+ip_addr)




#if __main__ == "__main__":
main()

