class SquareCalculator:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        self.plugins.append(plugin) # the plugin class itself appended here

    def calculate_square(self, num):
        squares = []
        for plugin in self.plugins:
            square = plugin.calculate_square(num)
            squares.append(square)
        return squares
    
