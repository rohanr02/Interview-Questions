s1 ="sale"
s2 ="seal"

def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("Valid anagrams")
    else:
        print("Invalid anagrams")

check(s1, s2)
