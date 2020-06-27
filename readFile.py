
tf = open("F:/备忘录.txt","a+")
tf.write("李琳你在哪儿?")
tf.seek(0)
for line in tf.readlines():
    print(line)

'''
tf.close()
tf = open("F:/备忘录.txt","wt+a")
tf.write("李琳你哪儿?")
for line in tf.readlines():
    print(line)

tf.close()
'''