# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re
s1="prashants"
i=re.compile(r'([a-z][A-Z][0-9])',s1)
