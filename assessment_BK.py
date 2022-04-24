import string

def react(polymer_string):
    """
    There is a processing plant that needs to be optimized, and we need your help.

    The processing plant creates chemical polymers made of 26 monomers, and 26 reactive monomers. When a monomer, and it's corresponding reactive monomer touch, they will react, and disappear from the chain.

    Each monomer has a symbol corresponding to a lower case letter in the alphabet ie: `a-z`.
    Each monomer's reactive cousin is given an upper case letter, ie: `A-Z`.

    In a chain, when a reactive pair, ie `Aa` or `aA` touch, they will disappear and the chain will re-attach. 

    This means that in a polymer chain like `AaefxxXXB`, it will react to form: `efB`. It forms this by the following process:
    1. `Aa` will react, creating `efaaAAB`
    2. `xX` will react, creating `efxXB`
    3. `xX` will react, creating `efB`
    4. `efB` is now stable and will no longer react. 

    Your task is to code an algorithm that prints out the stable and fully reacted polymer given any polymer chain input.

    To help you, here are some examples:

    1. `vRaKkNgeUYTt` will become `vRaNgeUY`
    2. `WySrKeqEzAYyYUQqYuIicrRClZGrjfdEvSxYcCQxcCTqpUu` will become `WySrKeqEzAYUYulZGrjfdEvSxYQxTqp`
    3. `mJYBPpluUqQrleJjgGUWwTtsywWdDuMmNOSsLlfXxOtTCcFfgXxZGgthHb` will become `mJYBlrleUsyuNOfOgZtb`

    Must return the string of reacted polymer.
    """
    # Get active pair combinations:
    lower_alphabet = list(string.ascii_lowercase)
    upper_alphabet = [x.upper() for x in lower_alphabet]
    active_pairs = list(i+j for i,j in zip(lower_alphabet,upper_alphabet))
    active_pairs.extend(list(i+j for i,j in zip(upper_alphabet,lower_alphabet)))

    # Get chemical string to list:
    polymer_list = list(polymer_string)

    # reaction (recursive):
    indices_to_remove = list()
    for i,j in enumerate(polymer_list):
        if i - 1 < 0:
            left_index = 0
        else:
            left_index = i - 1
        if i + 1 > len(polymer_list)-1:
            right_index = len(polymer_list)-1
        else:
            right_index = i + 1

        check_1 = polymer_list[left_index] + j                
        check_2 = j + polymer_list[right_index]

        if check_1 in active_pairs:
            indices_to_remove.append(left_index)
            indices_to_remove.append(i)
        if check_2 in active_pairs:
            indices_to_remove.append(right_index)
            indices_to_remove.append(i)
    
    polymer_string_reaction = ''.join([v for i,v in enumerate(polymer_list) if i not in list(set(indices_to_remove))])
    
    print(polymer_string,' ---> ',polymer_string_reaction)
    if polymer_string_reaction == polymer_string:
        print("Final state: {}".format(polymer_string_reaction))
        return polymer_string_reaction
    else:
        return(react(polymer_string=polymer_string_reaction))

print("***** Chemical Process Start *****")
print(react(polymer_string="vRaKkNgeUYTt"))
print("***** Chemical Process End *****")