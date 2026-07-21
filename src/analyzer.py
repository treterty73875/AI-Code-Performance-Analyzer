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
    count_datatype, used_datatypes=count_datatypes(content)
    count_return, return_list=count_return_statements(content)
    Display_variables,variables_used,variables_unused=show_variables(content)
    return line_count, word_count, blank_line_count, character_count,for_loops_count, while_loops_count, if_statements_count, functions_count, variables_count, variables,count_datatype,used_datatypes,count_return,return_list,Display_variables,variables_used,variables_unused

def tokenization(content):
    symbols=["{","}","(",")","=",",",";"]
    for symbol in symbols:
            content=content.replace(symbol," " + symbol + " ")
    words=content.split()
    return words



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
    words=tokenization(content)
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
     line=tokenization(content)
     count=0;
     datatypes=["int","float","double","char","void","long","bool","long long","short"]
     for i in range(1,len(line)):
        keyword=extract_keyword(line[i-1])
        if keyword in datatypes and "("  in line[i]:
            count+=1;
     return count;

def count_keyword(content,target_keyword):
    line=tokenization(content)
    count=0;
    for i in range(0,len(line)):
        keyword=extract_keyword(line[i])
        if keyword==target_keyword:
            count+=1
    return count

def count_variables(content):
    words = tokenization(content)

    datatypes = [
        "int", "float", "double", "char",
        "bool", "long", "short", "void"
    ]

    count = 0;
    variables = []

    for i in range(1, len(words)-1):

        previous = extract_keyword(words[i - 1])
        current = extract_keyword(words[i])
        
        if (previous in datatypes and
            current not in datatypes and
            "(" not in words[i] and
            words[i+1]!="("):

            variables.append(current)
            count += 1

    return count, variables


def count_datatypes(content):
    words=tokenization(content)
    datatypes_used=[]
    datatypes=["int","float","char","double","bool","long","short","void"]
    for i in range(0,len(words)):
        keyword=extract_keyword(words[i])
        if keyword in datatypes:
            if keyword not in datatypes_used:
                datatypes_used.append(keyword)

    datatype_count=len(datatypes_used)
    return datatype_count, datatypes_used

def count_return_statements(content):
    words=tokenization(content)
    return_statement=[]
    for i in range(0,len(words)):
        keyword=extract_keyword(words[i])
        if keyword=="return":
            if  i+1<len(words) and words[i+1] not in ["{","}"]:
                w=words[i]+ " "+words[i+1]
                return_statement.append(w)
            else :
                return_statement.append(words[i])
              
    count=len(return_statement)
    return count,return_statement

def show_variables(content):
 count, variables=count_variables(content)
 used_variables =  find_used_variables(content,variables)
 unused_variables = find_unused_variables(variables,used_variables)
 return variables,used_variables,unused_variables


def find_used_variables(content,variables):
    words=tokenization(content)
    datatypes={"int","char","string","double","long","long long","short","bool","float"}
    used_variables=[]
    for i in range(1,len(words)):   
        if words[i-1] not in datatypes:
            if words[i] in variables:
                if words[i] not in used_variables:
                    used_variables.append(words[i])
    return used_variables

def find_unused_variables(variables,used_variables):
    unused_variables=[]
    for variable in variables:
        if variable not in used_variables:
                unused_variables.append(variable)
    return unused_variables

        
