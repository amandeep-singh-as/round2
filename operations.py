class Operations:
    
    def addition(self, items) -> int:
        result = 0
        for item in items:
            if not list(item):
                result += int(item.text)
            else:
                result += self.__operate(item)
        return result

    def subtraction(self, items) -> int:
        minuend, subtrahend = 0, 0
        for item in items:
            if not list(item):
                if item.tag == 'minuend':
                    minuend = int(item.text)
                else:
                    subtrahend = int(item.text)
            else:
                if item.tag == 'minuend':
                    minuend = self.__operate(item)
                else:
                    subtrahend = self.__operate(item)
        return minuend - subtrahend

    def division(self, items) -> int:
        dividend, divisor = 0, 1
        for item in items:
            if not list(item):
                if item.tag == 'divisor':
                    divisor = int(item.text)
                else:
                    dividend = int(item.text)
            else:
                if item.tag == 'divisor':
                    divisor = self.__operate(item)
                else:
                    dividend = self.__operate(item)
        try:
            return dividend // divisor
        except ZeroDivisionError:
            return "Zero division"

    def multiplication(self, items) -> int:
        result = 1
        for item in items:
            if not list(item):
                result *= int(item.text)
            else:
                result *= self.__operate(item)
        return result

    def __operate(self, items) -> int:
        result = 0
        for item in items:
            operation = item.tag
            if operation == 'addition':
                result += self.addition(item)
            elif operation == 'subtraction':
                result -= self.subtraction(item)
            elif operation == 'division':
                result = self.division(item) if result == 0 else result // self.division(item)
            elif operation == 'multiplication':
                if result == 0:
                    result = 1
                    result *= self.multiplication(item)
        return  result


