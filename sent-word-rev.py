def reversal(sentence: str):
    # Split the sentence into words by whitespace
    # Filter out any empty strings caused by leading/trailing/multiple spaces
    words = [w for w in sentence.split(' ') if w]
    
    revword= []
    
    for word in words: 
        word = word[::-1]
        print(word)
        revword.append(word)
    
    print(revword)
    joined = " ".join(revword)
    print(joined)

    
    
    return words

sample = "this is killer "

print(reversal(sample))

