def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    if len(s) <= 6 and len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha():
             for each in s:
                if each.isdigit():
                    if  not s[-1].isdigit():
                        return False
                    for i in s:
                        if not i.isdigit() and not i.isalpha():
                            return False
                        if i.isdigit() and i != s[-1]:
                          if s[s.index(i) + 1].isalpha():
                             return False
                    if each == '0':
                        return False
                    break
             return True
    return False




main()