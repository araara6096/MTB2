reverse_list([], []).
reverse_list([X], [X]).
reverse_list([H | T], R) :- reverse_list(T, R1), append(R1, [H], R).is_palindrome([]).  % An empty list is a palindrome
is_palindrome([_]). % A single-element list is a palindrome
is_palindrome(List) :-
    append([First|Middle], [Last], List), % Split the list into a first element, a middle sublist, and a last element
    First == Last,                        % The first and last elements must be the same
    is_palindrome(Middle).                % Check if the middle sublist is a palindrome

