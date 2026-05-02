# 🔹 Symbol Table
symbol_table = {}

# 🔹 Semantic Analyzer Function
def analyze(node):
    if node is None:
        return None

    # PROGRAM
    if node.type == "program":
        analyze(node.children[0])

    # STATEMENTS
    elif node.type == "statements":
        for child in node.children:
            analyze(child)

    # DECLARATION
    elif node.type == "declaration":
        var_type, var_name = node.value

        if var_name in symbol_table:
            print(f"Error: Variable '{var_name}' already declared")
        else:
            symbol_table[var_name] = var_type

    # ASSIGNMENT
    elif node.type == "assign":
        var_name = node.value

        if var_name not in symbol_table:
            print(f"Error: Variable '{var_name}' not declared")
            return

        expr_type = evaluate_expression(node.children[0])

        if expr_type != symbol_table[var_name]:
            print(f"Type Error: Cannot assign {expr_type} to {symbol_table[var_name]}")

    # PRINT
    elif node.type == "print":
        var_name = node.value

        if var_name not in symbol_table:
            print(f"Error: Variable '{var_name}' not declared")


# 🔹 Expression Type Evaluation
def evaluate_expression(node):
    if node.type == "number":
        if isinstance(node.value, int):
            return "int"
        else:
            return "float"

    elif node.type == "identifier":
        if node.value not in symbol_table:
            print(f"Error: Variable '{node.value}' not declared")
            return None
        return symbol_table[node.value]

    elif node.type == "binop":
        left_type = evaluate_expression(node.children[0])
        right_type = evaluate_expression(node.children[1])

        if left_type == "float" or right_type == "float":
            return "float"
        return "int"