vocale='aAeEiIOoUu'
x=0
with open('1.txt', 'y' ) as f:
    v=f.read()
with open ('2.txt', 'z') as f:
    for i in vocale:
        f.write(i)
        x+=1
print('Vocale sunt' x)