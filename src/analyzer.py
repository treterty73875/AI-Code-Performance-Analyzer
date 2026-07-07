def analyze_content(content):
    line_count=count_lines(content)
    word_count=count_words(content)
    blank_line_count=count_blank_lines(content)
    character_count=count_characters(content)
    return line_count, word_count, blank_line_count, character_count


def count_lines(content):
    lines=content.split("\n")
    count=0;
    for i in range(0,len(lines)):
        count+=1
    return count;


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


