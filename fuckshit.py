# FUCKSHIT by nuthater
# CREATION DATE: 4/21/2023
# Type of language: Esoteric

# Main Code
def run(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')
        res = ""
        for line in lines:
            content = line.strip(' ')
            digits = []
            for digit in content:
                if digit.isdigit():
                    if digit == '1':
                        digits.append(1)
                    elif digit == '2':
                        sh = input(">> ")
                        digits.append(int(sh))
                    else:
                        continue
            result = sum(digits)
            res += chr(result)
        print(res)
import sys
run(sys.argv[1])