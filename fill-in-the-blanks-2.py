# A list of blanks to be passed in to the play game function.
numbers  = ["___1___", "___2___", "___3___", "___4___"]

# The following are quizzes in 3 different levels to pass in to the play_game function.
easy_quiz = '''Paris is the capital city of ___1___ and also fashion. All roads lead to ___2___ , which is the capital of Italy. It may still
surprise some people that the capital city of The USA is not New York City but ___3___ . Finally, ___4___ is the capital of the largest country in
the world.'''
answers_easy = ['France', 'Rome', 'Washington DC', 'Moscow']

medium_quiz = '''The capital of Australia is ___1___ on the contrary to the common guess Sydney. The capital city of tango dance and also Argentina
is ___2___. ___3___ is the capital city of Vietnam. ___4___ is the capital of the second most crowded country country in the world.'''
answers_medium = ['Canberra', 'Buones Aires', 'Ottawa', 'New Delhi']

hard_quiz = '''The capital of Morocco is ___1___. The capital city of Fiji is ___2___. ___3___ is the capital city of Bangladesh. ___4___ is the capital of Jamaica.'''
answers_hard = ['Rabat', 'Suva', 'Dhaka', 'Kingston']

print "Capitals of the World\nGame on!"

def get_quiz_data(level_chosen):
    """
    Assigns the data of the chosen quiz and its answers
    according to the raw input (choice of the player).
    """
    is_answered_correctly = True
    if level_chosen == "easy":
        quiz = easy_quiz
        answers = answers_easy
    elif level_chosen == "medium":
        quiz = medium_quiz
        answers = answers_medium
    elif level_chosen == "hard":
        quiz = hard_quiz
        answers = answers_hard
    else:
        print "PLEASE CHOOSE A VALID SELECTION."
        is_answered_correctly = False
        quiz, answers,level_chosen = get_quiz_data(level_chosen)
    if is_answered_correctly == True:
        print "You have chosen ", level_chosen, "\nYou will get 5 guesses per problem."
        print quiz

def level_select():
    """
    player selects level.
    """
    levels = ['easy', 'medium', 'hard']
    level_chosen = raw_input("Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard.\nPlease type your anwer here: ")
    quiz,answers = get_quiz_data(level_chosen)
    return quiz, answers, level_chosen


def return_if_blank_has_number(blank, numbers):
    """
    Checks if a number in numbers is a substring of the blank passed in.
    """
    for number in numbers:
        if number in blank:
            return number
    return None

def play_game():
    """
    # Plays the quiz.
    A player is prompted to replace numbers in blanks, which appear in numbers with their own answers.
    """
    quiz, answers,level_chosen = level_select()
    for blank in quiz.split():
        replacement = return_if_blank_has_number(blank, numbers)
        if replacement != None:
            current_number_of_attempts = 0 #refers to the current number of attempts
            total_attempts = 5
            while (current_number_of_attempts<total_attempts): #while the the current attempt is less than total
                user_input = raw_input("NEXT QUESTION:\n What should be substituted in for" + replacement + ". Type your answer here (Please capitalize your answer): ")
                if user_input in answers:
                    quiz = quiz.replace(replacement, user_input) # replaces current placeholder with the user input
                    print quiz # prints quiz for each question with user input added.
                    break
                else:
                    current_number_of_attempts += 1 #moves forward the next attempt
                    print "--WRONG!-- Let's try again. Attempts left:", total_attempts-i # total_attempts-i = for the countdown
            if i == total_attempts: # refers there is no attempt left
                print "--No attempts left. Please answer the next question--"
    print "*** CONGRATULATIONS! YOU HAVE COMPLETED THE QUIZ! ***"

play_game()
