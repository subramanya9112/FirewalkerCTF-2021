```
tshark -r capture.pcap -Y "mysql.command==3" -T fields -e mysql.query > output.txt

tshark -r capture.pcap -Y "mysql.command==3" -T fields -e frame.time -e mysql.query > timed_queries.txt

grep "password" timed_queries.txt > password_queries.txt

cat password_queries.txt| cut -d " " -f 4 > time.txt

HTB{b1t_sh1ft1ng_2xf1l_1s_c00l}
HTB{b1t_sh1ft1ng_3xf1l_1s_c00l}
```
