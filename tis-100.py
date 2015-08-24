# tis-100.py
import sys

'''
ERR code 0x01: invalid instruction
ERR code 0x02: invalid register
ERR code 0x03: invalid label
ERR code 0x04: invalid offset
'''

ACC = 0 	# ACC register
BAK = 0 	# BAK register
IP = 0

ins = []

with open(sys.argv[1]) as f:
	ins = f.read().splitlines()

for i in range(len(ins)):
	ins[i] = ins[i].strip(' \t')

def error(code):
	print 'ERR at instruction %s code %s' % (IP, code)	

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
			error(0x02)
	
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
		try:
			IP = ins.index(opcode[1] + ':')
		except:
			error(0x03)

	elif opcode[0] == 'JEZ':
		if ACC == 0:
			try:
				IP = ins.index(opcode[1] + ':')
			except:
				error(0x03)

	elif opcode[0] == 'JNZ':
		if ACC != 0:
			try:
				IP = ins.index(opcode[1] + ':')
			except:
				error(0x03)

	elif opcode[0] == 'JGZ':
		if ACC > 0:
			try:
				IP = ins.index(opcode[1] + ':')
			except:
				error(0x03)

	elif opcode[0] == 'JLZ':
		if ACC < 0:
			try:
				IP = ins.index(opcode[1] + ':')
			except:
				error(0x03)

	elif opcode[0] == 'JRO':
		try:
			if opcode[1] == 'ACC':
				IP = ACC
			else:
				IP = IP + int(opcode[1])
		except:
			error(0x04)

	elif opcode[0].endswith(':'):
		# this is a label, do nothing
		pass

	else:
		error(0x01)

while IP < len(ins):
	execute(ins[IP])
	IP += 1
