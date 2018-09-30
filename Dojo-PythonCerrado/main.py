class Brainfuck:
    def brainfuck_program(self,program):
        idx = 0
        cells = [0] * 30000
        pointer = 0
        while idx < len(program):
            op = program[idx]
            if op == '+':
                cells[pointer] += 1
            idx += 1
        return cells[pointer]
