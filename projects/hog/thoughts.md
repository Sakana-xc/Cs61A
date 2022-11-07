Q5:
A strategy is a function that, given a player's
score and their opponnet's score, returns the number
of dice that the current player will roll in turn

and this game is a loop, whiile ends ether score0 or score 1 hit 100 or beyond

so now we have can call

who = 0

score(who) = take turn(strategy(who), opponent_score, dice=six_sided)

to get the current (who)players score

then we define weather player get another round:

if extre_turn:
who = 1
else:
who = 0

score0 += score 0
score1 += score 1

while max(score0, score1) < goal which is 100
game carry on

so when max(score0,score1) > 100
we need to print the bigger one, and game ends

The question is how to stop the game? what code

In Q2 there are two things that need attention paid
Frist while/ if / continue loop
Second strategy can not ne passed in the take_turn function directly , it needs to be defined as
num_rolls = strategy0(score0,socore1)// strategy1(score1, score0)
why?
