'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# Problem: return total amount of times "th" appears in a word
test = "thhtththth"
# total : 4
def count_th(word, total = 0):
    # We need a counter to track occurences
    # split string to arr
    word = list(word)
    # concat word[0] + word[1]
    # if combo  = "th"

    if len(word) < 2:
        return total
    elif word[0] + word[1] == "th":
        # increase total += 1
        total += 1
        # print(total)
        # remove first letter
        word.pop(0)
        # Run again
        return count_th(word, total)
    else:
        word.pop(0)
        return count_th(word,total)
    
    # return total
    # print(total)
count_th(test)