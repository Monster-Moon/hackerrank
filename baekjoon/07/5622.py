


num_dict = {2: ['A', 'B', 'C'], 
            3: ['D', 'E', 'F'],
            4: ['G', 'H', 'I'],
            5: ['J', 'K', 'L'],
            6: ['M', 'N', 'O'],
            7: ['P', 'Q', 'R', 'S'],
            8: ['T', 'U', 'V'],
            9: ['W', 'X', 'Y', 'Z']
            }

inp = input()
print(sum([i+1 for i, j in zip(num_dict.keys(), num_dict.values()) for a in inp if a in j]))



