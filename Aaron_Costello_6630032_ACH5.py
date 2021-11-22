import re


source= "Lorem ipsum doflor szit ametß, Aaron consqecytetu$r adipibsching elit, Costello sed do eiusmod tewmporα incid6kgidunt 6630032 ut labq8ore et café dolore_ magna aliqua. Purus! sit{|}~ \t\n\r\x0b\x0c amet volutpat cons&jequat mau7ris. Penaxtibus et"

a= re.findall("a",source)
print('There are', len(a),"letter a's in the text")

b= re.findall('\d',source)
print('there are', len(b),'digits in the text')

c= re.findall('\w',source)
print('there are', len(c),'alphanumeric characters in the text')

d= re.findall('\W',source)
print('there are', len(d),'non alphanumeric characters in the text')

e= re.findall('\s',source)
print('there are', len(e),'whitespace characters in the text')

