temp_count = 0
tac_code = []

def new_temp():
    global temp_count
    temp_count += 1
    return f"t{temp_count}"


def generate(node):
    if node is None:
        return None

    # PROGRAM
    if node.type == "program":
        generate(node.children[0])

    # STATEMENTS
    elif node.type == "statements":
        for child in node.children:
            generate(child)

    # DECLARATION → ignore
    elif node.type == "declaration":
        pass

    # ASSIGNMENT
    elif node.type == "assign":
        rhs = generate_expr(node.children[0])
        tac_code.append(f"{node.value} = {rhs}")

    # PRINT
    elif node.type == "print":
        tac_code.append(f"print {node.value}")


def generate_expr(node):
    if node.type == "number":
        return str(node.value)

    elif node.type == "identifier":
        return node.value

    elif node.type == "binop":
        left = generate_expr(node.children[0])
        right = generate_expr(node.children[1])

        temp = new_temp()
        tac_code.append(f"{temp} = {left} {node.value} {right}")
        return temp