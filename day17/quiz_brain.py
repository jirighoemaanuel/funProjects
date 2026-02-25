class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.next_question()

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"{current_question.text}?:")
        return answer

    next_question()
