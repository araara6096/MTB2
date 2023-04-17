fib(1,1).
fib(2,1).
fib(N,Z):-P is N-1,fib(P,A),Q is N-2,fib(Q,B), Z is A+B.
