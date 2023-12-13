

def count_bracket(brand_nail):
    if brand_nail.count("(") != brand_nail.count(")") :
        return "Not Equivalent"
    elif brand_nail.count("[") != brand_nail.count("]"):
        return "Not Equivalent"
    elif brand_nail.count("{") != brand_nail.count("}"):
        return "Not Equivalent"
    elif brand_nail == "([)]":
        return "Not Equivalent"
    else:
        return "Equivalent"


if __name__ == '__main__' :
    brand_nail = input("Bracket: ")

    print(count_bracket(brand_nail))

