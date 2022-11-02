from time import time


x1 = time()
f = open('fyaml.txt', 'r')
ms = f.readlines()
for i in range(len(ms)):
    zn = ms[i]
    ms[i] = zn[:-1]
f.close()
ans = []
for i in range(len(ms)):
    if ms[i] != "---" and ms[i] != "lessons: ":
        if ms[i][0] + ms[i][1] != "  " and ms[i][0] + ms[i][1] != "- ": 
            st = ms[i].split(": ")
            itg = "<" + st[0] + ">" + st[1] + "</" + st[1] + ">"
            ans.append(itg)
        else:
            if ms[i][0] == "-":
                ans.append("</lessons>")
                ans.append("<lessons>")
                gl = ms[i][2:]
                st = gl.split(": ")
                itg = "  <" + st[0] + ">" + st[1] + "</" + st[0] + ">"
                ans.append(itg)
            else:
                if ms[i][2] == "-":
                    gl = ms[i]
                    st = gl.split("- ")[1]
                    itg = "  <" + "weeks" + ">" + st + "</" + "weeks" + ">"
                    ans.append(itg)
                else:
                    if ms[i][0] + ms[i][1] == "  ":
                        gl = ms[i][2:]
                        st = gl.split(": ")
                        itg = "  <" + st[0] + ">" + st[1] + "</" + st[0] + ">"
                        ans.append(itg)
                    
                    
ans.append("</lessons>")                    
itg = open('res_hand1.txt', 'w')
for i in range(len(ans)):
    if i !=1:
        itg.write(ans[i] + '\n')
                
print(f'Время выполнения:\t{time() - x1}')