class Brainfuck:
    def brainfuck_program(self,program):
        idx = 0
        while idx < len(program):
    			op = program[idx]
    			if op == '+':
    				cells[pointer] += 1
