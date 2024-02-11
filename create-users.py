#!/usr/bin/env python3
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match(r'^\s*#', line)  # regex to match lines starting with #
        
        if match or len(line.strip().split(':')) != 5:
            continue
        
        fields = line.strip().split(':')
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')
        
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        os.system(cmd)  # execute command to create user
        
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        os.system(cmd)  # execute command to set password
        
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                os.system(cmd)  # execute command to assign user to group

if __name__ == '__main__':
    main()
