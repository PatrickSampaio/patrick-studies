vowels = 'AEIOU'

def minion_game(string):
    # your code goes here
    stuart_letters = set([letter for letter in string if letter not in vowels])
    kevin_letters = set([letter for letter in string if letter in vowels])
    
    kevin_points = calculate_score(string, kevin_letters)
    stuart_points = calculate_score(string, stuart_letters)
    
    winner_points = max(kevin_points, stuart_points)
    winner_name = 'Kevin' if winner_points == kevin_points else 'Stuart'
    
    print('{} {}'.format(winner_name, winner_points))
    
def calculate_score(string, letters):
    current_points = 0
    for letter in letters:
        words = []
        for i in range(0, len(list(string))+1):
            current_word = string[string.index(letter):i] 
            if not current_word:
                continue
            current_points += sum([1 if current_word == string[index:index+len(current_word)] else 0 for index in range(len(list(string)))])
            
    return current_points
    
