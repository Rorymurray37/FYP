def buy(df,bal,holdings,priceindex,sellindex):

    close = df.columns.get_loc("Close") # get index of close col

    buyprice = df.iloc[priceindex,close]
    sellprice = df.iloc[priceindex+sellindex,close] #sell price 100 timesteps forward

    buytotal = 10 * buyprice



    bal = bal - buytotal #10 shares bought
    newposition = Position(buyprice,sellprice)

    return bal,holdings,newposition







def sell(bal,holdings,price):
    selltotal = 10*price
    bal = bal + selltotal


    return bal,holdings

def sellall(bal,holdings,price,shares):
    total = shares * price
    holdings = 0
    bal = total
    shares = 0
    return bal,holdings

class Position:
    def __init__(self, buyprice, sellprice):

        self.buyprice = buyprice
        self.sellprice = sellprice


    def get_sellprice(self):
        return sellprice

    def get_buyprice(self):
        return buyprice



# Paper Trade
#works buy buying when label 1, balance is updated and a new position object is created until the
#position is finally closed

def paperTrade(df,sellindex):

    balance = 100000
    stockholdings = 0
    numShares = 0
    Labelcol = df.columns.get_loc("Label") # get index of label col
    close = df.columns.get_loc("Close")


    buylist = []  #list to store buy positions

    for i in range(len(df)):
        if df.iloc[i,Labelcol] == 1:
            if balance > 10 * df.iloc[i,close] and i+sellindex<len(df):

                balance,stockholdings,position = buy(df,balance,stockholdings,i,sellindex)
                #print(balance)
                buylist.append(position)





        if len(buylist) != 0:  #buylist not empty
            for t in buylist:
                pos = t
                sellprice = pos.sellprice

                if(df.iloc[i,close] >= sellprice):
                    balance,stockholdings = sell(balance,stockholdings,sellprice)

                    buylist.remove(pos)
                    del pos



    print(len(buylist))
    balance = float(str(round(balance, 2))) #rounding
    stockholdings = float(str(round(stockholdings,2)))


    print('Final balance : ',balance)   #print outputs
    print('Final holdings : ', stockholdings)
    pl =  balance - 100000
    pl_percentage = pl/100000 *100
    print( "P&L : ", pl,'  Gain : ',pl_percentage,'%' )

            
