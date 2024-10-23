import re

txt = str(input("introduceti textul aici:"))

#Check if the string has any a, r, or n characters:

x = re.findall("[aeiouAEIOU]", txt)
y = re.findall("[qwrtpsdfghjklmnbvcxzQWRTPDFGHJKLMNBVCXZ]",txt)

print("Vocale:",x)
print("Consoane:",y)