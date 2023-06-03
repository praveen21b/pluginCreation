# Text Processor Plugin

The `text_plugin.py` file contains the plugin classes (BasePlugin, ConvertToUpperCase, and ConvertToLowerCase). These classes are defined in the plugin file and can be developed and maintained independently.

The `text_processing_main.py` file is the main program that uses the plugin classes. It imports the required plugins (ConvertToUpperCase and ConvertToLowerCase) from the `text_plugin` module and utilizes them in the `TextProcessor` class.

By separating the plugin classes into their own file, you can easily extend the functionality by creating additional plugins in separate files and importing them as needed.

This modular approach allows for better code organization, maintainability, and reusability, as each plugin can be developed, tested, and maintained independently of the main program.