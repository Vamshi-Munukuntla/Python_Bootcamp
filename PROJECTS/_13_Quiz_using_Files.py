import random
import os

# Step 6 - Implement logic to delete all .txt files from current directory
#           except country_data.txt
for file_name in os.listdir():
    if file_name.endswith('.txt') and not file_name.startswith('country_data'):
        os.unlink(file_name)

# Step 1 - Prompt for question and student numbers
# TODO 1.1 - Ask from user the number of questions
#            and the number of students in class

question_count = int(input('Total Number of Questions: '))
student_count = int(input('Total number of students in class: '))

# Step 2 - Parse country data text file in a Dictionary
# TODO 2.1 - Create empty countries dictionary
countries = {}
# TODO 2.2 - Open country_data.txt file
# TODO 2.3 - Parse data in countries dictionary
with open('country_data.txt', encoding="utf8") as country_info:
    country_info.readline()
    for country in country_info:
        info_list = country.strip().split(';')
        name, capital = info_list[1:3]
        countries[name] = capital

# Step 3 - Create Question Files and randomize the questions
for quiz_num in range(student_count):
    # Create quiz files
    with open(f'questions{quiz_num+1}.txt', mode='w') as quiz_file:
        # TODO 3.2 - Write header for the quiz in questions text files
        quiz_file.write('Name:\n\nDate:\n\n')
        quiz_file.write(f"{' ' * 20} Country Capitals Quiz (Form {quiz_num+1})")
        quiz_file.write('\n\n')
        # TODO 3.3 - Shuffle the order of countries based on random module
        country_list = list(countries.keys())
        random.shuffle(country_list)
        # TODO 3.4 - Loop Through number of questions and make a question for each
        for question_num in range(question_count):
            # Step 4 - Create multiple options for answers and answer text files
            # TODO 4.1 - Get correct and wrong answers
            correct_answer = countries[country_list[question_num]]
            wrong_answers = list(countries.values())
            del wrong_answers[wrong_answers.index(correct_answer)]
            # TODO 4.2 - Generate answer options
            wrong_answers = random.sample(wrong_answers, 3)
            answer_options = wrong_answers + [correct_answer]
            # TODO 4.3 - Randomize the answer options
            random.shuffle(answer_options)
            # Step 5 - Write content to questions and answers text files
            # TODO 5.1 - Write questions and answer options to questions text files
            quiz_file.write(f'{question_num+1}. What is the capital city of {country_list[question_num]}? \n')
            for i in range(4):
                quiz_file.write(f"{' '*5} {'ABCD'[i]}.{answer_options[i]}\n")
            quiz_file.write('\n')
            # TODO 5.2 - Write correct answers to answers text files
            with open(f'answers{quiz_num+1}.txt', "a") as answer_file:
                answer_file.write(f"{question_num+1}.{'ABCD'[answer_options.index(correct_answer)]}\n")


