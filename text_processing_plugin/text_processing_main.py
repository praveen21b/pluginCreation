class TextProcessor:
    def __init__(self) -> None:
        self.plugins = []
        
    def register_plugins(self, plugin:object) -> None:
        self.plugins.append(plugin)
        
    def process_text(self,text):
        processed_text = []
        for plugin in self.plugins:
            text = plugin.process_text(text)
            processed_text.append(text)
        return processed_text