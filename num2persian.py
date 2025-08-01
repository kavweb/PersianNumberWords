planeA = {
    "1":["صد","planB","یک"],
    "2":["دویست","بیست","دو"],
    "3":["سی صد","سی","سه"],
    "4":["چهارصد","چهل","چهار"],
    "5":["پانصد","پنجاه","پنج"],
    "6":["ششصد","شصت","شش"]}
planBData = ["ده","یازده","دوازده","سیزده","چهارده","پانزده","شانزده","هفده","هجده","نوزده"]
module = ["هزار","میلیون","میلیارد"]
finallText = ""
usePB = False
counter = 0
userEntry = input("put you number to chenge it into the persian  ... ")
def checkAnd(checkCounter):
    if (checkCounter+1)%3!=0 or checkCounter==0:
        return " و "
    else:
        return " "
if userEntry:
    for item in userEntry:
        if 0<=counter<=2 and len(userEntry) > 0 and item != 0 :
            tempNum = planeA[item][counter]
            finallText = finallText + tempNum + checkAnd(counter)
        counter+=1

print(finallText)