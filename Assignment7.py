print('Welcome to the quiz that tests your Periodic Table knowledge!')
max_attempts = int(input('How many attempts do you want for your questions?'))
def question(question_number, option1, option2, option3, option4, question, correct_answer):
    points = 1
    current_attempt = 1
    while(current_attempt <= max_attempts):
        print()
        print("Question %s (attempt %s of %s):" % (question_number, current_attempt, max_attempts))
        print('%s' % question)
        print("a. %s" % option1)
        print("b. %s" % option2)
        print("c. %s" % option3)
        print("d. %s" % option4)
        answer = input("Answer:")
        if answer == correct_answer:
            if current_attempt > 1:
                points = 0.5
            if int(question_number) < 6:
                print("You are correct. You are now moving on to Question %s. Your points are " % (int(question_number) + 1) + str(points))
            else:
                print("You are correct. Your points are " + str(points))
            break
        else:
            points = 0
            print("You are incorrect. Your points are " + str(points))
            current_attempt += 1         
    return points

score = 0
score = question(str(1), 'Go', 'Zr', 'Th', 'Au', 'What is the elemental symbol of gold?', 'd')
score += question(str(2), 'The Boron Group', 'The Halogen Group', 'Alkali Metals', 'The Nitrogen Group', "Which group is Bromine in?", 'b')
score += question(str(3), '85', '78', '74', '82', 'What is the atomic number for lead?', 'd')
score += question(str(4), 'Hydrogen', 'Scandium', 'Nitrogen', 'Radium', "What is the lightest element?", 'a')
score += question(str(5), '77', '6', '9', '118', 'What is the atomic number for carbon?', 'b')
score += question(str(6), 'Alkali Metals', 'Alkaline Earth Metals', 'Lathanides', 'Actinides', 'Which group is Calcium in?', 'b')
print('Your total score is %s.' % str(score))

