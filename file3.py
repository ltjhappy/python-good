
fo = open("f.txt","w+")
ls = ["KBKV","心怡","小艾","宝马7系","有钱人"]
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()
