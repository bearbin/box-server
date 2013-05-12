def ask(questionText, answerTypeAllowed = 0, allowedAnswers = None, acceptedAnswerText = "Answer accepted.", typeErrorText = "Your answer was of the wrong type.", badAnswerText = "Your answer was not one of the allowed answers.", genericErrorText = "An error occured.", defaultAnswer = None):
    """
    Ask a question on the command line.
    
    answerTypeAllowed : What type of answers to allow. Defaults to any type.
    questionText      : What question the user is asked. This is required.
    allowedAnswers    : What values are allowed. Defaults to any.
    acceptedAnswerText: What to say when the answer is accepted. `None` to supress printing.
    typeErrorText     : The text printed if the input was of the wrong type.
    badAnswerText     : What is printed when the answer is not one of the specified allowed ones.
    genericErrorText  : What happens when an error occurs.
    defaultAnswer     : If the user does not enter anything, what's the default answer. None to ignore.
    
    answerTypeAllowed Values:
    0 : Any type.
    1 : String
    2 : Integer
    3 : Float
    4 : Boolean 
    """

    # TODO: Simplify more.

    def badAnswer():
        print(badAnswerText)
        input("Press enter to continue. ")

    if answerTypeAllowed not in list(range(5)):
        print("There was an error with internal coding :(")
        print("Please tell the maintainer this error:")
        print("answerTypeAllowed out of bounds when ask_question function called.")
        print("answerTypeAllowed was "+str(answerTypeAllowed)+" when allowed values are 0-4.")
        return

    while 1:
        userInput = input(questionText + " ")
        if (not userInput) and (defaultAnswer):
            if acceptedAnswerText: print(acceptedAnswerText)
            return defaultAnswer
        if allowedAnswers is not None:		
            if answerTypeAllowed == 0:
                if userInput in allowedAnswers:
                    if acceptedAnswerText: print(acceptedAnswerText)
                    return userInput
                else:
                    badAnswer()
                    continue
            elif answerTypeAllowed == 1:
                if str(userInput) in allowedAnswers:
                    if acceptedAnswerText: print(acceptedAnswerText)
                    return str(userInput)
                else:
                    badAnswer()
                    continue
            elif answerTypeAllowed == 2:
                try:
                    int(userInput)
                except ValueError:
                    print(typeErrorText)
                    input("Press enter to continue. ")
                    continue
                if int(userInput) in allowedAnswers:
                    if acceptedAnswerText: print(acceptedAnswerText)
                    return int(userInput)
                else:
                    badAnswer()
                    continue
            elif answerTypeAllowed == 3:
                try:
                    float(userInput)
                except ValueError:
                    print(typeErrorText)
                    input("Press enter to continue. ")
                    continue
                if float(userInput) in allowedAnswers:
                    if acceptedAnswerText: print(acceptedAnswerText)
                    return float(userInput)
                else:
                    badAnswer()
                    continue
            elif answerTypeAllowed == 4:
                if str(userInput).lower() in ['y', 'n', 'yes', 'no', '0', '1', 'true', 'false']:
                    if str(userInput).lower() in ['y', 'yes', '1', 'true']:
                        if acceptedAnswerText: print(acceptedAnswerText)
                        return True
                    else:
                        if acceptedAnswerText: print(acceptedAnswerText)
                        return False
                else:
                    print(typeErrorText)
                    input("Press enter to continue. ")
                    continue
            else:
                print(genericErrorText)
                input("Press enter to continue. ")
                continue
        elif allowedAnswers is None:
            if answerTypeAllowed == 0:
                if acceptedAnswerText: print(acceptedAnswerText)
                return userInput
            elif answerTypeAllowed == 1:
                if acceptedAnswerText: print(acceptedAnswerText)
                return str(userInput)
            elif answerTypeAllowed == 2:
                try:
                    int(userInput)
                except ValueError:
                    print(typeErrorText)
                    input("Press enter to continue. ")
                    continue
                if acceptedAnswerText: print(acceptedAnswerText)
                return int(userInput)
            elif answerTypeAllowed == 3:
                try:
                    float(userInput)
                except ValueError:
                    print(typeErrorText)
                    input("Press enter to continue. ")
                    continue
                if acceptedAnswerText: print(acceptedAnswerText)
                return float(userInput)
            elif answerTypeAllowed == 4:
                if str(userInput).lower() in ['y', 'n', 'yes', 'no', '0', '1', 'true', 'false']:
                    if str(userInput).lower() in ['y', 'yes', '1', 'true']:
                        if acceptedAnswerText: print(acceptedAnswerText)
                        return True
                    else:
                        if acceptedAnswerText: print(acceptedAnswerText)
                        return False
                else:
                    print(typeErrorText)
                    input("Press enter to continue. ")
                    continue
            else:
                print(genericErrorText)
                input("Press enter to continue. ")
                continue
        else:
            print(genericErrorText)
            input("Press enter to continue. ")
            continue

if __name__ == "__main__":
    print("askquestion.py Version 1.0")
    result = ask("Do you wish to see some demos of askquestion.py (Y/n):", answerTypeAllowed = 4, allowedAnswers = None, acceptedAnswerText = None, defaultAnswer = True)
    if result:
        print("You just saw one! askquestion.py supports many different types of questions.")
        while 1:
            result = ask("""(1) Anything
(2) String (basically above, just always returns as string)
(3) Integer
(4) Float
(5) Boolean
Type the corresponding number to try one or zero to cancel (0-5):""", answerTypeAllowed = 2, allowedAnswers = list(range(0, 6)), acceptedAnswerText = None)
            if result == 0:
                break
            elif result == 1:
                result = ask("Enter anything:", answerTypeAllowed = 0, acceptedAnswerText = None)
                print("You entered "+str(result)+"!")
            elif result == 2:
                result = ask("Enter 'foo', 'bar' or 'derp':", answerTypeAllowed = 1, allowedAnswers = ["foo", "bar", "derp"], acceptedAnswerText = None)
                print("You entered "+result+"!")
            elif result == 3:
                result = ask("Enter a number from one to ten (1-10):", answerTypeAllowed = 2, allowedAnswers = list(range(10)),  acceptedAnswerText = None)
                print("You entered "+str(result)+"!")
            elif result == 4:
                result = ask("Please enter a float:", answerTypeAllowed = 3, acceptedAnswerText = None)
                print("You entered "+str(result)+"!")
            else:
                result = ask("Please enter a boolean (Y/n):", answerTypeAllowed = 4, acceptedAnswerText = None, defaultAnswer = True)
                print("You entered "+str(result)+"!")
    print("Thanks for using askquestion.py! Exiting.")
