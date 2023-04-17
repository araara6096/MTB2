conc([],L,L).
conc([H|T],L2,[H|L]):-conc(T,L2,L).
