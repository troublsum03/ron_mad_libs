from random import randint
import copy

story = (
    "One day {} friend and I decided to go to the {} game in {}. " +
    "We really wanted to see the {} play the {}. " +
    "So, we {} out {} down to the {} and bought some {}s. " +
    "We got into the game and it was a lot of fun. " +
    "We ate some {} {} and drank some {} {}. " +
    "We had a great time! We plan to go ahead next year!"
)

# create a dictionary to lookup words by type
word_dict = {
    'adjective':['greed', 'abrasive', 'grubby' 'rich', 'harsh', 'tasty'],
    'city name':['Chicago', 'New York', 'Charlotte', 'Los Angeles', 'San Antonio', 'Louisville', 'Denver'],
    'noun':['people', 'map', 'music', 'dog', 'hamster', 'ball', 'hotdog', 'salad'],
    'action verb':['run', 'fall', 'craw;', 'scurry', 'cry', 'watch', 'swim', 'jump', 'bounce'],
    'sports noun':['ball', 'mit', 'punk', 'uniform', 'helmet', 'scoreboard', 'player'],
    'place':['park', 'desert', 'forest', 'store', 'restaurant', 'waterfall']
}

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('place', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
    )

print("STORY 1: ")
print(create_story())
print()
print("STORY 2: ")
print(create_story())
print()
print("STORY 3: ")
print(create_story())
print()
print("STORY 4: ")
print(create_story())
