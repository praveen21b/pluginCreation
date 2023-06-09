import calculator_main

class SquarePlugin:
    def calculate_square(self, num):
        pass  # Implement this method in the plugin

class MultiplySquarePlugin(SquarePlugin):
    def calculate_square(self, num): # overrides the parent class
        return num * num
    
class PowerSquarePlugin(SquarePlugin):
    def calculate_square(self, num):
        return num ** 2


# examples
calculator = calculator_main.SquareCalculator()
# print(type(calculator))
calculator.register_plugin(PowerSquarePlugin())
# result_squarePlgin = calculator.calculate_square(5)
# print(f'Value from SquarePlugin class: {result_squarePlgin}', '\n')
calculator.register_plugin(MultiplySquarePlugin())
result = calculator.calculate_square(5)
print(f'Result: {result}')