import calculator
import time

def main():
    while True:
        operator, a, b = calculator.info_receive()
        calculator.operation(operator, a, b)
        if operator == "7":
            break
        time.sleep(3)

main()