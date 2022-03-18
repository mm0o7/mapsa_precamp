class Csv():
    
    
    def __init__(self, path, seprator, header = True) -> dict:
        self.header = header
        self.path = path
        self.seprator = seprator
        
        
    def get_data(self):
        with open(self.path, 'r', encoding='utf8') as f:
            if self.header:
                header_ = f.readline()
            else:
                header_ = []
            answers = f.readlines()
            return header_, answers
        
        
    def dict_reader(self):
        csv_dict = dict()
        if not self.seprator:
            raise Exception("no seprator have given")
        headers, answers = self.get_data()
        headers = headers.strip('\n')
        headers_list = headers.split(self.seprator)
        ans = []
        for i in range(6):
            parm = []
            for answer in answers:
                answer = answer.strip('\n')
                answer_list = answer.split(self.seprator)
                parm.append(answer_list[i])
            ans.append(parm)
        answer_adder = zip(headers_list, ans)
        csv_dict.update(answer_adder)
        return csv_dict    
            

def whitespace_deleter(list_name):
    listed_name = []
    for _ in list(list_name):
        listed_name.append(_.replace(" ",""))
    return listed_name 


def str_counter(name, list_name):
    counter = 0
    for _ in list_name:
        if name == _:
            counter += 1
    return counter        

            
def ready_up():
    true_answer = Csv("esm_famil_data.csv", ",")
    answer = true_answer.dict_reader()
    return answer


answers = ready_up()


participants = []
all_answers = []
def add_participant(participant, answers):
    participants.append(participant)
    all_answers.append(list(answers.values()))
    
    
def calculate_all():
    score = [0 for i in range(len(participants))]
    scores = {}
    for i in range(6):
        temp = []
        for answer in all_answers:
            temp.append(answer[i].replace(" ",""))
        if "" not in temp:
            complete = True
        else:
            complete = False
        ct = 0    
        for _ in temp:
            if _ in whitespace_deleter(list(answers.values())[i]) and _ != "":
                if str_counter(_, temp) == 1:
                    if complete:
                        score[ct] += 10
                    else:
                        score[ct] += 15
                else:
                    if complete:
                        score[ct] += 5
                    else:
                        score[ct] += 10                    
            ct += 1
    scores.update(zip(participants, score))
    print(scores)
