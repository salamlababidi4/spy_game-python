# Write a function that takes in a list of integers and returns True if it contains 007 in order.
# Example:
# spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(mylist):
    zero = 0
    for num in range(len(mylist)):
        if mylist[num] == 0:
            zero+=1
            if zero == 2:
                for sev in mylist[num:]:
                    if sev == 7:
                        print("007")
                        return True
    print("HARD LUCK:(")
    return False