planeA = {
    "1":["یک","planB","صد"],
    "2":["دو","بیست","دویست"],
    "3":["سه","سی","سی صد"],
    "4":["چهار","چهل","چهارصد"],
    "5":["پنج","پنجاه","پانصد"],
    "6":["شش","شصت","ششصد"]}
planB = ['ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده']
module = ["میلیارد","میلیون","هزار"]
finallText = []
usePB = False
checkAnd = False

counter = 0
userEntry = input("put you number to chenge it into the persian  ... ")
def checkAndFunc(checkCounter):
    print (checkAnd)
    if checkCounter != 0 or checkAnd == False:
        return " و "
    else:
        return " "
def addNumberToArray(number,counter):
    changeNumberToP = planeA[number][counter]
    finallText.append(changeNumberToP)
    
if userEntry:
    userEntryLen = len(userEntry)
    if userEntryLen%3==1:
        tempNum = userEntry[0]
        addNumberToArray(tempNum,counter=0)
        userEntry = userEntry[1:]
    elif userEntryLen%3==2:
        tempNum = userEntry[0:2]
        counter = 1
        for num in tempNum:
            addNumberToArray(num , counter)
            counter -= 1
        userEntry = userEntry[2:]
    for i in range(int(len(userEntry)/3)):
        tempNum = userEntry[0:3]
        userEntry = userEntry [3:]
        counter = 2
        for itemA in tempNum:
            addNumberToArray(itemA,counter)
            counter-=1
print(finallText)