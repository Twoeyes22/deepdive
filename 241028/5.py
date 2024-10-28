def repeat_n_times(x,n):
    result = ""
    if type(x) == "str" :
        for i in range(n):
            result+=x
    else:
        return x*n
    return result

if  __name__ == "__main__":
    print(repeat_n_times(3,4))