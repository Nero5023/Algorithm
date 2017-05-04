ALLOW = 'allow'
DENY  = 'deny'

class TrieNode:
    def __init__(self, value = None):
        self.value = value
        self.ip0 = None
        self.ip1 = None
        self.tag = None
        self.order = None

    def __getitem__(self, key):
        if key == '0':
            return self.ip0
        if key == '1':
            return self.ip1
        raise Exception("input key error")

class Tire:
    def __init__(self):
        self.root = TrieNode()
        self.orderIter = 1

    def insert(self, ipStr, isALLOW, mask=32 ):
        if mask > 32 or mask < 0:
            return
        current = self.root
        for i in range(0, mask):
            x = ipStr[i]
            if x == '0':
                if current.ip0 is None:
                    current.ip0 = TrieNode('0')
                current = current.ip0
            else:
                if current.ip1 is None:
                    current.ip1 = TrieNode('1')
                current = current.ip1
        if current.tag is None:
            current.tag = isALLOW
            current.order = self.orderIter
            self.orderIter+=1

    def matchWithIP(self, testIPStr):
        currrent = self.root
        result = currrent.tag
        firstTime = self.orderIter
        if currrent.order is not None:
            firstTime = currrent.order

        for cha in testIPStr:
            if currrent[cha] == None:
                break
            currrent = currrent[cha]
            if currrent.tag is None:
                continue
            if currrent.tag == ALLOW:
                if currrent.order < firstTime:
                    firstTime = currrent.order
                    result = ALLOW
            if currrent.tag == DENY:
                if currrent.order < firstTime:
                    firstTime = currrent.order
                    result = DENY
        if result is None:
            result = ALLOW
        return result


def converTOIPBinStr(ipStr):
    nums = ipStr.split('.')
    nums = map(int, nums)
    ips = map(lambda x: '{0:08b}'.format(x), nums)
    return ''.join(ips)

def convertRule(rule):
    (isAllow, ipmask) = rule.split(' ')
    ipmask = ipmask.split('/')
    mask = 32
    if len(ipmask) == 2:
        mask = ipmask[1]
    return (isAllow, converTOIPBinStr(ipmask[0]), int(mask))



def checkallows(rules, checkips):
    rules = map(convertRule, rules)
    checkips = map(converTOIPBinStr, checkips)
    tire = Tire()
    for rule in rules:
        tire.insert(ipStr=rule[1], isALLOW=rule[0], mask=rule[2])
    for checkip in checkips:
        print tire.matchWithIP(checkip)




#
# def toMaskBin(maskNum):
#     mask = 0
#     remain = 32 - maskNum
#     while maskNum != 0:
#         mask = (mask << 1) + 1
#         maskNum -= 1
#     while remain != 0:
#         mask = mask << 1
#         remain -= 1
#     return mask
#
#
#
# def ifMatchRule(ip, ruleIp ,mask):
#     return (ip & mask) == (ruleIp & mask)





if __name__ == '__main__':
    # ipcheck = converTOIP("1.2.3.5")
    # web = converTOIP("1.2.3.4")
    # mask = toMaskBin(30)
    # print ifMatchRule(ipcheck, web, mask)
    rules = ["allow 1.2.3.4/30", "deny 1.1.1.1", "allow 127.0.0.1", "allow 123.234.12.23/3", "deny 0.0.0.0/0"]
    ips = ["1.2.3.4", "1.2.3.5", "1.1.1.1", "100.100.100.100", "219.142.53.100"]
    checkallows(rules, ips)
