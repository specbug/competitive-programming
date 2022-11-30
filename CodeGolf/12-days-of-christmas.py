g = "A Partridge in a Pear Tree.#Two Turtle Doves, and#Three French Hens,#Four Calling Birds,#Five Gold Rings,#Six Geese-a-Laying,#Seven Swans-a-Swimming,#Eight Maids-a-Milking,#Nine Ladies Dancing,#Ten Lords-a-Leaping,#Eleven Pipers Piping,#Twelve Drummers Drumming,".split('#')
d = 'First Second Third Fourth Fifth Sixth Seventh Eighth Ninth Tenth Eleventh Twelfth'.split()
for i in range(12):
	print(f'On the {d[i]} day of Christmas\nMy true love sent to me\n'+"\n".join(g[:i+1][::-1])+'\n')