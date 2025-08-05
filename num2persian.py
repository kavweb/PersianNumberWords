planA = {
    "1":["یک","planB","صد"],
    "2":["دو","بیست","دویست"],
    "3":["سه","سی","سی صد"],
    "4":["چهار","چهل","چهارصد"],
    "5":["پنج","پنجاه","پانصد"],
    "6":["شش","شصت","ششصد"]}
planB = ['ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده']
module = ["میلیارد","میلیون","هزار"]
finalArray = []
result = ""
checkAnd = False
counter = 0
usePB = False

userEntry = input("put you number to chenge it into the persian  ... ")

def add_number_2_array( number, counter):

    if number != '0': 
        changeNumberToP = planA[number][counter]
        finalArray.append(changeNumberToP)

    else:
        finalArray.append(" ")

def number_to_array_4_planeB(number):
    changeNumberToP = planB[int(number)]
    finalArray.append(changeNumberToP)


if userEntry:
    userEntryLen = len(userEntry)
    
    if userEntryLen %3 == 1:
        tempNum = userEntry[0]
        counter = 0
        add_number_2_array(tempNum,counter)
        userEntry = userEntry[1:]
        
    elif userEntryLen % 3 == 2:
        tempNum = userEntry[0:2]
        counter = 1
        for num in tempNum:
            if counter == 1 and num == "1":
                usePB = True
                
            elif usePB:
                number_to_array_4_planeB(num)
                usePB = False
                
            else:
                add_number_2_array(num , counter)

            counter -= 1

        userEntry = userEntry[2:]
        
    for i in range(int(len(userEntry) /3)):
        tempNum = userEntry[0:3]
        userEntry = userEntry [3:]
        counter = 2
        
        for itemA in tempNum:
            if counter == 1 and itemA == "1":
                usePB = True
                
            elif usePB:
                number_to_array_4_planeB(itemA)
                usePB = False
                
            else:
                add_number_2_array(itemA , counter)
                
            counter-=1
            
            
            
print(finalArray)