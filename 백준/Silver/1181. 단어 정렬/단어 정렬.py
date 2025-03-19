alphabet_to_int_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

int_to_alphabet_dict = {v: k for k, v in alphabet_to_int_dict.items()}

num_test_case = int(input())
list_inputs_set = set()

for _ in range(num_test_case):
    now_input = input()
    now_input_decoded = 0
    for decimal, decode in enumerate(reversed(now_input)):
        now_input_decoded = now_input_decoded + alphabet_to_int_dict[decode] * 100**(decimal)
    list_inputs_set.add(now_input_decoded)

list_inputs = list(list_inputs_set)
list_inputs.sort()

for input_num in list_inputs:
    now_str = ""
    stred_now_int = str(input_num)
    if len(stred_now_int) % 2 ==1:
        stred_now_int = "0" + stred_now_int

    for i in range(len(stred_now_int) // 2):
        now_str += int_to_alphabet_dict[int(stred_now_int[2*i:2*i+2])]
            
    print(now_str)