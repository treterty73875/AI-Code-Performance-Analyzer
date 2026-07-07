import reader
import analyzer
content=reader.read_file()
line_count, word_count, blank_line_count, character_count=analyzer.analyze_content(content)
print("\n-----content of the file-----\n",content)
print("\n--------Analysis report--------\n",)
print("Total number of lines:", line_count)
print("Total number of words:", word_count)
print("Total number of blank lines:", blank_line_count)
print("Total number of characters:", character_count)
print("\n-------------------------------\n")

