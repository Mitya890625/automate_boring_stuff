import re

def regex_formatter(input_string):
    try:
        regex_p = re.compile(r"\d{2}/\d{2}/\d{4}")
        mo = regex_p.search(input_string)
        if mo == None:
            raise ValueError("Date format is wrong or absent in text"
)
        return mo.group()
    except ValueError:
        return "Wrong format or there is no match in text"



res = input("Enter the date:")
print(regex_formatter(res))