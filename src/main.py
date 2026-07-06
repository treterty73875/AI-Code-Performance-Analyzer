import reader
import analyzer
content=reader.read_file()
total_lines=analyzer.analyze_file(content)
print("\n-----content of the file-----\n",content)
print("\n-----total lines in the file-----\n",total_lines)