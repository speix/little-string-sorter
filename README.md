# Little String Sorter
Given a list of strings that represent encoded messages where the first column is the identifier
and the remaining parts is the actual content to be put in order, sort them out in a way such that:
1. First in place are the actual characters in alphabetical order.
2. Then the digits in ascending order.
3. If there is an exact match, re-order based on the first column (the identifier).

### Example

##### Given List of strings:
```
'q1 30 41 222',
'b5 xi me nu',
'br8 eat nim did',
'w1 has uni gry',
't2 34 54 398',
'f3 34 54 410',
'r1 box ape bit',
'b4 xi me nu',
'a3 34 54 410',
'a2 34 54 398'
```

##### Desired output:
```
'r1 box ape bit',
'br8 eat nim did',
'w1 has uni gry',
'b4 xi me nu',
'b5 xi me nu',
'q1 30 41 222',
'a2 34 54 398',
't2 34 54 398',
'a3 34 54 410',
'f3 34 54 410'
```
