from matplotlib import pyplot as plt
from matplotlib import pylab as plb
import numpy as np

def findpayment(loan, r, m):
    return loan*((r*(1+r)**m)/((1+r)**m-1))

class mortgage():
    def __init__(self,loan, annual_rate, months):
        self.loan=loan
        self.rate=annual_rate/12.0
        self.months=months
        self.paid=[0.0]
        self.outstanding=[loan]
        self.payment=findpayment(loan, self.rate, months)
        self.legend=None

    def makepayment(self):
        self.paid.append(self.payment)
        reduction=self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def gettotalpaid(self):
        return sum(self.paid)

    def __str__(self):
        return self.legend

    def plotpayments(self,style):
        plb.plot(self.paid[1:],style,label=self.legend)

    def plotbalance(self,style):
        plb.plot(self.outstanding,style, label=self.legend)

    def plottotpaid(self,style):
        totpaid=[self.paid[0]]
        for i in range(1, len(self.paid)):
            totpaid.append(totpaid[-1] + self.paid[i])
        plb.plot(totpaid,style, label=self.legend)

    def plotnet(self,style):
        totpaid=[self.paid[0]]
        for i in range(1,len(self.paid)):
            totpaid.append(totpaid[-1]+self.paid[i])
        equityacquired=plb.array([self.loan] * len(self.outstanding))
        equityacquired = equityacquired - plb.array(self.outstanding)
        net=plb.array(totpaid)-equityacquired
        plb.plot(net,style, label=self.legend)

class fixed(mortgage):
    def __init__(self,loan, r, months):
        mortgage.__init__(self,loan,r,months)
        self.legend = 'Fixed, ' + str(round(r*100,2)) + '%'

class fixedwithpts(mortgage):
    def __init__(self,loan, r, months, pts):
        mortgage.__init__(self,loan, r, months)
        self.pts=pts
        self.paid=[loan*(pts/100.00)]
        self.legend = 'Fixed, ' + str(round(r*100,2)) + '%, ' + str(pts) + ' points'

class TwoRate(mortgage):
    def __init__(self,loan,r,months,teaserrate, teasermonths):
        mortgage.__init__(self, loan, teaserrate, months)
        self.teaserrate=teaserrate
        self.teasermonths=teasermonths
        self.nextrate=r/12.0
        self.legend=str(teaserrate*100)+' % for '+str(self.teasermonths)\
                    +' months, then ' + str(round(r*100,2)) + '%'

    def makepayment(self):
        if len(self.paid) == self.teasermonths +1:
            self.rate=self.nextrate
            self.payment=findpayment(self.outstanding[-1],self.rate,self.months-self.teasermonths)

        mortgage.makepayment(self)

def comparemortgages(amt,years,fixedrate,pts,ptsrate,varrate1,varrate2,varmonths):
    totmonths=years*12
    fixed1=fixed(amt,ptsrate,totmonths)
    fixed2=fixedwithpts(amt,ptsrate,totmonths,pts)
    tworate=TwoRate(amt,varrate2,totmonths,varrate1,varmonths)
    morts=[fixed1,fixed2,tworate]
    for m in range(totmonths):
        for mort in morts:
            mort.makepayment()
    plotmortgages(morts,amt)

def plotmortgages(morts, amt):
    def labelplot(figure, title, xlabel,ylabel):
        plb.figure(figure)
        plb.title(title)
        plb.xlabel(xlabel)
        plb.ylabel(ylabel)
        plb.legend(loc='best')
    styles = ['y-','r-.','g:']
    payments, cost, balance, netcost = 0,1,2,3
    for i in range(len(morts)):
        plb.figure(payments)
        morts[i].plotpayments(styles[i])
        plb.figure(cost)
        morts[i].plottotpaid(styles[i])
        plb.figure(balance)
        morts[i].plotbalance(styles[i])
        plb.figure(netcost)
        morts[i].plotnet(styles[i])

    labelplot(payments,' Monthly payments of $ ' + str(amt) +' Mortgages ', 'Months', ' Monthly Payments')

    labelplot(cost, 'Cash Outlay of $' + str(amt) +' Mortgages ', ' Months', 'Total Payments')

    labelplot(balance, 'Balance Remaining of $' + str(amt) + ' Mortgages ', ' Months', 'Remaining Loan Balance of $')

    labelplot(netcost, 'Net Cost of $' + str(amt) + ' Mortgages ', ' Months', 'Payments - Equity $')

comparemortgages(amt=200000,years=30, fixedrate=0.07,pts=3.25,ptsrate=0.05,varrate1=0.045,varrate2=0.095,varmonths=48)

plb.show()

