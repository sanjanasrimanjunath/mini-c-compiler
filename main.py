from lexer import lexer

def run_lexer(data):
    lexer.input(data)
    for tok in lexer:
        print(tok)

if __name__ == "__main__":
    with open("test.mc") as f:
        data = f.read()

    run_lexer(data)

from parser import parser

if __name__ == "__main__":
    with open("test.mc") as f:
        data = f.read()

    result = parser.parse(data)
    print("\nAST:\n", result)


from parser import parser
from semantic import analyze, symbol_table

if __name__ == "__main__":
    with open("test.mc") as f:
        data = f.read()

    #result = parser.parse(data)
    #print("\nAST:\n", result)

    print("\n--- Semantic Analysis ---")
    analyze(result)

    print("\nSymbol Table:")
    print("\n---------------------------------")
    print("Variable    Type")
    print("---------------------------------")
    for var, typ in symbol_table.items():
        print(f"{var:<10} {typ}")
    print("---------------------------------")

from tac import generate, tac_code

print("\n--- Three Address Code (TAC) ---")
generate(result)

for line in tac_code:
    print(line)