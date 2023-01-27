# question 1
def perfect(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
        return divisors_sum == n


n = int(input("enter a number = "))
print(perfect(n))

# question 2
def palindrome(string):
    return string == string[::-1]

s = input("enter a word : ")
print(palindrome(s))

# question 3
def pascal_triangle(n):
    for i in range(n):
        row = [1]
        for j in range(1, i + 1):
            row.append(row[j - 1] * (i - j + 1) // j)
        print(row)

n = int(input("enter the number of rows: "))
print(pascal_triangle(n))

# question 4
import string

def is_pangaram(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in str.lower():
            return False

        return True

string = ' the quick brown fox jumps over the lazy dog'
if (is_pangaram(string) == True):
    print("yes")
else:
    print("no")

# question 5
def sort_words(sentence):
    words = sentence.split("-")
    words.sort()
    return "-".join(words)

sentence = input("enter a sentence which is hyphen seperated: ")
sorted_sentence = sort_words(sentence)
print("sorted sentence", sorted_sentence)

# question 6
def student_data(student_id, student_name=None, student_class=None):
    print("student ID:", student_id)
    if student_name is not None and student_class is not None:
        print("Student Name:", student_name)
        print("Student Class:", student_class)

a = input("enter data=")
print(student_data(a))

# question 7
class student:
    pass

class marks:
    pass

student_1 = student()
student_2 = student()
marks_1 = marks()
marks_2 = marks()

print(isinstance(student_1, student))
print(isinstance(student_2, student))
print(isinstance(marks_1, marks))
print(isinstance(marks_2, marks))

print(issubclass(student, object))
print(issubclass(student, object))

# question 8
class sumtozero:
    def _init_(self, arr):
        self.arr = arr

    def find_triplets(self):
        triplets = []
        self.arr.sort()
        for i in range(len(self.arr) - 2):
            if i > 0 and self.arr[i] == self.arr[i - 1]:
                continue
            l = i + 1
            r = len(self.arr) - 1
            while l < r:
                total = self.arr[i] + self.arr[r] + self.arr[i]
                if total == 0:
                    triplets.append([self.arr[i], self.arr[l], self.arr[r]])
                    l += 1
                    r -= 1
                    while l < r and self.arr[l] == self.arr[l - 1]:
                        l += 1
                    while l < r and self.arr[r] == self.arr[r + 1]:
                        r -= 1
                elif tutorial < 0:
                    l += 1
                else:
                    r -= 1
        return triplets

# question 9
class Parentheses:
    def _init_(self, string):
        self.string = string
        self.stack = []

    def is_valid(self):
        for char in self.string:
            if char in "({[":
                self.stack.append(char)
            elif char in ")}]":
                if not self.stack:
                    return False
                if char == ")" and self.stack[-1] != "(":
                    return False
                if char == "{" and self.stack[-1] != "{":
                    return False
                if char == "[" and self.stack[-1] != "[":
                    return False
                self.stack.pop()
        if not self.stack:
            return True
        else:
            return False

string = input("enter a string of parentheses:")
p = Parentheses(string)
print(p.is_valid())