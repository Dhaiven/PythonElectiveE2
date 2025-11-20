def artdecode(list):
    result = ""
    for value in list:
        result += value[0] * value[1]
    return result

if __name__ == "__main__":
    print(artdecode([('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]))