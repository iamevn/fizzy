# fizzy
- a fizzy program consists of lines containing a sequence of one or more comma separated natural numbers followed by a colon, followed by a string.
- the final line in a fizzy program is two comma separated integers representing an inclusive range to loop over.
- when executed, a fizzy program shall print out the numbers in that range in increasing order
- except for values which are congruent to 0 modulo a number in each rule. these values will instead print the string associated with that rule
- only one number for each rule must match.
- multiple numbers for the same rule shall only print the string once
- multiple rules matching shall print each string in order from the lowest matching number to the highest
- a backwards range like `10,1` is allowed and indicates that iteration should be done in decreasing order
- a blank program is shorthand for the canonical fizzbuzz:
```
3:fizz
5:buzz
1,100
```

- a program consisting of just the range `R` is shorthand for:
```
3:fizz
5:buzz
R
```

- a range with just one number is assumed to start from 1
- rules producing the same string are allowed
- overlapping rules (rules with the same modulus) are allowed, they shall be printed in the order that they occure in the source code

## Examples
- program:
```
2,4:hello
3:world
13
```
output:
```
1
hello
world
hello
5
helloworld
7
hello
world
hello
11
worldhello
13
```

- program:
```
1:_
2:.
3:,
6,0
```
output:
```
_.,
_
_.
_,
_.
_
_.,
```

- program:
```
1:🙃
2:🙃
4
```
output:
```
🙃
🙃🙃
🙃
🙃🙃
```

- program:
```
3,4:over
2,3:lap
2,6
```
output:
```
lap
overlap
lapover
5
over
```

<!-- step size? -->

