def price_format(num):
    price = float(num)
    return "${:,.2f}".format(price)

def multiple(num1, num2):
    number1 = float(num1)
    number2 = float(num2)
    
    if number1 > 0 and number2 > 0:
        percent = number1/number2
        return f"({round(percent, 2)}x)"
    return 0