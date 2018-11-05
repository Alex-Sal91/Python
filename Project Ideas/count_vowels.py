def count_vowels(str):
    count = 0
    for char in str:
        if char in "aeiouAEIOU":
            count += 1
    return count


a = count_vowels("Hello my name is Alex")

print("There are {} vowels in this string".format(a))