import unittest
import re
import string


#exercise 1
def maxs(num, num2):
    if num > num2:
        return True
    return False

#exercise 2
def max_of_three(a, b, c):
    ans = []
    ans.append((a, b, c))
    for n in ans:
        return max(n)


#exercise 3
def getLength(string):
    ans = 0
    for n in string:
        ans = ans + 1
    return ans

#exercise 4
def is_vowel(vowel):
    vowels = ["A", "E", "O", "I", "U"]
    lower_value = [x.lower() for x in vowels]
    if vowel in vowels or vowel in lower_value:
        return True
    else:
        return False

#exercise 5
def translate(string):
    ans = []
    vowels = ['a', 'e', 'o', 'i', 'u']
    for n in string:
        if  n == " ":
            ans.append(" ")
        if not  n in vowels and not n == " ":
            a = n + 'o' + n
            ans.append(a)
        else:
            ans.append(n)
    join_ans ="".join(ans)
    return join_ans

#exercise 6
def sum(list1):
    ans = 0
    for n in list1:
        ans = n + ans
    return ans

def multiplicity(list1):
    ans = 1
    for n in list1:
        ans = ans * n
    return ans

#exercise 7
def reverse(string):
    return string[::-1]

#exercise 8
def is_palindrome(string):
    return string == string[::-1]




#exercise 9
def is_member(value, list1):
    if value in list1:
        return True
    return False


#exercise 10
def member(list1, list2):
    for n in list1:
        for b in list2:
            if n == b:
                return True
    return False



#exercise 11
def generate_n_chars(num, char):
    return  char * num


#exericse 12
def histogram(list1):
    ans = "*"
    more = " "
    for n in list1:
         more = ans * n
         print more


#exericse 13
def max_in_list(list1):
    ans = 0
    for n in list1:
        if n > ans:
            ans = n
    return ans

#exercise 14
def map_list(list1):
    length = [len(x) for x in list1]
    return length


#exercise 15
#you can also just use max() for this
def find_longest_word(lst):
    get_length = [len(x) for x in lst]
    ans = 0
    for n in get_length:
        if n > ans:
            ans = n
    return ans



#exercise 16
def filter_long_words(list1, n):
    result = []
    for b in list1:
        if len(b) > n:
            result.append(b)
    return result


#exercise 17
def palindrome(string):
    to_lower = string.lower()
    only_letters = " ".join(re.findall("[a-zA-Z]+", to_lower))
    return only_letters == "".join(reversed(only_letters[::-1]))


#exercise 18
def panagram(str1):
    a = string.ascii_lowercase
    compare = []
    to_lower = [x.lower().strip() for x in str1]
    alpha =  "".join(sorted(set(to_lower)))
    if len(alpha) == len(a):
        if alpha == a:
            return True
    return False

#exercise 19
def beer():
    for n in reverse(range(1, 100)):
       print str(n) + " bottles of beer on the wall " + str(n) + " bottles of beer. \n"" \
       ""Take one down, pass it around, " + str(n-1) + " bottles of beer on the wall."



#exercise 20
def translate_english(string1):
    dictionary = {"merry": "god", "christmas": "jul", "and": "och",
                  "happy": "gott", "new": "nytt", "year": "ar"}
    to_lower = [x.lower() for x in string1]
    app = []
    for n in to_lower:
        if n in dictionary:
            app.append(dictionary[n])
    return app


