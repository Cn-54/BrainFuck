
operators = [">","<","+","-","[","]",",","."]

def run(program):
    code = [c for c in program if c in operators]
    DataPointer = 0
    CodePointer = 0
    memory = [0] * 30_000
    while CodePointer < len(code):
        op = code[CodePointer]
        match op:
            case ">": DataPointer += 1
            case "<": DataPointer -= 1
            case "+": memory[DataPointer] += 1
            case "-": memory[DataPointer] -= 1
            case "[":
                if memory[DataPointer] == 0:
                    depth = 1
                    while depth > 0:
                        CodePointer += 1
                        if code[CodePointer] == '[': depth += 1
                        elif code[CodePointer] == ']': depth -= 1
            case "]":
                if memory[DataPointer] != 0:
                    depth = 1
                    while depth > 0:
                        CodePointer -= 1
                        if code[CodePointer] == ']': depth += 1
                        elif code[CodePointer] == '[': depth -= 1
            case ",": memory[DataPointer] = ord(input("input: ")[0])
            case ".": print(chr(memory[DataPointer]))
        CodePointer +=1