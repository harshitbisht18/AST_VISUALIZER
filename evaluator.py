def evaluate(node):
    if node.type == 'Number':
        return node.value

    elif node.type == 'ADD':
        return evaluate(node.left) + evaluate(node.right)
    elif node.type == 'SUB':
        return evaluate(node.left) - evaluate(node.right)
    elif node.type == 'MUL':
        return evaluate(node.left) * evaluate(node.right)
    elif node.type == 'DIV':
        return evaluate(node.left) / evaluate(node.right)

    # Comparison operators
    elif node.type == 'EQ':
        return int(evaluate(node.left) == evaluate(node.right))
    elif node.type == 'NEQ':
        return int(evaluate(node.left) != evaluate(node.right))
    elif node.type == 'GT':
        return int(evaluate(node.left) > evaluate(node.right))
    elif node.type == 'LT':
        return int(evaluate(node.left) < evaluate(node.right))
    elif node.type == 'GTE':
        return int(evaluate(node.left) >= evaluate(node.right))
    elif node.type == 'LTE':
        return int(evaluate(node.left) <= evaluate(node.right))

    # Logical operators
    elif node.type == 'AND':
        return int(bool(evaluate(node.left)) and bool(evaluate(node.right)))
    elif node.type == 'OR':
        return int(bool(evaluate(node.left)) or bool(evaluate(node.right)))
    elif node.type == 'NOT':
        return int(not bool(evaluate(node.left)))

    # Conditional (if-then-else)
    elif node.type == 'IF':
        condition_value = evaluate(node.condition)
        if condition_value:
            return evaluate(node.true_branch)
        else:
            return evaluate(node.false_branch)

    raise ValueError(f"Unknown node type: {node.type}")
