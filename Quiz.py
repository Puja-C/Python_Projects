# ask user questions, and based on their answer print the score in the end

quiz = {
    "question 1" : {
        "question" : "What is the capital of Italy?",
        "answer" : "Rome"
    },
    "question 2" : {
        "question" : "Which is the largest planet of our solar system?",
        "answer" : "Jupiter"
    },
    "question 3" : {
        "question" : "What element does 'O' represent on the periodic table?",
        "answer" : "Oxygen"
    },
    "question 4" : {
        "question" : "True or False? Electrons are smaller than atoms.",
        "answer" : "True"
    },
    "question 5" : {
        "question" : "How many bones are in the human body?",
        "answer" : "206"
    },
}

score = 0

for key, value in quiz.items() :
    print(value['question'])
    answer = input("Enter your answer:")
    if answer.lower() == value['answer'].lower():
        print('Correct!')
        score += 1
        print('Your score is %d' % score)
    else :
        print('Incorrect!')
        print("The correct answer is " + value['answer'])

print("You have completed the quiz! Your final score is %d." % score)
