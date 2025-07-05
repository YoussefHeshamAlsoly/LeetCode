def nextGreatestLetter(letters, target):
    """
    :type letters: List[str]
    :type target: str
    :rtype: str
    """
    letters = [ord(i) for i in sorted(set(letters))]
    
    print(letters)
    for i in letters:
        print(i)
        if i > ord(target):
            return chr(i)
    return(chr(letters[0]))

lets = ["c","f","j"]
target = 'c'
print(nextGreatestLetter(lets, target))
