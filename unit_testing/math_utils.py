
class MathUtils:

    def int_division(self, a, b):
        if b==0:
            raise ValueError("Divisor cannot be 0!")
        return a//b
    
    def power(self, a,b):
        return a**b
    