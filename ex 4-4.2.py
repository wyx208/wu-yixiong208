c,n,b,o=0,0,0,0
strs=input("请随意输入一行字符，包括字母，数字，空格等:")
for s in strs:
    if ord('a')<=ord('2')or ord('A')<=ord(s)<=ord('2'):
        c+=1
    elif ord('0')<=ord(s)<=ord(s)<=ord('9'):
        n+=1
    elif ord(' ')==ord(s):
        b+=1
    else:
        o+=1
print("包含字母{0}个，数字{1}个，空格{2}个，其他字符{3}个".format(c,n,b,o))
