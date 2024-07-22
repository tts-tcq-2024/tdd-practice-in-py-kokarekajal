import re 
def add(varx): 
    if varx == "" or varx == "0":
        return 0
    delimiter = delimiter_call(varx)
    vary=numbers(varx,delimiter)
    result=sumnumbers(vary)
    return result
def delimiter_call(varx):
     if varx.startswith("//"):
         return varx[2]
     return ','
def numbers(varx,delimiter):
     if varx.startswith("//"):
         return varx[4:].split(delimiter)
     return re.split(rf"{re.escape(delimiter)}|\n", varx)
def sumnumbers(var2):
    return sum(parse_int(num) for num in vary if valid_number(num))
def parse_int(num_str):
    try:
        return int(num_str)
    except ValueError:
        return 0
def valid_number(num_str):
    try:
        num=int(num_str)
        return num<=1000
    except ValueError:
        return False
