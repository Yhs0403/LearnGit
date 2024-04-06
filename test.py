def FrequencyList(string, number=5):
    res={}
    for i in string:
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    sorted_res = dict(sorted(res.items(), key=lambda item: item[1],reverse=True))
    return sorted_res

def main():
    sort=FrequencyList(input("请键入需要排序的字符串："),input("请键入需要输出的字符数："))
    print(sort)

if __name__=='__main__':
    main()