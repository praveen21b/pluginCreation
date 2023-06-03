import text_processing_main

class BasePlugin:
    def process_text(self,text):
        pass
    
class ConvertToLowerCase(BasePlugin):
    def process_text(self, text):
        return text.lower()
    
class ConvertToUpperCase(BasePlugin):
    def process_text(self, text):
        return text.upper()
    
# Example
processed_texts = text_processing_main.TextProcessor()
## add the plugins to the list
processed_texts.register_plugins(ConvertToLowerCase())
processed_texts.register_plugins(ConvertToUpperCase())
## print the processed texts
print(processed_texts.process_text('HEllO wOrLd!!'))
