import random

def margin_of_error(x, y, n):
    prob_error = 100 - x - y
    b = n + prob_error
    moex = random.choice(range((n*-1),(b+1),1))
    moey = random.choice(range((n*-1),(n+1),1))
    x += moex
    y += moey
    return (x, y)

def election_sim(x, y, moe, number_of_elections=20000):
    x = int(x)
    y = int(y)
    moe = int(moe)
    no_wins = 0 # number of wins x over y
    no_sure_wins = 0 # number of wins by majority
    for i in range(number_of_elections):
        x1, y1 = margin_of_error(x, y, moe)
        victory = x1 - y1
        if victory >= 1:
            no_wins += 1
        if x1 >= 50:
            no_sure_wins += 1
    no_wins_percentage = float(no_wins) / number_of_elections
    no_sure_wins_percentage = float(no_sure_wins) / number_of_elections
    return no_wins_percentage, no_sure_wins_percentage


x = float(input("Enter polling bias candidate's RCP average: "))
print(x)
y = float(input("Enter their opponent's RCP average: "))
print(y)
moe = float(input("Enter the highest margin of error: "))
print(moe)
print()

nwp, nswp = election_sim(x,y,moe)

print("% of Election Wins: ", 100*nwp)
print("% of Majority Wins (over 50% of votes): ", 100*nswp)
print()
