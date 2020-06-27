
fo = open("f.txt","w+")
ls = ["李琳","心怡","小艾"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()