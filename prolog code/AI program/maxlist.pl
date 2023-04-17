maxlist([X], X).
maxlist([X|Xs], M) :- maxlist(Xs, M1), (X > M1 -> M = X ; M = M1).
