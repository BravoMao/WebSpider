import re
st="hello<nn>ss hello<aa>ss hello<kk>ss"
matchs = re.findall(r'hello<(.*?)>ss',st,re.DOTALL)
print(matchs)