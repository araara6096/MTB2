evenlength(List) :-
    length(List, Length),
    Length mod 2 =:= 0.

oddlength(List) :-
    length(List, Length),
    Length mod 2 =:= 1.
