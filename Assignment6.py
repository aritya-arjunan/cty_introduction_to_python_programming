print('Welcome to the quiz that tests your Periodic Table knowledge!')
print('''

''')
def question(question_number, option1, option2, option3, option4, question, correct_answer):
    score = 0
    print()
    print("Question %s:" % question_number)
    print('%s' % question)
    print("a. %s" % option1)
    print("b. %s" % option2)
    print("c. %s" % option3)
    print("d. %s" % option4)
    answer = input("Answer:")
    if answer == correct_answer:
        if int(question_number) < 4:
            print("You are correct. You are now moving on to Question %s. Your score is 1" % (int(question_number) + 1))
        else:
            print("You are correct. Your score is 1")
        score = 1
    else:
        print("You are incorrect. You can have another attempt.")
        print()
        print("Question %s:" % question_number)
        print('%s' % question)
        print("a. %s" % option1)
        print("b. %s" % option2)
        print("c. %s" % option3)
        print("d. %s" % option4)
        answer = input("Answer:")
        if answer == correct_answer:
            if int(question_number) < 4:
                print("You are correct. You are now moving on to Question %s. Your score is 0.5" % (int(question_number) + 1))
            else:
                 print("You are correct. Your score is 0.5")
            score = 0.5
        else:
            print("You are incorrect. Your score is 0.")
    return score

total_score = question(str(1), 'Go', 'Zr', 'Th', 'Au', 'What is the elemental symbol of gold?', 'd')
total_score = total_score + question(str(2), 'The Boron Group', 'The Halogen Group', 'Alkali Metals', 'The Nitrogen Group', "Which group is Bromine in?", 'b')
total_score = total_score + question(str(3), '85', '78', '74', '82', 'What is the atomic number for lead?', 'd')
total_score = total_score + question(str(4), 'Hydrogen', 'Scandium', 'Nitrogen', 'Radium', "What is the lightest element?", 'a')
print('Your total score is %s.' % str(total_score))
