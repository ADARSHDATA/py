"""Q1. Count Uppercase and Lowercase Letters
Simple Question
Take a string from the user. Print:
Number of uppercase letters
Number of lowercase letters
Answer"""
"""s = input()

upper = 0
lower = 0

for ch in s:
    if ch >= 'A' and ch <= 'Z':
        upper += 1
    elif ch >= 'a' and ch <= 'z':
        lower += 1

print(upper)
print(lower)"""
"""Q2. Count Repeated Characters
Simple Question
Print the letters that appear more than one time.
Answer"""
"""s = input()

done = ""

for ch in s:
    if ch not in done:
        count = 0
        for x in s:
            if ch == x:
                count += 1
        if count > 1:
            print(ch, count)
        done += ch"""
"""Q3. Count Vowels
Simple Question
Count how many vowels are in the string.
Answer"""
"""s = input()

count = 0

for ch in s:
    if ch in "aeiouAEIOU":
        count += 1

print(count)"""
"""Q4. Join Two Strings
Simple Question
Take two strings and join them.
Answer"""
"""a = input()
b = input()

c = a + b

print(c)"""
"""Q5. Find Length of String
Simple Question
Find the length without using len().
Answer"""
"""s = input()

count = 0

for ch in s:
    count += 1

print(count)"""
"""Q6. Find Winner
Simple Question
String contains only A and D.
If A is more → Aditya
If D is more → Danish
If equal → Draw
Answer"""
"""s = input()

a = 0
d = 0

for ch in s:
    if ch == 'A':
        a += 1
    elif ch == 'D':
        d += 1

if a > d:
    print("Aditya")
elif d > a:
    print("Danish")
else:
    print("Draw")"""
"""Q7. Join Two Words
Simple Question
Take two words and join them.
Answer"""
"""a = input()
b = input()

print(a + b)"""
"""Q8. Palindrome
Simple Question
Check whether the string is the same from both sides.
Answer"""
"""s = input()

if s == s[::-1]:
    print("True")
else:
    print("False")"""
"""Q9. Reverse String
Simple Question
Print the string in reverse order.
Answer"""
"""s = input()

print(s[::-1])"""
"""Q10. Compare Two Strings
Simple Question
If both strings are same print YES else NO.
Answer"""
"""a = input()
b = input()

if a == b:
    print("YES")
else:
    print("NO")"""
"""Q11. Replace Word
Simple Question
Replace "You" with "Prepbytes".
Answer"""
"""s = input()

print(s.replace("You", "Prepbytes"))"""
"""Q12. Split String
Simple Question
Print every word on a new line.
Answer"""
"""s = input()

words = s.split()

for w in words:
    print(w)"""
"""Q13. Count Vowels and Consonants
Simple Question
Count:
Vowels
Consonants
Answer"""
"""s = input()

vowel = 0
consonant = 0

for ch in s:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            vowel += 1
        else:
            consonant += 1

print(vowel)
print(consonant)
"""