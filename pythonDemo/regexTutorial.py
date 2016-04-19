import re
st="hello<nn>ss hello<aa>ss hello<kk>ss"
matchs = re.findall(r'he(.8?)o<(.*?)>ss',st,re.DOTALL)
print(matchs)