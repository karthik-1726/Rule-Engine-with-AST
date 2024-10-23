class Node:
    def __init__(self, type, left=None, right=None, value=None, operator=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value
        self.operator = operator  # Added operator

    def to_dict(self):
        # Create a dictionary representation for JSON serialization
        return {
            'type': self.type,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None,
            'value': self.value,
            'operator': self.operator.to_dict() if self.operator else None
        }



def create_rule(rule_string):
    rule_string = rule_string.strip()
    operators = ['>', '<', '>=', '<=', '==', '!=']

    for operator in operators:
        if operator in rule_string:
            left_operand, right_operand = rule_string.split(operator, 1)
            left_node = Node('operand', value=left_operand.strip())
            right_node = Node('operand', value=right_operand.strip())
            operator_node = Node('operator', value=operator)  # Create the operator node

            # Create a single expression node linking left operand and right operand with operator as a separate node
            return Node('expression', left=left_node, right=right_node)

    # If no operator is found, return the original string as a single operand
    return Node('operand', value=rule_string)





def combine_rules(rules):
    """Combine rules into a single AST."""
    root = Node('operator', left=create_rule(rules[0]))
    for rule in rules[1:]:
        root = Node('operator', left=root, right=create_rule(rule))
    return root.to_dict()  # Return the dictionary representation


def evaluate_rule(ast, data):
    # Evaluate the AST against the data
    return True  # Simplified for example
