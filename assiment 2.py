# Q1. Find Grades

# Your school has the following grading system based upon the marks (M) obtained by a student:

#  If M ≤ 10, the grade will be E.
#  If 11 ≤ M ≤ 20, the grade will be D.
#  If 21 ≤ M ≤ 30, the grade will be C.
#  If 31 ≤ M ≤ 40, the grade will be B.
#  If 41 ≤ M ≤ 50, the grade will be A.

# Your friend will enter his marks out of 50, and your task is to print his grades.

M = int(input())

if M <= 10:
    print("E")
elif M <= 20:
    print("D")
elif M <= 30:
    print("C")
elif M <= 40:
    print("B")
else:
    print("A")


# Q2. Get Value

# You are provided with a table containing some characters and their corresponding values.

# P or p → PrepBytes
#  Z or z → Zenith
#  E or e → Expert Coder
#  D or d → Data Structure

# Return the value corresponding to the input character.


C = input()

if C == "P" or C == "p":
    print("PrepBytes")
elif C == "Z" or C == "z":
    print("Zenith")
elif C == "E" or C == "e":
    print("Expert Coder")
elif C == "D" or C == "d":
    print("Data Structure")


# Q3. Maximum Out of Three Numbers


# Take three numbers and return the largest number among them. If all three numbers are the same, return **-1**.
   
A, B, C = map(int, input().split())

if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B)
else:
    print(C)


# Q4. Second Smallest


# You are given three distinct integers X, Y and Z. Return the second smallest integer.

X, Y, Z = map(int, input().split())

if X < Y and Y < Z:
    print(Y)
elif X < Z and Z < Y:
    print(Z)
elif Y < X and X < Z:
    print(X)
elif Y < Z and Z < X:
    print(Z)
elif Z < X and X < Y:
    print(X)
else:
    print(Y)
# Q5. Check Whether the Triangle is Acute or Obtuse

# Write a program that takes three angles and checks whether the triangle is acute or obtuse.


A, B, C = map(int, input().split())

if A > 90 or B > 90 or C > 90:
    print("obtuse")
else:
    print("acute")