1) Determine Daily Volatility: Average True Range (5 days/10 days)
2) Based on the ATR and percentage risk of the account, determine contract size: ```RiskPct * AccountBal/ ATR```
3) Scaling the **notional** account size based on how much acc up/down: 10% down, notional account becomes -20% and repeat the process above again
4) Entry rule: 
* Entry: shorter term: Break out of 20-day box + longer term: 55 day box: place one unit of trade 
* Monitor: Break-out considered failed if price move 2N against initial price before 10-day opposition breakout
* If fail to enter 20-day breakout, monitor 55-day box
* If 20-day breakout is false breakout, enter on the next 20-day break out
* If 55-day box broken out --> enter
5) Adding position by price + 1/2N 
6) Move-up stoploss: based on 5) move the initial position stop 1/2N so that the total position risk is now 2N (each one is 1N)
7) For each instrument: more volatility = wider stop and smaller position size
8) Determine Strength and Weakness based on how many N has move from the last breakout, divided by N to normalize among markets
