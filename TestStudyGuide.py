import time
def main():
    answer = ''
    question = 1
    total = 0
    answer = input("Which of the following serves as a six-year term of office?\nA. President of United States\nB. US Senator\nC. US Representative\nD. Supreme Court Justice\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("Which of the following serves a term of four years?\nA. President of United States\nB. United States Senator\nC. United States Representative\nD. Supreme Court Justice\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("Which of the following serves a term of two years?\nA. President of United States\nB. United States Senator\nC. United States Representative\nD. Supreme Court Justice\n")
    total, question = checkAnswer(answer, question, total)    
    answer = input("The term of a Supreme Court Justice is?\nA. Two years\nB. Six years\nC. Four years\nD. life\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("How many terms may the president serve?\nA. Two\nB. Six\nC. Four\nD. Eight\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("How many branches of government do we have on the national level?\nA. One\nB. Two\nC. Three\nD. Four\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("How many members serve in the legislative branch of government?\nA. 535\nB. 100\nC. 435\nD. 538\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("How many members are in the Senate?\nA. 535\nB. 100\nC. 435\nD. 538\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("How many members in the House of Representatives?\nA. 535\nB. 100\nC. 435\nD. 538\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("How many justices currently serve on the United States Supreme Court?\nA. Five\nB. Nine\nC. Eight\nD. Twelve\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("This state sends the most electors to the electoral college.\nA. Illinois\nB. California\nC. Texas\nD. New York\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("Which of the following branches of government enforces the law?\nA. Executive Branch\nB. Legislative Branch\nC. Judicial Branch\nD. The Olive Branch\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("When the Supreme Court declares a law unconstitutional, it is using its power of:\nA. Eminent Domain\nB. Habeas Corpus\nC .Judicial Review\nD. Veto\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("Which of the following is charged with negotiating treaties, with foreign nations?\nA. The President\nB. The Senate\nC. The House of Representatives\nD. The Supreme Court\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("This branch of government has the power to collect taxes, declare war, ratify treaties, and regulate interstate and foreign commerce.\nA. The Executive Branch\nB. The Legislative Branch\nC. The Judicial Branch\nD. The General Assembly\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("How many senators does a state send to Washington, DC?\nA. One\nB. Two\nC. Three\nD. Four\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("Which of the following is protected by the First Amendment?\nA. Libel\nB. Slander\nC. Political Speech\nD. All of the Above\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("This legislative body is based on population:\nA. Senate\nB. Supreme Court\nC. House of Representatives\nD. General Assembly\n")
    total, question = checkAnswer(answer, question, total)    
    answer = input("This legislative body is based on equal representation.\nA. Senate\nB. Supreme Court\nC. House of Representatives\nD. General Assembly\n")
    total, question = checkAnswer(answer, question, total)
    answer = input("A Constitutional Amendment:\nA. Can be repealed\nB. Changes the Constitution\nC. Requires approval by three fourths of the states\nD. All of the above\n")
    total, question = checkAnswer(answer, question, total)
    print(total, "/ 20")
def checkAnswer(answer, question, total):
    num = 0
    result = 0
    while True:
        try:
            answer = answer.capitalize()
            if answer == 'A':num = 1
            elif answer == 'B': num = 2
            elif answer == 'C': num = 3
            elif answer == 'D': num = 4
            else: answer = input("Please type again as either A, B, C, or D\n")
        except: answer = input("Please type again as either A, B, C, or D\n")
        if num > 0: break
    if question == 1 and num == 2: result=1
    elif question == 2 and num == 1: result=1
    elif question == 3 and num == 3: result=1
    elif question == 4 and num == 4: result=1
    elif question == 5 and num == 1: result=1
    elif question == 6 and num == 3: result=1
    elif question == 7 and num == 1: result=1
    elif question == 8 and num == 2: result=1
    elif question == 9 and num == 3: result=1
    elif question == 10 and num == 2: result=1
    elif question == 11 and num == 2: result=1
    elif question == 12 and num == 1: result=1
    elif question == 13 and num == 3: result=1
    elif question == 14 and num == 1: result=1
    elif question == 15 and num == 2: result=1
    elif question == 16 and num == 2: result=1
    elif question == 17 and num == 3: result=1
    elif question == 18 and num == 3: result=1
    elif question == 19 and num == 1: result=1
    elif question == 20 and num == 4: result=1
    else: result=0
    if result == 1:
        print("Correct")
        total = total + 1
    elif result == 0: print("Incorrect")
    time.sleep(1)
    question = question + 1
    return total, question
if __name__ == '__main__':
    main()