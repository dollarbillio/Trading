signs = input ("Signs for GJ_GU_UJ?: ")
if signs == "+++":
    print ("G>J, G>U, U>J --> Long GJ")
if signs == "++-":
    print ("G>J, G>U, U<J --> Long GU")
if signs == "+--":
    print ("G>J, G<U, U<J --> Short UJ")
if signs == "---":
    print ("G<J, G<U, U<J --> Short GJ")
if signs == "--+":
    print ("G<J, G<U, U>J --> Short GU")
if signs == "-++":
    print ("G<J, G>U, U>J --> Long UJ")
if signs == "-+-":
    print ("G<J, G>U, U<J --> Short UJ")
if signs == "+-+":
    print ("G>J, G<U, U>J --> Long UJ")
