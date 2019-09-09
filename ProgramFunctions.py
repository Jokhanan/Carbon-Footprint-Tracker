#--------------------------------------------------------------------------------------------------------
# Name: CFET Program Functions (ProgramFunctions.py)
# Purpose: Has all relevant stand-alone functions required for functionality of CFET
#
#
# Author: Nisarg Shah
# Created: 4-Jan-2018
# Updated: 18-Jan-2019
#--------------------------------------------------------------------------------------------------------
from TechnologyClass import TechnologyEvent
from TravelClass import TravelEvent
import glob

def signupCheck(username, password):
    '''
    Checks if username and password user wants to signup with are valid and the username how not previously been taken

    Parameters
    ----------
    username: str
        Username user wants to signup with
    password: str
        Password user wants to signup with

    Returns
    -------
    bool: True for signup success, False otherwise
    
    '''
    if len(username) == 0 or len(password) == 0:
        return False
    credFile = open("masterLoginCred.txt", "r+")
    credHolding = credFile.readlines()
    credFile.close()
    for i in range(len(credHolding)):#if username already exists returns false
        if i % 5 == 1 and credHolding[i][:-1] == username:
            return False
    return True

def login(username, password):

    '''
    Checks if inputed username and password are valid by cross referencing user login credential file.

    Parameters
    ----------
    username: str
        Username user wants to login with
    password: str
        Password user wants to login with

    Returns
    -------
    userFirstName: str
        First name of user
    userLastName: str
        Last name of user
    bool: True for login success, False otherwise
    
    '''

    dataFile = open("masterLoginCred.txt", "r+")
    credCheck = dataFile.readlines()
    dataFile.close()
    for i in range(len(credCheck)):#checks login credentials if they match it returns true
        if i % 5 == 1:
            if credCheck[i][:-1] == username and credCheck[i + 1][:-1] == password:
                   userFirstName = credCheck[i + 2][:-1]
                   userLastName = credCheck[i + 3][:-1]
                   return userFirstName, userLastName, True
    return False

def profileCreation(username, password, firstName, lastName, dob, location):
    '''
    Creates user account and user file using user info

    Parameters
    ----------
    username: str
        Username user wants to signup with
    password: str
        Password user wants to signup with]
    firstName: str
        First name of user
    lastName: str
        Last name of user
    dob: str
        Date of birth of user
    location: str
        Country of residence of user

    Returns
    -------
    None 
    '''
    #creates account in login credential file
    credFile = open("masterLoginCred.txt", "a")
    credFile.write("Next User: \n")
    credFile.write(username + "\n")
    credFile.write(password + "\n")
    credFile.write(firstName + "\n")
    credFile.write(lastName + "\n")
    credFile.close()

    #creates account file in directory
    newFile = open(firstName + lastName + ".txt","w+")
    newFile.write(firstName + "\n")
    newFile.write(lastName + "\n")
    newFile.write(dob + "\n")
    newFile.write(location + "\n")
    newFile.close()


def eventCreation(firstName, lastName, eventType, eventSubType, eventDate, eventTitle, eventAmount, eventDiscription):
    '''
    Creates an event object ased on user input and writes it to user file

    Parameters
    ----------
    firstName: str
        First name of user
    lastName: str
        Last name of user
    eventType: str
        Category/type of event
    eventSubType: str
        Subtype of event
    eventDate: str
        Date the event occured
    eventTitle: str
        The title of the event
    eventAmount: float
        The amount a given subtype was used
    eventDescription:str
        The description of the event
        
    Returns
    -------
    None
    '''
    
    if eventType == 'Technology':
        tempEvent = TechnologyEvent(eventDate, eventTitle, eventDiscription, eventAmount, eventSubType)
    elif eventType =='Travel':
        tempEvent = TravelEvent(eventDate, eventTitle, eventDiscription, eventAmount, eventSubType)
    #writes all event details to user file
    userFile = open(firstName + lastName + ".txt","a")
    userFile.write(eventType +'\n')
    userFile.write(eventSubType +'\n')
    userFile.write(eventTitle +'\n')
    userFile.write(eventDate +'\n')
    userFile.write(eventDiscription +'\n')
    userFile.write(str(eventAmount) +'\n')
    userFile.write(decimalLimiter(tempEvent.calculator()) +'\n')
    userFile.close()
    

def eventHistoryComplier(firstName, lastName):
    '''
    Creates event objects for all the events logged on user file

    Parameters
    ----------
    firstName: str
        First name of user
    lastName: str
        Last name of user

    Returns
    -------
    eventContainer: list
        List of all created event objects
    '''

    eventContainer= []
    userFile = open(firstName + lastName + ".txt","r")
    infoHold = userFile.readlines()
    userFile.close()
    for i in range(4):
        infoHold.pop(0)
        
    for i in range(len(infoHold)): #complies all evetns into a container
        if i%7 == 0:
            eventType = infoHold[i][:-1]
            if eventType == 'Technology':
                tempEvent = TechnologyEvent(infoHold[i + 3][:-1], infoHold[i + 2][:-1], infoHold[i + 4][:-1],
                                            infoHold[i + 5][:-1], infoHold[i + 1][:-1])
            elif eventType == 'Travel':
                tempEvent = TravelEvent(infoHold[i + 3][:-1], infoHold[i + 2][:-1], infoHold[i + 4][:-1],
                                            infoHold[i + 5][:-1], infoHold[i + 1][:-1])
            eventContainer.append(tempEvent)
    
    return eventContainer
    
def emissionsScoreGenerator(firstName, lastName):
    '''
    Calculates the users score for each event subtype

    Parameters
    ----------
    firstName: str
        First name of user
    lastName: str
        Last name of user

    Returns
    -------
    scores: list
        List holds total score and all subType event scores
        
    '''
    # score List layout: scores= [total, smartphone, tablet, computer,tv, transit, car, train, airplane]
    scores= [0, 0, 0, 0, 0, 0, 0, 0, 0]
    userFile = open(firstName + lastName + ".txt","r")
    infoHold = userFile.readlines()
    userFile.close()
    for i in range(4):
        infoHold.pop(0)
     
    for i in range(len(infoHold)): # complies all subevent scores
        if i%7 == 1:
            eventSubtype = infoHold[i][:-1]
            eventScore = float(decimalLimiter(float(infoHold[i+5][:-1])))
            if eventSubtype == 'Smartphone':
                scores[1] = scores[1] + eventScore
            elif eventSubtype == 'Tablet':
                scores[2] = scores[2] + eventScore
            elif eventSubtype == 'Computer':
                scores[3] = scores[3] + eventScore
            elif eventSubtype == 'Television':
                scores[4] = scores[4] + eventScore
            elif eventSubtype == 'Public Transit':
                scores[5] = scores[5] + eventScore
            elif eventSubtype == 'Car':
                scores[6] = scores[6] + eventScore
            elif eventSubtype == 'Train':
                scores[7] = scores[7] + eventScore
            elif eventSubtype == 'Airplane':
                scores[8] = scores[8] + eventScore
            scores[0] = scores[0] + eventScore

            eventTitle = infoHold[i+1][:-1]

    return scores

def leaderBoardScore(firstName, lastName):
    '''
    Complies all leaderboard scores along with a dictionary with the keys being scores and the values being user names

    Parameters
    ----------
    firstName: str
        First name of user
    lastName: str
        lastname of user
    
    Returns:
    --------
    topScores: list
        Up to top 10 lowest scores
    allPersonalScores: dict
        Dictionary of users and their scores
    userRank: int
        Rank of current user
    '''
    allPersonalScores = {}
    allScores= []
    allFiles = glob.glob('*.txt')#gets all text files in directory and puts them into a lsit

    #goes through each user file and complies total score for the user
    for i in range(len(allFiles)):
        runningTotal = 0
        if allFiles[i] == 'masterLoginCred.txt':# if the file is the login file the loop passes for the iteration
            pass
        else:
            tempFile = open(allFiles[i], 'r')
            tempContent = tempFile.readlines()
            tempFile.close()

            personInfo = tempContent[0][:-1] + " " + tempContent[1][:-1] + " - " + tempContent[3][:-1]
            for j in range(4):# removes the users personal info 
                tempContent.pop(0)
            for k in range(len(tempContent)):
                if k%7 == 6:#gets users total score
                    runningTotal = runningTotal + float(tempContent[k][:-1])
            allScores.append(runningTotal)#puts the final score into a list of all other scores
            allPersonalScores[str(runningTotal)] = personInfo # adds a dictionary entery with the score and the user the score belongs to
            if allFiles[i] == firstName + lastName + '.txt':# if the file is the current Users, saves the current users score 
                currentUserScore = runningTotal

    #Insertion Sort all scores from lowest to greatest   
    for i in range(len(allScores)):
        shiftingValue = allScores[i]
        indexValue = i - 1
        while (indexValue >= 0) and (allScores[indexValue] > shiftingValue):
            allScores[indexValue + 1] = allScores[indexValue]
            indexValue = indexValue  - 1
        allScores[indexValue + 1] = shiftingValue
        
    #Binary Search for current user score
    upperBound = len(allScores) - 1
    lowerBound = 0
    while lowerBound <=  upperBound:
        midPoint = (lowerBound + upperBound)//2
        if allScores[midPoint] < currentUserScore:
            lowerBound = midPoint + 1
        elif allScores[midPoint] > currentUserScore:
            lowerBound = midPoint - 1
        else:
            userRank = midPoint + 1
            break   
    topScores = allScores[0:10] #takes top 10 scores from allScores
    return topScores, allPersonalScores, userRank

def decimalLimiter(num):
    '''
    Limits any float nuber to 3 decimal places or lower

    Parameters
    ----------
    num: float
        Number that needs to be limited

    Returns
    -------
    num: str
        Returns float with 3 deicmal places as a string
    '''
    num = str(num)
    for i in range(len(num)):
        if num[i] == '.':# after the deicmal if the length is less than 3 return original number, if more than 4, length of number is limited to 3 decimals
            if len(num)- i - 4 < 0:
                return num
            else:
                num = num[0:i+4]
                return num
    
    
    
