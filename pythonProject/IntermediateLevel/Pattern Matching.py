# Pattern Matching with Regex
# Regular expressions, also called regex, are descriptions of a pattern of text.
# It can detect the presence or absence of a text by matching it with a particular pattern and also can split a pattern into one or more sub-patterns.
# For example, a \d in a regex stands for a digit character — that is, any single numeral between 0 and 9.
# Check Phone Numbers Using Regex In Python - \d\d\d-\d\d\d-\d\d\d\d
#  adding a 3 in curly brackets ({3}) after a pattern is like saying, “Match this pattern three times.”
#  So the slightly shorter regex is as follows:  \d{3}-\d{3}-\d{4}

import re

# regex object
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')- Phone number found
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')   # For separating the area code from mobile number
mo = phoneNumRegex.search('My number is 011-555-4242.')
# print('Phone number found: ' + mo.group())      # Output is Phone number found: 415-555-4242

# Parentheses for Grouping and Capturing with Regex
# One of the ways of pattern matching with Regex is by using Parentheses around the patterns.
# Separate the area code from mobile number

print(mo.group(1))
areaCode, number = mo.groups()
print("area code:", areaCode)
print("number:", number)

# Match a parenthesis
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))     # Output is (415)

# Grouping and the Pipe Character(|)
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())     # Output is 'Batman'

# Understanding Curly Braces in Regex
# (Hi){3} will match the string as 'HiHiHi'
# (Hi){3,5} - 'HiHiHi', 'HiHiHiHi' and 'HiHiHiHiHi'
# (Hi){3,}  will match with three or more instances
# (Hi){,4} will match with 0 to 5 instances.

haRegex = re.compile(r'(Hi){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())    # Output is HiHiHi

# Occurrence of the pattern using curly brackets and then search for if a specific pattern exists in it or not.
haRegex = re.compile(r'(Ha){3}')
mo2 = haRegex.search('Ha')== None
print(mo2)         # Output is True

# Optional Operator or question mark (?) in Regular Expression
# The “?” character flags the group that precedes it as an optional part of the pattern.
# (wo)? - the pattern wo is an optional group - The regex will match text that has zero instances or one instance of wo in it.
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
print(mo2.group())      # Output is Batman,Batwoman

# Zero or More Pattern Matching with the Star
# The * (called the star or asterisk) means “match zero or more” - It can be completely absent or repeated over and over again
# To match an actual star character, prefix the star in the regular expression with a backslash, \*.
# (wo)* part of the regex matches zero instances of wo in the string.
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())   # Output is Batman

# To match at least one occurrence of a pattern in the string.

batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())    # Output is Batwoman

# To match more than one occurrence of a pattern in the string.

batRegex = re.compile(r'Bat(wo)*man')
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())     # Output is Batwowowowoman

# One or More Pattern Matching with the Plus
# * means “match zero or more,” the + (or plus) means “match one or more.”
# +Plus - the group preceding a plus must appear at least once. It is not optional.
# To match an actual plus sign character, prefix the plus sign with a backslash to escape it: \+.

# match at least one occurrence of a pattern in the string.
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())    # Output is Batwoman

# the regex Bat(wo)+man will not match the string ‘The Adventures of Batman’ because at least one wo is required by the plus sign.
batRegex = re.compile(r'Bat(wo)+man')
mo3 = batRegex.search('The Adventures of Batman')== None
print(mo3)      # Output is True










