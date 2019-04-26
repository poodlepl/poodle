# CONTRIBUTING

All the PRs should be done to the poodle-patch branch.   
The `dev` branch is inactive as of now.

### TODO

1. Lexer   
    1. Add a forward buffer which sees a few characters ahead and thus performs the required actions.   
2. Parser   
    1. Show errors with line numbers.   
    2. Detect and print the errors which occurs first.
    3. If while loop's syntax is wrong, exit only the while loop and still parse the remaining program.
    4. While loop must be iterated if condition is correct, using operator and cond.   


Commit messages should be precise to what they do.
