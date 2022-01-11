import re

def balance(equation):
    """
    Balance the equation.
    """
    # Split the equation into reactants and products
    reactants, products = equation.split("->")

    # Split the reactants and products into individual elements
    reactants = reactants.split("+")
    products = products.split("+")

    # Split each element into individual elements
    reactants = [element.split() for element in reactants]
    products = [element.split() for element in products]

    # Create a list of elements and their coefficients
    elements = []
    for element in reactants + products:
        if element:
            elements.append(element[0])

    # Create a dictionary of elements and their coefficients
    elements = {element: 0 for element in elements}

    # Count the number of each element in the reactants
    for element in reactants:
        if element:
            elements[element[0]] += int(element[1])

    # Count the number of each element in the products
    for element in products:
        if element:
            elements[element[0]] -= int(element[1])

    # Create a list of the elements and their coefficients
    elements = [(element, elements[element]) for element in elements]

balance("HCl + Na -> NaCl + H2")
