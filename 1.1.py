# as shown in the examples of the assignment pdf, i am assuming that the input is a string with only alphabets.
# hence the input is assumed to be a single word.

#function to check if user wants to continue or not
def check_continue():
    print("Press ENTER if you wish to play another round")
    user_command = input("OR enter 'Quit' if you want to exit: ").lower()   #making quit case insensitive
    # validate user command
    if user_command not in ['quit', '']:
        print("Invalid command! Please press ENTER or enter 'Quit'.")
        check_continue()
    elif user_command == 'quit':
        return
    else:
        main()      #if user press enter then it again calls the main()
    
#to sort or reverse the substrings
def sort_or_reverse(n, s, sub_strings):
    new_substrings = []

    if n & len(s):      #if bitwise and is non zero
        # sub_strings in reverse order:
        print("Reversed the order of the sub strings:") 
        for i in range(len(sub_strings)-1, -1, -1):
            new_substrings.append(sub_strings[i])
    
    else:   #if bitwise and is zero
        # sub strings in lexicographic order:
        print("Sub strings in lexicographic order:")
        for sub in sorted(sub_strings):
            new_substrings.append(sub)
    print(new_substrings)   #print the new sub strings

# func to extract the substrings of length k
def extract_substrings(s, k):
    sub_strings = []
    for i in range(len(s) - k + 1):
        sub_strings.append(s[i:i+k])
    return sub_strings

# to count the number of set bits in binary n
def count_set_bits(n):
    return bin(n).count('1')


# basically the main function where all the processing starts and all the other functions are called
def process_string(n, s):
    # parity check
    if n & 1:
        # n is odd
        print("Your registration number is odd, hence your script will be poetically transformed!")
        vowels = 'aeiouAEIOU'   # Define vowels
        result = ''
        for char in s:
            if char.isalpha():  # Check if the character is an alphabet
                if char in vowels:
                    result += char.upper()  # Convert vowels to uppercase
                else:
                    result += char.lower()  # Convert consonants to lowercase
            else:
                result += char  # Keep spaces, punctuation unchanged
        s = result  #updated string
        print("Your poetic string is:", s)
    else:
        # n is even
        reversed_s = ''
        print("Your registration number is even, hence your script will be reversed as in ancient sanskrit scripts!")
        for char in s:
            reversed_s =  char + reversed_s
        s = reversed_s  #updated the string
        print("Mirror perspective:", s)
    # after doing one of the above two transformations, its time to form sub strings
    k = int(count_set_bits(n))
    print(f"Number of 1s (set bits) in binary {n} ({bin(n)}) is: {k}")
    sub_strings = list(extract_substrings(s, k))
    print("Substrings of length", k, "are:", sub_strings) 

    sort_or_reverse(n, s, sub_strings)
    # after completion ask the user if he wants to continue
    check_continue()

#main
def main():
    # taking input from the user
    # making sure the input is a positive integer
    while True:
        try:
            n = int(input("Enter your registration number: "))  # unique registration number of the writer
            if n <= 0:  # n should be positive integer
                raise ValueError("The registration number must be a positive integer.")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
       
    s = input("Enter your content: ")      # content string representing writer's text
    process_string(n, s) 
    
main()  # start of the program
