# -*- coding:utf-8 -*-
class KthNumber:
    def findKth(self, k):
        # write code here
        if k==0:return -1
        if k==1:return 3
        if k==2:return 5
        if k==3:return 7
        list1 = [3,5,7]
        list2 = [3,5,7]
        list3 = [3,5,7]
         
        for i in range(3,k):
            num = min(3*list1[0],5*list2[0],7*list3[0])
            if num==list1[0]*3:
                list1.pop(0)
                 
            if num==list2[0]*5:
                list2.pop(0)
                 
            if num==list3[0]*7:
                list3.pop(0)
                     
            list1.append(num)
            list2.append(num)
            list3.append(num)
             
        return num


if __name__ == '__main__':
    print KthNumber().findKth(16)
    for i in range(1, 20):
        print KthNumber().findKth(i)