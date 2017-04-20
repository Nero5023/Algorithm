# -*- coding:utf-8 -*-

class Finder:
    def findString(self, s, n, x):
        # write code here
        return self.findStringIter(s, 0, n-1, x)

    def findStringIter(self, strArr, start, end, target):
        if start > end:
            return None
        mid = (start + end)//2
        value = strArr[mid]
        if value == target:
            return mid
        if value == "":
            left = self.findStringIter(strArr, start, mid-1, target)
            right = self.findStringIter(strArr, mid+1, end, target)
            if left is None and right is None:
                return None
            elif left is None:
                return right
            else:
                return left
        if value < target:
            return self.findStringIter(strArr, mid+1, end, target)
        else:
            return self.findStringIter(strArr, start, mid-1, target)

if __name__ == '__main__':
    print Finder().findString(["","","","","","","AECOGS","AOOFYXQ","AQ","AVMMTXNXRA","BAXEVHLYME","BCA","BUV","BVTPMOLHLC","BX","CBDHCOMI","CDWGWW","CLG","CODB","CWKIYFYHNIY","CZA","D","DEMJMHQYMC","DFLYAK","DRR","DVMVXK","EIHULX","EOTCMEXHH","ETYGMD","EXXHWDPS","GNVM","GVEBGEFC","HEFVFXDND","HOUUXMYVC","IDPNQI","IIODZQF","IVPD","JEGHXQCTTNT","JJXNXIYGH","JZBCHVIHK","LIDN","LLKIIAZ","MCBFFHFJBLT","MRTYDDIM","MVWD","N","NJBXRKL","NLEMZIZ","NMMQL","NQQRGMAN","NUO","O","OBC","ONES","OPP","OXOPR","Q","QBZNAE","QCK","QGR","QKLUDC","RWASPGXEUJY","TDDWTG","TER","TTZK","TV","UGUJUEU","UIQYOL","USQENKTCEGJ","UZ","V","VDGRM","VNEFQVOGRYX","VQNFRIPQR","WHLNXPTCPAI","WNYVMOYJBCY","WSZQBUGJO","WVPZVAWYJJ","X","XMTDBDND","XPANBKVAKB","XTPYTK","Y","ZUDJMEVLQJN"],84,"TER")