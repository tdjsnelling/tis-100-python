# tis-100.py
import sys

# error codes
'''
ERR code 0x01: invalid instruction
ERR code 0x02: invalid register
ERR code 0x03: invalid label
ERR code 0x04: invalid offset
'''

# ACC & BAK registers
ACC = 0
BAK = 0

# instruction pointer
IP = 0

# list for instructions to be loaded into
ins = []

# load instructions into array
with open(sys.argv[1]) as f:
	ins = f.read().splitlines()

# strip any spaces and tabs from instructions
for i in range(len(ins)):
	ins[i] = ins[i].strip(' \t')

# handle errors
def error(code):
	print 'ERR at instruction %s code %s' % (IP + 1, code)	

# main execution loop
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
		elif opcode[2] == 'NIL':
			pass
		else:
			error(0x02)
	
	elif opcode[0] == 'SWP':
		ACC, BAK = BAK, ACC

	elif opcode[0] == 'SAV':
		BAK = ACC

	elif opcode[0] == 'ADD':
		if opcode[1] == 'ACC':
			ACC += ACC
		else:
			ACC += int(opcode[1])

	elif opcode[0] == 'SUB':
		if opcode[1] == 'ACC':
			ACC -= ACC
		else:
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

	elif opcode[0].startswith('#'):
		# this is a comment, do nothing
		pass

	elif opcode[0] == '':
		# this is whitespace, do nothing
		pass

	# if none of the above, must be an invalid instruction
	else:
		error(0x01)

# iterate through list, execute instructions
while IP < len(ins):
	execute(ins[IP])
	IP += 1
