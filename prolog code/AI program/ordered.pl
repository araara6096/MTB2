ordered([]).
ordered([_]).
ordered([H,T|Rest]):-T>=H,ordered([T|Rest]).
