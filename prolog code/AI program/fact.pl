fact(0,1).
fact(N,Z):- P is N-1,fact(P,Q),Z is N*Q.
