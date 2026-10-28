ascii_art=[
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,    
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
        """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
        """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
          |
          |
          |
          |
          |
    =========
    """]


import random
words=['mecca','yemen','bangeladesh']
random_word=random.choice(words)
dash_list=['_']*len(random_word)
print(*dash_list,end=f"\n{ascii_art[6]}" )
tries=6
no_repeat_list=[]
while "_" in dash_list and tries > 0:
    guess= input ("please enter a letter: ").lower()
    if guess in no_repeat_list:
        print("you have entered this letter, please try again")
        continue
    no_repeat_list.append(guess)
    if guess not in random_word: 
        tries -= 1
    else:
        for position in range(len(random_word)):
          if random_word[position]==guess :
              dash_list[position]=guess
              
    print(" ".join(dash_list))       
    print(ascii_art[tries],f"\nyou have {tries} left..")
if tries==0:
    print("Sorry you lost, please try another time!") 
else :
    print (""" 
           *****************
           congrats! You won
           *****************
           """)

