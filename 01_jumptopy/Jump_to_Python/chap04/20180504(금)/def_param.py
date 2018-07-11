def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i

    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    elif choice == "div":
        result = args[0]
        for i in args[1:]:
            result //= i
    elif choice == "sub":
        result = args[0]
        for i in args[1:]:
            result -= i
    return result


print(sum_mul('div', 7, 3))
