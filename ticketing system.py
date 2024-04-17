#main ticketing file

from tickets import Ticket

tNum = 2000
ticketcounter = 0
openedtickets = 0
closedtickets = 0
tick = []
# tNum += ticketcounter

def displaystats():
    print("---TICKET STATISTICS---")
    print("Tickets Created:", ticketcounter)
    print("Tickets Opened:", openedtickets)
    print("Tickets Closed:", closedtickets)
    print("")

#possible: only do respond/reopen, then ask after input which ticket the user wants to respond/reopen.

p = 1

while p == 1:
    print("Type 'Display Tickets' to display all tickets. Type 'Create' to create a ticket. Type 'Respond' to respond to a ticket. Type 'Reopen' to reopen a ticket. Type 'Display Stats' to display ticket statistics. Type 'Exit' to close program.")
    reqholder = input()
    if "Respond" in reqholder:
        ticketinteract = int(input("Input the desired ticket to respond to: "))
        tick[ticketinteract - 2001].respondticket()
        tick[ticketinteract - 2001].display()
        openedtickets -= 1
        closedtickets += 1
    elif "Reopen" in reqholder:
        ticketinteract = int(input("Input the desired ticket to reopen: "))
        tick[ticketinteract - 2001].reopenticket()
        tick[ticketinteract - 2001].display()
        openedtickets += 1
        closedtickets -= 1
    elif "Create" in reqholder:
        ticketcounter += 1
        openedtickets += 1
        tick.append(str(tNum + ticketcounter))
        tick[ticketcounter - 1] = Ticket(tNum + ticketcounter, ".", ".", ".", ".", ".", ".",)
        tick[ticketcounter - 1].createticket()
        tick[ticketcounter - 1].ticketpassword()
        tick[ticketcounter - 1].display()
        if tick[ticketcounter - 1]._ticketStatus == "Closed":
            openedtickets -= 1
            closedtickets += 1
        else:
            pass
    elif "Display Stats" in reqholder:
        displaystats()
    elif "Display Tickets" in reqholder:
        tickprint = 1
        for i in tick:
            tick[tickprint - 1].display()
            tickprint += 1

    elif "Exit" in reqholder:
        break
    else:
        print("Invalid Input.")

#make a display for stats, and display for tickets, give user a chance to reopen or respond to tickets after(?) (or let them respond as the ticket is made.)