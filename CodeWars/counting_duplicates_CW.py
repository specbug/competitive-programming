def duplicate_count(text):
    # Your code goes here
    
    counter = {}
    ans = 0
    
    for i in text:
        i = i.lower()
        counter[i] = counter.get(i, 0) + 1    
    
    for i in list(counter.values()):
        if i > 1:
           ans += 1
    
    return ans