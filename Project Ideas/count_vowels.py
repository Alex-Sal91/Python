def count_vowels():
    str = raw_input("Enter your favourite film: ")
    count = 0
    for char in str:
        if char in "aeiouAEIOU":
            count += 1
    return count



print("There are {} vowels in your movie title!".format(count_vowels()))

