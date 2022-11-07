himalayan(a).
himalayan(b).
himalayan(c).
himalayan(X):-mountain(X);skier(X).

like(a, rain).

like(a, snow).

like(b, V):-notlike(a, V).
notlike(b, Y):-like(a, Y).

mountain(Z):-notlike(Z, rain).

skier(W):-like(W,snow).

g(M):-himalayan(M),mountain(M),not(skier(M)),!.
