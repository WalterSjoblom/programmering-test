
första = int(input("Mata in basen->"))
andra = int(input("Mata in höjden->"))

print(f"Triangelns area är: {första*andra}")




def get_price_type(age):
        if age > 19:
            print("vuxen")
        elif age < 15:
            print("barn")
        else:
            print("ungdom")

print(get_price_type(14))





start = 144
slut = 2470
total = 0

for i in range(start, slut + 1):
    total += i 

print("Summan är:", total)






def parts_nonoverlap(s, n):
    seen = set()
    for i in range(0, len(s) - n + 1, n):
        part = s[i:i+n]
        if part not in seen:
            print(part)
            seen.add(part)

parts_nonoverlap("8999382739737", 4)






def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("legolas"))



