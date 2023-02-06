def count_string(str):
    cnt = 0
    
    for string in str:
        if len(string) > 2 and string[0] == string[-1]:
            cnt +=1
    return cnt

string = ["abc", "ada", "121", "123"]
print("Number of strings: ", count_string(string))