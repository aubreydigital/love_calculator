print()
print('Welcome to the Love Calculator!')
print('-' * 30)
name1 = input('What is your name?\n')
name2 = input('What is their name?\n')
nameArr = list(name1.lower() + name2.lower())
true= ['t', 'r', 'u', 'e']
love = ['l', 'o', 'v', 'e']
truels = 0
lovels = 0
for c in nameArr:
    for l in true:
        if c in l:
            truels += 1
    for l in love:
        if c in l:
            lovels += 1


loveScore = int(str(truels) + str(lovels))
if loveScore < 10 or loveScore > 90:
    print(f'Your score is {loveScore}, you go together like coke and mentos.')
elif loveScore >= 40 or loveScore <= 50:
    print(f'Your score is {loveScore}, you are alright together')
else:
    print(f'Your score is {loveScore}')
