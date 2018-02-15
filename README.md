A minimal compiler written in Python to imitate the Lisp language. Aims to learn more programming knowledge by coding on stuff. The codes are currently being developing.
## Overviews of how this compiler work
1. Read the program string
2. Fit the string into a AST which each node containing one token
3. Replace The nodes with variable recursively until the whole tree only consist of primitive operation
4. Evaluate the root and return the value


## Few examples (Cases needed to be considered when developing)
- Basic operaters
```
(if (< 3 4) (5) (+ 4 6)) //5
```
- Simple function
```
(define (square x) (* x x) )(square 3) //9
```
- Closure
```
(define (addxFunc x) 
(lambda y) (+ x y)
)
((addXFunc 3) (5)) //8
```
- Lambda function
```
(define (applyTwice f x) (f (f (x)))
(applyTwice (lambda (x)(* x 2)) 5)//20
```
- Nested functions
```
(define (plusTwo x)
(
(define (plusOne x)(+ x 1))
(plusOne (plusOne x))
))
(plusTwo 3) //5
(plusTwo 
```

- List operation (con car cdr)
