del(H,[H|T],T).
del(X,[H|T],[H|T1]):-del(X,T,T1).
