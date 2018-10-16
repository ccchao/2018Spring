"""
File name: codecheck.py
Students: Junxiao Chen
Deadline: Thursday, Feb. 15th

Warm-up Project
Simulation of the board game Mastermind
"""

def random_code(random_times = 4, random_limit = 5):
    """ 
    :type random_times: int
    :type random_limit: int
    :rtype answer_code: list
    """
    answer_code = []
    for i in range(random_times):
        answer_code.append(random.randint(0, random_limit))
    return answer_code#[i for i in range(random_times)]

   
def code_check(guess_code,answer_code):
    """
    :type answer_code: list
    :type guess_code: list
    :rtype checked_list: list
    
    """
    
    #convert answer_code list to a dict for count each element.
    answer_dict = {}    
    for ele in answer_code:
        try:
            answer_dict[ele] += 1 
        except KeyError:
            answer_dict[ele] = 1
    
    #count how many guess code are right.
    for ele in guess_code:
        if ele in answer_dict:
            if answer_dict[ele] > 0:
                answer_dict[ele] -= 1
        
    contained_num = 0   
    left_num = 0
    for key in answer_dict:
        left_num += answer_dict[key]
    contained_num = 4 - left_num

    checked_list = []
    for i in range(contained_num):
        checked_list.append(6) 
    
    #match number
    for i in range(len(answer_code)):
        if answer_code[i] == guess_code[i]:
            checked_list.append(7) 
            checked_list.remove(6)
    
    checked_list.sort()
            
    return checked_list
 