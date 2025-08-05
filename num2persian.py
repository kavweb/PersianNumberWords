planA = {
    "1":["یک","planB","صد"],
    "2":["دو","بیست","دویست"],
    "3":["سه","سی","سی صد"],
    "4":["چهار","چهل","چهارصد"],
    "5":["پنج","پنجاه","پانصد"],
    "6":["شش","شصت","ششصد"],
    "7":["هفت","هفتاد","هفتصد"],
    "8":["هشت","هشتاد","هشتصد"],
    "9":["نه","نود","نهصد"]
    }
planB = ['ده', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده']
module = ["هزار","میلیون","میلیارد","تریلیون","کوادریلیون","کوینتیلیون","سیکستیلون","سپتیلیون","اکتیلیون","نونیلیون","دسیلیون","آندسیلیون","دودسیلیون","تریدسیلیون","کواتردسیلیون","کویندسیلیون","سیکسدسیلیون","سپتندسیلیون","اکتودسیلیوم","نومدسیلیون"]
finalArray = []
result = ""
checkAnd = False
counter = 0
usePB = False

userEntry = input("put you number to chenge it into the persian  ... ")

def add_number_2_array( number, counter , division):
    '''
        This function adds all numbers to the array except numbers between 11 and 19.
    '''
    if number != '0': 
            
        changeNumberToP = planA[number][counter]
        finalArray.append(changeNumberToP)
        
        if counter == 1 or counter==2:
            finalArray.append("و")
        elif division >= 0 :
            finalArray.append(module[division])
            finalArray.append("و")
    
def number_to_array_4_planeB(number,division):
    '''
        This function else of add_number_2_array
    '''
    changeNumberToP = planB[int(number)]
    finalArray.append(changeNumberToP)
    finalArray.append(module[division])
    finalArray.append("و")

if userEntry:
    userEntryLen = len(userEntry)
    userEntrylenDivision = int((userEntryLen/3)-2)
    
    if userEntryLen %3 == 1:
        tempNum = userEntry[0]
        counter = 0
        add_number_2_array(tempNum, counter, userEntrylenDivision)
        userEntry = userEntry[1:]
        userEntrylenDivision -= 1
        
    elif userEntryLen % 3 == 2:
        tempNum = userEntry[0:2]
        counter = 1
        
        for num in tempNum:
            if counter == 1 and num == "1":
                usePB = True
                
            elif usePB:
                number_to_array_4_planeB(num , userEntrylenDivision)
                usePB = False
                
            else:
                add_number_2_array(num , counter , userEntrylenDivision)
        
            counter -= 1

        userEntrylenDivision -= 1
        userEntry = userEntry[2:]
        
    for i in range(int(len(userEntry) /3)):
        tempNum = userEntry[0:3]
        userEntry = userEntry[3:]
        counter = 2
        
        for itemA in tempNum:
            
            if counter == 1 and itemA == "1":
                usePB = True
                
            elif usePB:
                number_to_array_4_planeB(itemA, userEntrylenDivision)
                usePB = False
                
            else:
                add_number_2_array(itemA , counter , userEntrylenDivision)
            
            counter -= 1
        userEntrylenDivision -= 1
        
for i in finalArray:
    result = result + " " + i
    
print(result)