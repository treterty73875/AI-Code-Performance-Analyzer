import reader
import analyzer
content=reader.read_file()
line_count, word_count, blank_line_count, character_count, for_loops_count, while_loops_count, if_statements_count, functions_count , variables_count, variables= analyzer.analyze_content(content)
print("\n-----content of the file-----\n",content)
print("\n--------Analysis report--------\n",)
print("Total number of lines:   \n", line_count)
print("Total number of words:   \n", word_count)
print("Total number of blank lines:   \n", blank_line_count)
print("Total number of characters:   \n", character_count)
print("Total number of for loops:   \n", for_loops_count)
print("Total number of while loops:   \n", while_loops_count)
print("Total number of if statements:   \n", if_statements_count)
print("Total number of functions:    \n", functions_count)
print("Total number of variables:   \n", variables_count)
print("Variables: \n", variables)
print("\n-------------------------------\n")

