'''
	8kyu - Range Extraction
	https://www.codewars.com/kata/range-extraction/solutions/python
'''

def solution(args):
    arr = ''
    flag = True
    pre = 0
    count = 0
    for i in args:
        if flag:
            arr+=str(i)
            pre = i
            flag = False
            count = 0
        else:
            if i != pre+1:
                if count!=0:
                    if count > 1:
                        arr+='-'
                    else:
                        arr+=','
                    arr+=str(pre)
                arr+=','
                arr+=str(i)
                count = 0
            else:
                count+=1
            pre = i
    if count != 0:
        if count > 1:
              arr+='-'
        else:
              arr+=','
        arr+=str(pre)
    return arr