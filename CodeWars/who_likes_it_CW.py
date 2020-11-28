def likes(names):
    #your code here
    
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return names[0] + ' likes this'
    elif len(names) < 4:
        return ', '.join([i for i in names[:-1]]) + ' and ' + names[-1] + ' like this'
    else:
        return ', '.join([i for i in names[:2]]) + ' and ' + str(len(names[2:])) + ' others like this'
    