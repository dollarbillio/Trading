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

If position is Long GU as the best position, want Long G, Short U, 
Maximum position:Long GJ and Short UJ -> if GU is up -> keep the position
                                      -> if GU is down -> short UJ
Lesser position: GJ up and UJ up (Strength of U) --> If GU is up -> Change to long GJ 
                                                 --> If GU is down ->  Change to long UJ
                GJ down and UJ down (weakness of G) --> if GU is up --> Change to short UJ
                                                    --> if GU is down --> short GJ
Worst position: GJ down and UJ up (weakness of G and strength of U) --> if GU up --> long UJ
                                                                    --> if GU down --> short GU
-------------------------------------------------------------------------------------------------
If position is Short GJ as the best position, want Short G, Long J, 
Maximum position: Short GU and Short UJ -> if GJ is up -> Short UJ
                                      -> if GJ is down -> keep the position
Lesser position: GU down and UJ up (Strength of J) --> If GJ is up -> Change to long UJ 
                                                 --> If GJ is down ->  Change to short GU
                GU up and UJ down (strength of G) --> if GJ is up --> Change to short UJ
                                                    --> if GJ is down --> short GJ
Worst position: GU up and UJ up (weakness of J and strength of G) --> if GJ up --> long GJ
                                                                    --> if GJ down --> long UJ
