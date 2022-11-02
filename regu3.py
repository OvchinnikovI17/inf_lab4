import re
from time import time

x1 = time()
#pattern1 
pat1 = r'^([a-zA-z]+)(: )(.+)'
#pattern2
pat2 = r'^([a-zA-z]+)(:)( )$'
#pattern3
pat3 = r'(- )([a-zA-z]+)(:)(.+)'
#pattern4
pat4 = r'(  )([a-zA-z]+)(:)( )$'
#pattern5
pat5 = r'^(  - )[0-9]+'
#pattern6
pat6 = r'(  )([a-zA-z]+)(: )(.+)'

f = open('fyaml.txt', 'r')
ms = f.readlines()
for i in range(len(ms)):
    zn = ms[i]
    ms[i] = zn[:-1]
f.close()
ans = []

for i in ms:
    st = i
    sct = re.search(pat3, st) 
    if sct:
        ans.append("</lessons>")
        ans.append("<lessons>")
        st = st[2:]
        match = re.split(r': ', st)
        ans.append("  <" + match[0] + ">" + match[1] + "</" + match[0] + ">")
    else:
        sct = re.search(pat5, st)
        if sct:
            match = re.split(r'- ', st)
            ans.append("  <weeks>" + match[1] + "</weeks>")
        else:
            sct = re.search(pat6, st)
            if sct:
                st = st[2:]
                match = re.split(r': ', st)
                ans.append("  <" + match[0] + ">" + match[1] + "</" + match[0] + ">")
            else:
                sct = re.search(pat2, st)
                if sct:
                    match = re.split(r': ', st)
                    ans.append("<" + match[0] + ">")
                else:
                    sct = re.search(pat1, st)
                    if sct:
                        match = re.split(r': ', st)
                        ans.append("<" + match[0] + ">" + match[1] + "</" + match[0] + ">")
ans.append("</lessons>")


itg = open('res_regu3.txt', 'w')        
              
for i in range(len(ans)):
    if i != 1 and i != 2:
        itg.write(ans[i] + '\n')
        
        
print(f'Время выполнения:\t{time() - x1}')