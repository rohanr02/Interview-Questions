s1 ="part"
s2 ="trap"

def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("Valid anagram")
    else:
        print("Inalid anagram")

check(s1, s2)
