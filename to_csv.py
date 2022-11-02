from time import time

x1 = time()
f = open('fyaml.txt', 'r')
ms = f.readlines()
for i in range(len(ms)):
    zn = ms[i]
    ms[i] = zn[:-1]
f.close()
ans = []

itg = open('res_to_csv.txt', 'w')  

fl = 0
coun = 0
tabl = ""
for i in ms:
    st = i
    if st[0] == "-" and st[1] == " ":
        coun = coun + 1
        if coun == 2:
            break
        st = st[2:]
        mt = st.split(": ")
        tabl = tabl + mt[0] + " "
    if st[0] == " " and st[1] == " " and st[2] == "-":
        tabl = tabl + "weeks/" + str(fl) + " "
        fl = fl + 1
    else:
        if st[0] == " " and st[1] == " " and "weeks" not in st:
            st = st[2:]
            mt = st.split(": ")
            tabl = tabl + mt[0] + " "
            
itg.write(tabl + '\n')

tabl = ""
for i in ms:
    st = i
    if st[0] == "-" and st[1] == " ":
        itg.write(tabl[:-1] + '\n')
        tabl = ""
        mt = st.split(": ")
        tabl = tabl + mt[1] + ","
    else:
        if st[0] == " " and st[1] == " " and st[2] == "-":
            mt = st.split("- ")
            tabl = tabl + mt[1] + ","
        else:
            if st[0] == " " and st[1] == " " and "weeks" not in st:
                mt = st.split(": ")
                tabl = tabl + mt[1] + ","
                
                
itg.write(tabl[:-1] + '\n')