pow(X,0,1).
pow(X,N,Z):- P is N-1,pow(X,P,Q),Z is X*Q.
