#Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.

import random

for i in range(10):
	x=random.random()
	print("pseudorandom number",i,":", x)


"""	output:
1st run:
pseudorandom number 0 : 0.4233818796826032
pseudorandom number 1 : 0.03769028458618828
pseudorandom number 2 : 0.08212855534044106
pseudorandom number 3 : 0.5062538873306858
pseudorandom number 4 : 0.7717094844886577
pseudorandom number 5 : 0.3135212493492633
pseudorandom number 6 : 0.5146792025989035
pseudorandom number 7 : 0.44028717308583365
pseudorandom number 8 : 0.6806970827082004
pseudorandom number 9 : 0.4892405016515964

2nd run:
pseudorandom number 0 : 0.10349836238648735
pseudorandom number 1 : 0.5337116938315652
pseudorandom number 2 : 0.7626598717805779
pseudorandom number 3 : 0.6583204359296251
pseudorandom number 4 : 0.13098983805526354
pseudorandom number 5 : 0.4958073872763985
pseudorandom number 6 : 0.9246739350447256
pseudorandom number 7 : 0.5554116932860521
pseudorandom number 8 : 0.6015264669112084
pseudorandom number 9 : 0.11650966304366428


"""