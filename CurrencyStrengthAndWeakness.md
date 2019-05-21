```py
signs = input ("Signs for GJ_GU_UJ?: ")
if signs == "+++":
    print ("G>J, G>U, U>J --> Long GJ")
if signs == "++-":
    print ("G>J, G>U, U<J --> Long GU")
if signs == "+--":
    print ("G>J, G<U, U<J --> Rotation")
if signs == "---":
    print ("G<J, G<U, U<J --> Short GJ")
if signs == "--+":
    print ("G<J, G<U, U>J --> Short GU")
if signs == "-++":
    print ("G<J, G>U, U>J --> Rotation")
if signs == "-+-":
    print ("G<J, G>U, U<J --> Short UJ")
if signs == "+-+":
    print ("G>J, G<U, U>J --> Long UJ")
```

-----------------------------------------------------------------------------------------------
**Long GU**
```
If current position = GU(-) as the best position, G(-), U(+), 
*Maximum position: GJ(-) and UJ(+) --> if GU(+) -> will not happen
                                   --> if GU(-) -> keep the position

*Lesser position: GJ(-) and UJ(-) (weakness of U) --> If GU(+) -> Change to short UJ
                                                  --> If GU(-) ->  Change to short GJ
                 GJ(+) and UJ(+) (strength of G)  --> if GU(+) -> Change to long GJ
                                                  --> if GU(-) -> long UJ

*Worst position: GJ(+) and UJ(-) [G(+) and U(+)] --> if GU(+) -> long GU
                                                 --> if GU(-) -> not happen
```
**Short GU**
```
If current position = GU(+) as the best position, G(+), U(-), 
*Maximum position:GJ(+) and UJ(-) --> if GU(+) -> keep the position (GU(+))
                                  --> if GU(-) -> Will not happen

*Lesser position: GJ(+) and UJ(+) (Strength of U) --> If GU(+) -> Change to long GJ 
                                                  --> If GU(-) ->  Change to long UJ
                  GJ(-) and UJ(-) (weakness of G) --> if GU(+) --> Change to short UJ
                                                  --> if GU(-) --> short GJ

Worst position: GJ(-) and UJ(+) (weakness of G and strength of U) --> if GU(+)  --> Will not happen
                                                                  --> if GU down --> short GU
```
**Short GJ**
```
If GJ(-) as the best position, G(-), J(+), 
Maximum position: GU(-) and UJ(-) --> if GJ(+) -> will not happens
                                  --> if GJ(-) -> keep the position
Lesser position: GU(-) and UJ(+) (Weakness of J) --> If GJ(+) -> Change to long UJ 
                                                 --> If GJ(-) ->  Change to short GU
                 GU(+) and UJ(-) (strength of G) --> if GJ(+) --> Change to long GU
                                                 --> if GJ(-) --> short UJ
Worst position: GU(+) and UJ(+) (weakness of J and strength of G) --> if GJ up --> long GJ
                                                                  --> if GJ down --> will not happen
```
**Long GJ**
```
If GJ(+) as the best position, G(+), J(-), 
Maximum position: GU(+) and UJ(+) --> if GJ(+) -> keep the position
                                  --> if GJ(-) -> will not happen
Lesser position: GU(-) and UJ(+) (Weakness of G) --> If GJ(+) -> Change to long UJ 
                                                 --> If GJ(-) ->  Change to short GU
                 GU(+) and UJ(-) (strength of J) --> if GJ(+) --> Change to long GU
                                                 --> if GJ(-) --> short UJ
Worst position: GU(-) and UJ(-) [J(+) and G(J)] --> if GJ up --> will not happen
                                                 --> if GJ down --> short GJ
```
