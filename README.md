# cellular-automata

project around cellular automata.

## description
30x30 grid with randomly generated 50 men and 50 women.
Each person gets a random value between 0 and 100.
The goal is to match everyone so that each couple has the lowest value.
The value of the couple is abs(men.value-woman.value).

Each generation the non-empty cells can move to a random direction or stay still.
If two non empty cells meat, they  can become a couple or change partners if they are allready in a relationship.

### start example
<img src="https://i.imgur.com/5cWOqlP.png">

### mid example
<img src="https://i.imgur.com/7aGZ5no.png">

### end example
<img src="https://i.imgur.com/hhO8qn0.png">

