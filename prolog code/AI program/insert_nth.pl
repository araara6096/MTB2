insert_nth(I, 1, L, [I|L]). % if inserting at first position, simply add I to the beginning of the list
insert_nth(I, N, [H|T], [H|R]) :- N1 is N-1, insert_nth(I, N1, T, R). % if not inserting at first position, remove the head element and recursively call insert_nth on the tail
insert_nth(_, _, [], []). % if the list is empty, there is no Nth position to insert into, so return an empty list as well.
