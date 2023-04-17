gcd(X,Y,D):- X=:=Y,D is X.
gcd(X,Y,D):-
    X>Y,
    X1=X-Y,
    gcd(X1,Y,D).
gcd(X,Y,D):-
    Y>X,
    gcd(Y,X,D).
