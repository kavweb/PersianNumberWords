data = {
    "1":["یک","planB","صد"],
    "2":["دو","بیست","دویست"],
    "3":["سه","سی","سی صد"],
    "4":["چهار","چهل","چهارصد"],
    "5":["پنج","پنجاه","پانصد"],
    "6":["شش","شصت","ششصد"]}
planBData = ["ده","یازده","دوازده","سیزده","چهارده","پانزده","شانزده","هفده","هجده","نوزده"]
module = ["هزار","میلیون","میلیارد"]
finallText = ""
counter = 0
userEntry = input("put you number to chenge it into the persian  ... ")
if userEntry:
    for item in userEntry:
        if 0<=counter<=2 and len(userEntry) > 0:
            tempNum = data[userEntry]
            print(tempNum[counter])
            counter+=1
            