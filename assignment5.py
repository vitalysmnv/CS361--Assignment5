# -*- coding: utf-8 -*-

#open document 
print("Welcome to your personal Goal Tracker! Here you may update, create, and track your goals. \n")
mvp_doc = open(r'D:\mvp_doc.txt','a+')


goal_statement = "Goal: \n"


with open(r'D:\mvp_doc.txt') as f:
    first_line = f.readline()
    second_line = f.readlines()


if(first_line == goal_statement):
    print(("Your goal is currently: {}").format(second_line[0]))
    print("Would you like to restart with a new goal? (YES or NO)")
    ans1 = input()
    if (ans1.upper() == "YES"):
        print("Are you sure you would like to restart? (YES or NO) ")
        ans1 = input()

if (first_line != goal_statement or ans1.upper() == "YES"):
    mvp_doc.truncate(0)
    print("What is your goal: ")
    goal_count = input()
    mvp_doc.write("{}" .format(goal_statement))
    mvp_doc.write("{} \n".format(goal_count))


#take in the values for date and progress
print("Today's Date in (mm/dd/yyyy) format: ")
date = input()
print("Progress: ")
word_count = input()


#write the word count to doc
mvp_doc.write("\nOn {} your progress toward your goal was at {}.".format(date, word_count))
mvp_doc.write("\n")


#any notes for the update
print("Would you like to add any notes? (YES or NO)")
ans = input()


if ans.upper() == "YES":  
    print("Write your notes here: ")
    note = input()
    mvp_doc.write(("{} \n ").format(note))
    

#close doc
mvp_doc.close()


"""

HOW MY MVP DEMONSTRATES ALL 8 CHS'S:
1. The features are explicitly stated at the beginning of the program
2. None of the features are difficult; they are all extremely simple
3. The optional features I included (notes) are useable but not required for users
    they can be used to make the goal updates more or less complex
4. The features are always repeated so there will not be any unusual features (the 
familiar features are always there)
5. The user can restart their goals at any time; they can add new updates to their goals 
6. The path is simple and always the same
    First they are asked about the goal, asked for date and update, asked to add notes,
    and then they can run the program again
7. The goals are not restricted to any format (numeric, word-based, etc) so there are many
approaches that the user can follow
8. The user is asked to confirm a restart of their goals 


HOW MY MVP DEMONSTRATES THREE QUALITY ATTRIBUTES:
1. Usability
    The software stores data in a text file and is updated properly by 
    apending the new notes/updates to the text files
2. Adaptability
    The software allows updates to be tracked in numerical or alphanumerical format
3. Efficiency
    The software is fast and as soon as I open the text file
    
"""