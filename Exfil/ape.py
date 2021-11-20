import datetime
import binascii
timeframe = [int((datetime.datetime.strptime(x.strip()[:-3], '%H:%M:%S.%f') - datetime.datetime(1900, 1, 1)).total_seconds()) for x in open('time.txt').readlines()]

output = ''
for i in range(len(timeframe) - 1):
    if timeframe[i+1] - timeframe[i] < 3:
        output += '0'
    else:
        output += '1'

output = '0b' + output + '1'
n = int(output, 2)
flag = binascii.unhexlify('%x' % n)
print(flag)
