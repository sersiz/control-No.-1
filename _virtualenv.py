def addition(num):
    result =sum(num)
    return result


def multi(num):
    result = 1
    for numbers in num:
        result *= numbers
    return result


def divide(num):
    result = num[0]
    for numbers in num[1:]:
        if numbers == 0:
            raise ValueError("делить на ноль нельзя")
        result /= numbers
        return result


def subtract(num):
    result = num[0]
    for numbers in num[1:]:
        result -= numbers
    return result

def get_num():
    while True:
        try:
            num = input("введите числа ЧЕРЕЗ ПРОБЕЛЫ: ")
            number_list = [float(numbers) for numbers in num.split()]
            return number_list
        except ValueError:
            print("я же русским языком написал что вписать!")

def get_oper():
    while True:
        operatorion = input("теперь введём знак операции (+, -, *, /): ")
        if operatorion in ('+', '-', '*', '/'):
            return operatorion
        else:
            print("только те знаки которые я написал!")

def calculator():
    # print(result)

    num = get_num()
    operation = get_oper()

    try:
        if operation == "+":
           print("Ответ", addition(num))
        elif operation == "-":
           print("Ответ", subtract(num))
        elif operation == "*":
           print("Ответ", multi(num))
        elif operation == "/":
           print("Ответ", divide(num))

    except ValueError as e:
        print("Ошибка: {e}")

calculator()
