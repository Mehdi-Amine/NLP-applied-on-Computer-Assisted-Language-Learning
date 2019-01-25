# _*_ coding: utf-8 _*_

import codecs

#Making the dictionary
#------------------------------

#Opening the featuresFile and reading it line by line
featuresFile = codecs.open("Features.txt")
featuresLines = [l.strip('\n') for l in featuresFile.readlines()]

#Doing the same for the file wordsFile
wordsFile = codecs.open("Lexicon.txt", "r", "utf-8")
lexiconWords = [l.strip('\n') for l in wordsFile.readlines()]

#Creating dictionary that will bind each word with its list of features
dictionary = {}
listOfFeatures = []

#Looping over the words in the Lexicon file
#Every word is used for key in the dictionary
#every list of features is related to a word
for l in range(0, len(lexiconWords)):
    words = featuresLines[l].split()
    key = lexiconWords[l]
    dictionary[key] = words


#Reading arbInput file for input
#------------------------------

arbInput = codecs.open("arbInput.txt", "r", "utf-8")
arbTxt = arbInput.read()
arbTxtList = arbTxt.split()
sentenceStructure = []
correct = 1

for i in range(0, len(arbTxtList)):
    featuresList = dictionary[arbTxtList[i]]
    sentenceStructure.append(featuresList[0])

#DAMIR ISM NAAT
#------------------------------
if sentenceStructure[0] == "Damir" and sentenceStructure[1] == "Ism" and sentenceStructure[2] == "Naat":
    damirFeatures = dictionary[arbTxtList[0]]
    ismFeatures = dictionary[arbTxtList[1]]
    naatFeatures = dictionary[arbTxtList[2]]

#Checking gender AND number agreement violation btw Damir & Ism
    if damirFeatures[1] != ismFeatures[1] and damirFeatures[2] != ismFeatures[2]:
        if damirFeatures[2] == "Both":
            if damirFeatures[1] == "Pl&D" and ismFeatures[1] != "Du":
                if damirFeatures[1] == "Pl&D" and ismFeatures[1] != "Pl":
                    correct = 0
                    print "\nYou made a mistake in the number agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])
            elif damirFeatures[1] != "Pl&D":
                print "\nYou made a mistake in the gender and number agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])
        else:
            correct = 0
            print "You made a mistake in the gender and number agreement between %s and %s" %(arbTxtList[0], arbTxtList[1])

#Checking gender OR number agreement violation btw Damir & Ism
    elif damirFeatures[1] != ismFeatures[1] or damirFeatures[2] != ismFeatures[2]:
        if damirFeatures[1] != ismFeatures[1]:
            if damirFeatures[1] != "Pl&D" and ismFeatures[1] != "Du":
                if damirFeatures[1] == "Pl&D" and ismFeatures[1] != "Pl":
                    correct = 0
                    print "\nYou made a mistake in the number agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])
        elif damirFeatures[2] != ismFeatures[2]:
            if damirFeatures[2] != "Both":
                if damirFeatures[1] != "Pl&D":
                    correct = 0
                    print "\nYou made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])

#Checking gender and number agreement btw Ism and Naat
#For Animate Ism
    if ismFeatures[4] == "A":
        if ismFeatures[1] != naatFeatures[1] and ismFeatures[2] != naatFeatures[2]:
            correct = 0
            print "\nYou made a mistake in the gender and number agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
        elif ismFeatures[1] != naatFeatures[1] or ismFeatures[2] != naatFeatures[2]:
            if ismFeatures[1] != naatFeatures[1]:
                correct = 0
                print "\nYou made a mistake in the number agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
            elif ismFeatures[2] != naatFeatures[2]:
                correct = 0
                print "\nYou made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
#For Inanimate Ism
    if ismFeatures[4] == "IA":
        if ismFeatures[1] == "Sg" and naatFeatures[1] != "Sg":
            if ismFeatures[2] != naatFeatures[2]:
                correct = 0
                print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])

        if ismFeatures[1] == "Du" and naatFeatures[1] != "Du":
            if ismFeatures[2] != naatFeatures[2]:
                correct = 0
                print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])

        if ismFeatures[1] == "Pl" and naatFeatures[1] != "Sg":
            if ismFeatures[2] == naatFeatures[2]:
                correct = 0
                print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[1], arbTxtList[2])

        if ismFeatures[2] != naatFeatures[2]:
            if ismFeatures[1] != "Pl":
                print "\nYou made a mistake in the number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[1], arbTxtList[2])

#ISM NAAT
#------------------------------

if sentenceStructure[0] == "Ism" and sentenceStructure[1] == "Naat":
    ismFeatures = dictionary[arbTxtList[0]]
    naatFeatures = dictionary[arbTxtList[1]]

#Checking gender and number agreement btw Ism and Naat
#For Animate Ism
    if ismFeatures[4] == "A":
        if ismFeatures[1] != naatFeatures[1] and ismFeatures[2] != naatFeatures[2]:
            correct = 0
            print "\nYou made a mistake in the gender and number agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])
        elif ismFeatures[1] != naatFeatures[1] or ismFeatures[2] != naatFeatures[2]:
            if ismFeatures[1] != naatFeatures[1]:
                correct = 0
                print "\nYou made a mistake in the number agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])
            elif ismFeatures[2] != naatFeatures[2]:
                correct = 0
                print "\nYou made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])
#For Inanimate Ism
    if ismFeatures[4] == "IA":
        if ismFeatures[1] == "Sg" and naatFeatures[1] != "Sg":
            if ismFeatures[2] != naatFeatures[2]:
                correct = 0
                print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[0], arbTxtList[1])
        
        if ismFeatures[1] == "Du" and naatFeatures[1] != "Du":
            if ismFeatures[2] != naatFeatures[2]:
                correct = 0
                print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[0], arbTxtList[1])
    
        if ismFeatures[1] == "Pl" and naatFeatures[1] != "Sg":
            if ismFeatures[2] == naatFeatures[2]:
                correct = 0
                print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[0], arbTxtList[1])
                print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[0], arbTxtList[1])

        if ismFeatures[2] != naatFeatures[2]:
            if ismFeatures[1] != "Pl":
                correct = 0
                print "\nYou made a mistake in the number agreement between %s and %s\n" % (arbTxtList[0], arbTxtList[1])
                print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[0], arbTxtList[1])


#Joumla Fialia
#------------------------------
#------------------------------

#Fial Ism
#------------------------------

if sentenceStructure[0] == "Fial" and sentenceStructure[1] == "Ism":
    fialFeatures = dictionary[arbTxtList[0]]
    ismFeatures = dictionary[arbTxtList[1]]

    #Case it's a Fial followed by Ism
    #Check if there is only Fial and Ism
    if len(sentenceStructure) == 3:
        #Case where the phrase contains a Fial an Ism and something else


#Fial Ism Ism
#------------------------------
        if sentenceStructure[2] == "Ism":
            ism2Features = dictionary[arbTxtList[2]]

            #Checking for gender and number agreement between Fial and Ism
            #Checking if the first Ism is Det or NDet
            
            if ismFeatures[3] == "Det":
                if fialFeatures[1] != "Sg" and fialFeatures[2] != ismFeatures[2]:
                    correct = 0
                    print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[0], arbTxtList[1])
                elif fialFeatures[1] != "Sg" and fialFeatures[2] == ismFeatures[2]:
                    correct = 0
                    print "\nYou made a mistake in the number agreement between %s and %s\n" % (arbTxtList[0], arbTxtList[1])
                elif fialFeatures[1] == "Sg" and fialFeatures[2] != ismFeatures[2]:
                    correct = 0
                    print "\nYou made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])
        #In the case of the Ism being NDet no agreement with the verb has to be checked

#Fial Ism Naat
#------------------------------
        if sentenceStructure[2] == "Naat":
            naatFeatures = dictionary[arbTxtList[2]]
            #For Animate Ism
            if ismFeatures[4] == "A":
                if ismFeatures[1] != naatFeatures[1] and ismFeatures[2] != naatFeatures[2]:
                    correct = 0
                    print "\nYou made a mistake in the gender and number agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
                elif ismFeatures[1] != naatFeatures[1] or ismFeatures[2] != naatFeatures[2]:
                    if ismFeatures[1] != naatFeatures[1]:
                        correct = 0
                        print "\nYou made a mistake in the number agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
                    elif ismFeatures[2] != naatFeatures[2]:
                        correct = 0
                        print "\nYou made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
            #For Inanimate Ism
            if ismFeatures[4] == "IA":
                if ismFeatures[1] == "Sg" and naatFeatures[1] != "Sg":
                    if ismFeatures[2] != naatFeatures[2]:
                        correct = 0
                        print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                    
                    if ismFeatures[1] == "Du" and naatFeatures[1] != "Du":
                        if ismFeatures[2] != naatFeatures[2]:
                            correct = 0
                            print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                
                    if ismFeatures[1] == "Pl" and naatFeatures[1] != "Sg":
                        if ismFeatures[2] == naatFeatures[2]:
                            correct = 0
                            print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                            print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[1], arbTxtList[2])

                if ismFeatures[2] != naatFeatures[2]:
                    if ismFeatures[1] != "Pl":
                        correct = 0
                        print "\nYou made a mistake in the number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                        print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[1], arbTxtList[2])



#Fial Ism Naat Ism
#------------------------------

    if len(sentenceStructure) == 4:

        if sentenceStructure[2] == "Naat" and sentenceStructure[3] == "Ism":
            
           
            if ismFeatures[3] == "Det":
                if fialFeatures[1] != "Sg" and fialFeatures[2] != ismFeatures[2]:
                    correct = 0
                    print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[0], arbTxtList[1])
                elif fialFeatures[1] != "Sg" and fialFeatures[2] == ismFeatures[2]:
                    correct = 0
                    print "\nYou made a mistake in the number agreement between %s and %s\n" % (arbTxtList[0], arbTxtList[1])
                elif fialFeatures[1] == "Sg" and fialFeatures[2] != ismFeatures[2]:
                    correct = 0
                    print "\nYou made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[0], arbTxtList[1])
            #In the case of the Ism being NDet no agreement with the verb has to be checked
            

            if sentenceStructure[2] == "Naat" and sentenceStructure[3] == "NDet":
                naatFeatures = dictionary[arbTxtList[2]]
                #For Animate Ism
                if ismFeatures[4] == "A":
                    if ismFeatures[1] != naatFeatures[1] and ismFeatures[2] != naatFeatures[2]:
                        correct = 0
                        print "\nYou made a mistake in the gender and number agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
                    elif ismFeatures[1] != naatFeatures[1] or ismFeatures[2] != naatFeatures[2]:
                        if ismFeatures[1] != naatFeatures[1]:
                            correct = 0
                            print "\nYou made a mistake in the number agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
                        elif ismFeatures[2] != naatFeatures[2]:
                            correct = 0
                            print "\nYou made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
                #For Inanimate Ism
                if ismFeatures[4] == "IA":
                    if ismFeatures[1] == "Sg" and naatFeatures[1] != "Sg":
                        if ismFeatures[2] != naatFeatures[2]:
                            correct = 0
                            print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                            
                            if ismFeatures[1] == "Du" and naatFeatures[1] != "Du":
                                if ismFeatures[2] != naatFeatures[2]:
                                    correct = 0
                                    print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                    
                        if ismFeatures[1] == "Pl" and naatFeatures[1] != "Sg":
                            if ismFeatures[2] == naatFeatures[2]:
                                correct = 0
                                print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                                print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[1], arbTxtList[2])
                        
                        if ismFeatures[2] != naatFeatures[2]:
                            if ismFeatures[1] != "Pl":
                                correct = 0
                                print "\nYou made a mistake in the number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                                print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[1], arbTxtList[2])


#Fial Ism Naat Ism Naat
#------------------------------
    if len(sentenceStructure) == 5:
        ismFeatures2 = dictionary[arbTxtList[3]]
        naatFeatures2 = dictionary[arbTxtList[4]]
        
        if sentenceStructure[2] == "Naat" and sentenceStructure[3] == "Ism" and sentenceStructure[4] == "Naat":

            if sentenceStructure[2] == "Naat" and sentenceStructure[3] == "NDet":
                
                naatFeatures = dictionary[arbTxtList[2]]
                #For Animate Ism
                if ismFeatures[4] == "A":
                    if ismFeatures[1] != naatFeatures[1] and ismFeatures[2] != naatFeatures[2]:
                        correct = 0
                        print "\nYou made a mistake in the gender and number agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
                    elif ismFeatures[1] != naatFeatures[1] or ismFeatures[2] != naatFeatures[2]:
                        if ismFeatures[1] != naatFeatures[1]:
                            correct = 0
                            print "\nYou made a mistake in the number agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
                        elif ismFeatures[2] != naatFeatures[2]:
                            correct = 0
                            print "\nYou made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[1], arbTxtList[2])
                #For Inanimate Ism
                if ismFeatures[4] == "IA":
                    if ismFeatures[1] == "Sg" and naatFeatures[1] != "Sg":
                        if ismFeatures[2] != naatFeatures[2]:
                            correct = 0
                            print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
            
                    if ismFeatures[1] == "Du" and naatFeatures[1] != "Du":
                        if ismFeatures[2] != naatFeatures[2]:
                            correct = 0
                            print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                        
                    if ismFeatures[1] == "Pl" and naatFeatures[1] != "Sg":
                        if ismFeatures[2] == naatFeatures[2]:
                            correct = 0
                            print "\nYou made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                            print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[1], arbTxtList[2])
                        
                        if ismFeatures[2] != naatFeatures[2]:
                            if ismFeatures[1] != "Pl":
                                correct = 0
                                print "\nYou made a mistake in the number agreement between %s and %s\n" % (arbTxtList[1], arbTxtList[2])
                                print "Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[1], arbTxtList[2])

####
#Checking gender and number agreement btw Ism and Naat
#For Animate Ism
            if ismFeatures2[4] == "A":
                
                if ismFeatures2[1] != naatFeatures2[1] and ismFeatures2[2] != naatFeatures2[2]:
                    correct = 0
                    print "\n1You made a mistake in the gender and number agreement between %s and %s\n" %(arbTxtList[3], arbTxtList[4])
                elif ismFeatures2[1] != naatFeatures2[1] or ismFeatures2[2] != naatFeatures2[2]:
                    if ismFeatures2[1] != naatFeatures2[1]:
                        correct = 0
                        print "\n2You made a mistake in the number agreement between %s and %s\n" %(arbTxtList[3], arbTxtList[4])
                    elif ismFeatures2[2] != naatFeatures2[2]:
                        correct = 0
                        print "\n3You made a mistake in the gender agreement between %s and %s\n" %(arbTxtList[3], arbTxtList[4])
            #For Inanimate Ism
            if ismFeatures2[4] == "IA":

                if ismFeatures2[1] == "Sg" and naatFeatures2[1] != "Sg":
                    
                    if ismFeatures2[2] != naatFeatures2[2]:
                        
                        correct = 0
                        print "\n4You made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[3], arbTxtList[4])
                    
                if ismFeatures2[1] == "Du" and naatFeatures2[1] != "Du":
                    
                    if ismFeatures2[2] != naatFeatures2[2]:
                        correct = 0
                        print "\n5You made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[3], arbTxtList[4])
            
                if ismFeatures2[1] == "Pl" and naatFeatures2[1] != "Sg":
                    
                    if ismFeatures2[2] == naatFeatures2[2]:
                        correct = 0
                        print "\n6You made a mistake in the gender and number agreement between %s and %s\n" % (arbTxtList[3], arbTxtList[4])
                        print "7Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[3], arbTxtList[4])

                if ismFeatures2[2] != naatFeatures2[2]:
                    
                    if ismFeatures2[1] != "Pl":
                        correct = 0
                        print "\n8You made a mistake in the number agreement between %s and %s\n" % (arbTxtList[3], arbTxtList[4])
                        print "9Remember: %s is inanimate so %s should be singular female\n" % (arbTxtList[3], arbTxtList[4])




#If input is correct
if correct == 1:
    print "\nNo errors detected\n"




