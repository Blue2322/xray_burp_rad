#!/usr/bin/python3
# coding: utf-8
import subprocess

def scan(fileline):
	target_txt = fileline + ".txt"
	#设置代理：
	#（1）burp联动
	#（2）xray联动
	cmd = ["./rad","-t",fileline,"--http-proxy","127.0.0.1:8080","-text-output",target_txt]
	rsp = subprocess.Popen(cmd)
	output,error = rsp.communicate()
	print(output)

if __name__=='__main__':
	file = open("url.txt")
	for text in file.readlines():
		fileline = text.strip('\n')
		scan(fileline)
