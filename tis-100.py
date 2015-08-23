# tis-100.py
import sys

ACC = 0
BAK = 0
IP = 0

ins = []

with open(sys.argv[1]) as f:
	ins = f.read().splitlines()

for i in range(len(ins)):
	ins[i] = ins[i].strip(' \t')

def execute(opcode_full):
	global ACC
	global BAK
	global IP

	opcode = opcode_full.split(' ')

	# no god damn switch/case...
	if opcode[0] == 'NOP':
		pass
	
	elif opcode[0] == 'MOV':
		if opcode[2] == 'ACC':
			ACC = int(opcode[1])
		elif opcode[2] == 'OUT':
			if opcode[1] == 'ACC':
				print ACC
			else:
				print opcode[1]
		else:
			error()
	
	elif opcode[0] == 'SWP':
		ACC, BAK = BAK, ACC

	elif opcode[0] == 'SAV':
		BAK = ACC

	elif opcode[0] == 'ADD':
		ACC += int(opcode[1])

	elif opcode[0] == 'SUB':
		ACC -= int(opcode[1])

	elif opcode[0] == 'NEG':
		ACC = int(-ACC)

	elif opcode[0] == 'JMP':
		IP = ins.index(opcode[1])

	elif opcode[0] == 'JEZ':
		if ACC == 0:
			IP = ins.index(opcode[1])

	elif opcode[0] == 'JNZ':
		if ACC != 0:
			IP = ins.index(opcode[1])

	elif opcode[0] == 'JGZ':
		if ACC > 0:
			IP = ins.index(opcode[1])

	elif opcode[0] == 'JLZ':
		if ACC < 0:
			IP = ins.index(opcode[1])

	elif opcode[0] == 'JRO':
		if opcode[1] == 'ACC':
			IP = ACC
		else:
			IP = IP + int(opcode[1])

while IP < len(ins):
	execute(ins[IP])
	IP += 1

print ins
print 'ACC', ACC
print 'BAK', BAK
