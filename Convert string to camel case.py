#Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"

#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

#"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

# My Answer
def to_camel_case(text):
    new_text=""
    i=0
    while i<len(text):
        if text[i]=="-" or text[i]=="_":
            new_text += text[i+1].upper()
            i+=2
        else:
            new_text += text[i]
            i+=1
    return new_text

# Best Answer

def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
