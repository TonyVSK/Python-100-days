class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list


#    def still_has_questions(self, list_height):
#        if list_height > 0:
#            return True
#        else:
#            return False

    def next_question(self):
        on = 'true'
        counter = 0
        list_height = len(self.question_list)
        while on == 'true':
            current_question = self.question_list[self.question_number]
            self.question_number+=1
            user = input(f'Q. {self.question_number}: {current_question.text} (True/False): ').lower()
            if (user == 'true' and current_question.answer == 'True') or (user == 'false' and current_question.answer == 'False'):
                on = 'true'
                counter +=1
                list_height -= 1
            else:
                print(f'Gamer over... you did {counter} points')
                on = 'false'