# Python If Statements Notes

How to make decisions in python programs.

| symbol | Meaning                                                   |
|--------|-----------------------------------------------------------|
| ==     | determines if two values are equal                        |
| !=     | determines if two values are not equal                    |
| \>     | determines if a value is greater than another             |
| <      | determines if a value is less than another                |
| \>=    | determines if a value is greater than or equal to another |
| <=     | determines if a value is less than or equal to another    |


# Logical operators

| operator | sample  | use                                                                     |
|----------|---------|-------------------------------------------------------------------------|
| or       | x or y  | either x or y must be true                                              |
| and      | x and y | BOTH x and y must be true                                               |
| not      | not x   | if x is true, this evals to false and if x is false, this evals to true |


# Events

Events are actions that trigger responses by the program.
For instance, if a keypress event occurs, the program will respond to that event by performing some action such as closing down.

```
if event.type==QUIT or (event.type==KEYUP and 	event.key==K_ESCAPE):
   sys.exit()
            
elif event.type==KEYUP:
   if event.key==K_UP:
      keys = "Up Key"
   elif event.key==K_DOWN:
      keys = "Down Key"
   elif event.key==K_LEFT:
      keys = "Left Key"
   elif event.key==K_RIGHT:
      keys = "Right Key"

```