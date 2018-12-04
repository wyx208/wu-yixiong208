import jieba
excludes={"不得","这会子","到底","一句","原来","家里","姊妹","什么","一声","妹妹","不用","媳妇","看见","人家","如何","听说","问道","小丫头","今儿","罢了","那些","屋里","一回","这话","外头","自然","打发","哪里","不能","这么","几个","还有","只管","说话","那边","心里","二爷","她们","如此","银子","今日","二人","答应","出去","所以","不过","不好","姐姐","的话","一时","鸳鸯","过来","东西","丫头","这些","他们","不敢","告诉","袭人","回来","只是","大家","老爷","只得","太太","听见","这样","进来","咱们","就是","一面","只见","两个","没有","怎么","不是","不知","这个","一个","我们","你们","如今","说道","老太太","知道","姑娘","起来","这里","出来","众人","那里","奶奶","自己"}
txt=open("红楼梦.txt","r",encoding='GB18030').read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=='凤姐' or word=='熙凤':
        rword='凤姐'
    else:
        rword=word
    counts[word] = counts.get(word,0)+1
for word in excludes:
    del(counts[word])
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word,count=items[i]
    print ("{0:<10}{1:>5}".format(word,count))
