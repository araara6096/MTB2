sum_list([],0).
sum_list([H|T],N):-sum_list(T,X),N is X+H.
