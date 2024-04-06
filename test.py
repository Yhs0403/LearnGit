def FrequencyList(str : str, num : int=5):
    n=int(num)
    res={}  #统计原始字符串中各字符的出现频率，储存于res字典中
    for i in str:
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    SortedRes = sorted(res.items(), key=lambda x: x[1],reverse=True)    #对Res按照Value从大到小进行排序，存储于列表SortedRes中
    SortedRes = SortedRes[:n]   #取SortedRes中前num个值
    NSortedRes= {}  #创建用于存储输出值的字典NSortedRes，其中键为整理好的SortedRes中的值，值为对应字符的频率
    for i in SortedRes:
        p=i[0]
        NSortedRes[p]=i[1]
    return NSortedRes


def main():
    sort=FrequencyList(input("请键入需要排序的字符串："),input("请键入需要输出的字符数："))
    print(sort)

if __name__=='__main__':
    main()