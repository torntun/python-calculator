class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        if a<0:
            a=-a
        elif b<0:
            b=-b

        result = 0
        for i in range(b):
            result = self.add(result, a)
        if a<0 or b<0:
            return result
        else:
            return result

    def divide(self, a, b):
        result = 0

        if a<0 and b>0:
            while a < 0:
                a = self.add(a, b)
                result += 1
            return -result
        elif a<0 and b<0:
            while a <= b:
                a = self.subtract(-a, -b)
                a=-a
                result += 1
            return result
        elif a>0 and b<0:
            while a > 0:
                a = self.subtract(a, -b)
                result += 1
            return -result
        elif a==0:
            return 0
        else:
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
    
    def modulo(self, a, b):
        if a<0:
            a=-a
        elif b<0:
            b=-b
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))