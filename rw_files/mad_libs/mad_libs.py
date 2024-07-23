"""
program which pulls out text from text file, replaces certain words 
with user's input text and creates new file with substituted text
1. read info from text file
2. enter input
3. replace words from text file with user's input
4. save new file
"""

def read_file():
    text = open('lotr.txt',)
    text_arr = text.readlines()
    str_text = ""
    str_text = str_text.join(text_arr)
    return str_text


def input_words():
    noun = input("Please, enter noun: ")
    verb = input("Please, enter verb: ")
    adjective = input("Please, enter adjective: ")
    adverb = input("Please, enter adverb: ")
    return noun, verb, adjective, adverb

def replace_new_info(text, users_input):
    if "NOUN" in text:
        new_text = text.replace("NOUN", users_input[0])
    if "VERB" in text:
        new_text = text.replace("VERB", users_input[1])
    if "ADJECTIVE" in text:
        new_text = text.replace("ADJECTIVE", users_input[2])
    if "ADVERB" in text:
        new_text = text.replace("ADVERB", users_input[3])
    return new_text

def write_into_file(new_text):
    new_text_file = open("new_text_lotr.txt", "w")
    new_text_file.write(new_text)
    new_text_file.close()

def main():
    new_text = replace_new_info(read_file(), input_words())
    write_into_file(new_text)

main()