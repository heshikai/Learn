#!/usr/bin/python

dict1 = {'a':1,'bc':{'b':2,'c':3},'d':4}

print(dict1)


def print_di(param_dict,n):    
    print("{")
    for key in param_dict.keys():
        print("\t"*n,key,":",end = "")
        value = param_dict[key]
        if isinstance(value,dict):
            print_di(value,n+1)
        else:
            print(value)
        
    print("\t"*(n-1),"}")

print_di(dict1,0)