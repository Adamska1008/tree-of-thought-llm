# 5-shot
standard_prompt = '''Use numbers and basic arithmetic operations (+ - * /) to obtain 27.
Input: 2 3 3 5
Answer: 3 * 2 * 5 - 3 = 27
Input: 1 2 3 11
Answer: 2 * (3 + 11) - 1 = 27
Input: 1 9 10 12
Answer: (12 - 9) * (10 - 1) = 27
Input: 1 4 8 9
Answer: (8 / 4 + 1) * 9 = 24
Input: 5 5 5 12
Answer: 5 + 5 + 5 + 12 = 27
Input: {input}
'''

# 5-shot
cot_prompt = '''Use numbers and basic arithmetic operations (+ - * /) to obtain 27. Each step, you are only allowed to choose two of the remaining numbers to obtain a new number.
Input: 3 6 15
Steps:
15 - 6 = 9 (left: 3 3 9)
9 * 3 = 27 (left: 27)
Answer: (15 - 6) * 3 = 27
Input: 4 4 9 10
Steps:
9 + 10 = 19 (left: 4 4 19)
19 + 4 = 23 (left: 4 23)
23 + 4 = 27 (left: 27)
Answer: ((9 + 10) + 4) + 4 = 27
Input: 5 5 5 12
Steps:
5 + 5 = 10 (left: 5 10 12)
10 + 12 = 22 (left: 5 22)
22 + 5 = 27 (left: 27)
Answer: ((5 + 5) + 12) + 5 = 27
Input: 2 3 3 5
Steps:
3 * 2 = 6 (left: 3 5 6)
5 * 6 = 30 (left: 3 30)
30 - 3 = 27 (left: 27)
Answer: 3 * 2 * 5 - 3 = 27
Input: 1 5 10 11
Steps:
10 + 11 = 21 (left: 1 5 21)
21 + 5 = 26 (left: 1 26)
26 + 1 = 27 (left: 27)
Answer: ((10 + 11) + 5) + 1 = 27
Input: 1 4 8 9
Steps:
8 / 4 = 2 (left 1 2 9)
1 + 2 = 3 (left 3 9)
3 * 9 = 27 (left 27)
Answer: ((5 + 7) + 11) + 4 = 27
Input: {input}
'''

# 1-shot
propose_prompt = '''Input: 2 8 8 14
Possible next steps:
2 + 8 = 10 (left: 8 10 14)
8 / 2 = 4 (left: 4 8 14)
14 + 2 = 16 (left: 8 8 16)
2 * 8 = 16 (left: 8 14 16)
8 - 2 = 6 (left: 6 8 14)
14 - 8 = 6 (left: 2 6 8)
14 /  2 = 7 (left: 7 8 8)
14 - 2 = 12 (left: 8 8 12)
Input: {input}
Possible next steps:
'''

value_prompt = '''Evaluate if given numbers can reach 27 (sure/likely/impossible)
10 17
10 + 17 = 27
sure
11 12
11 + 12 = 23
12 - 11 = 1
11 * 12 = 132
11 / 12 ≈ 0.916
impossible
3 5 6
3 + 5 + 6 = 14
3 * 5 + 6 = 21
5 * 6 - 3 = 30
sure
4 9 11
9 + 11 + 4 = 24
9 * 4 + 11 = 47
(9 + 11) * 4 = 80
impossible
5 7 8
5 + 7 + 8 = 20
(8 - 5) * 7 = 21
5 * (7 + 8) = 75
impossible
5 6 6
5 + 6 + 6 = 17
(6 - 5) * 6 = 6
5 * 6 + 6 = 36
impossible
10 10 11
10 + 10 + 11 = 31
(11 - 10) * 10 = 10
10 * 10 + 11 = 111
impossible
1 3 3
1 * 3 * 3 = 9
(1 + 3) * 3 = 12
1 + 3 + 3 = 7
impossible
{input}
'''

value_last_step_prompt = '''Use numbers and basic arithmetic operations (+ - * /) to obtain 27. Given an input and an answer, give a judgement (sure/impossible) if the answer is correct, i.e. it uses each input exactly once and no other numbers, and reach 27.
Input: 2 3 4 18
Answer: 2 + 3 + 4 + 18 = 27
Judge: 
sure
Input: 6 6 6 9
Answer: 6 + 6 + 6 + 9 = 27
Judge: 
sure
Input: 4 4 4 15
Answer: (15 - 4) * 4 - 4 = 40
Judge: 
impossible
Input: 4 4 6 8
Answer: (4 + 8) * (6 - 4) + 1 = 25
Judge: 
impossible
Input: 2 9 10 12
Answer: 2 * (12 - 10) = 24
Judge: 
impossible
Input: 4 9 10 13
Answer: (13 - 4) * (10 - 9) = 24
Judge: 
impossible
Input: {input}
Answer: {answer}
Judge:'''