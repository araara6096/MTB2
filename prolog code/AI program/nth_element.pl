nth_element(1, [X|_], X).
nth_element(N, [_|T], X) :- N > 1, M is N - 1, nth_element(M, T, X).
