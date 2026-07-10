#from data.cpp_keywords import cpp_keywords


def analyze_content(content):
    line_count=count_lines(content)
    word_count=count_words(content)
    blank_line_count=count_blank_lines(content)
    character_count=count_characters(content)
    for_loops_count=count_for_loops(content)
    while_loops_count=count_while_loops(content)
    if_statements_count=count_if_statements(content)
    functions_count=count_functions(content)
    variables_count, variables = count_variables(content)
    return line_count, word_count, blank_line_count, character_count, for_loops_count, while_loops_count, if_statements_count, functions_count, variables_count, variables


def count_lines(content):
    lines=content.split("\n")
    count=0;
    for i in range(0,len(lines)):
        count+=1
    return count

#def count_items(items):
   # count=0;
   # for i in range(0,len(items)):
   #     count+=1
    #return count

def count_words(content):
    words=content.split()
    count=0;
    for i in range(0,len(words)):
       count+=1
    return count;


def count_blank_lines(content):
    blank_lines=content.split("\n")
    count=0;
    for i in range(0,len(blank_lines)):
        if blank_lines[i].strip() == "":
            count+=1
    return count;

def count_characters(content):
    count=0;
    for i in range(0,len(content)):
        count+=1
    return count;

def extract_keyword(tokens):
    keyword=""

    for ch in tokens:
        if ch.isalpha():
            keyword+=ch
        else:
            break
    return keyword

def count_for_loops(content):
 return count_keyword(content,"for")



def count_while_loops(content):
 return count_keyword(content,"while")    


def count_if_statements(content):
    return count_keyword(content,"if")



def count_functions(content):
     line=content.split()
     count=0;
     datatypes=["int","float","double","char","void","long","bool","long long","short"]
     for i in range(1,len(line)):
        keyword=extract_keyword(line[i-1])
        if keyword in datatypes and "(" in line[i]:
            count+=1;
     return count;

def count_keyword(content,target_keyword):
    line=content.split()
    count=0;
    for i in range(0,len(line)):
        keyword=extract_keyword(line[i])
        if keyword==target_keyword:
            count+=1
    return count

def count_variables(content):
    words = content.split()

    datatypes = [
        "int", "float", "double", "char",
        "bool", "long", "short", "void"
    ]

    count = 0;
    variables = []

    for i in range(1, len(words)):

        previous = extract_keyword(words[i - 1])
        keyword = extract_keyword(words[i])

        if (previous in datatypes and
            keyword not in datatypes and
            "(" not in words[i] and
            keyword != ""):

            variables.append(keyword)
            count += 1

    return count, variables