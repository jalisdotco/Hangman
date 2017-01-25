import random, string, sys 

bank = ['print','bank','prints','printing','printed','printer','letter',\
'kalashkinov','honduras','yeti','roaming','backup','ohkay']
bank = ['hello there']
letters = string.ascii_lowercase
words = random.choice(bank)
##star = '*' * len(words)            
guesses = 0
end = 'game over'

# Added a really Cool
print words
#
print guesses
##print star
while guesses != 10: 
    command = raw_input("Your guess:")
    if command in ['quit','exit']:
        sys.exit(0)
    guesses += 1

    print guesses

    