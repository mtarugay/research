#ticket file

class Ticket:
    ticketNo : 2000 #need to have a counter with a constant +1 per ticket!!!
    ticketCr : None
    staffID : None
    email : None
    desc : None
    _response : "Not Yet Provided"
    _ticketStatus : "Open"

    def __init__(self, ticketNo, ticketCr, staffID, email, desc, _response, _ticketStatus):
        self.ticketNo = ticketNo
        self.ticketCr = ticketCr
        self.staffID = staffID
        self.email = email
        self.desc = desc
        self._response = _response
        self._ticketStatus = _ticketStatus

    def createticket(self):
        print("---CREATING TICKET---")
        self.ticketCr = input("Ticket Creator: ")
        self.staffID = input("Staff ID: ")
        self.email = input("Email Address: ")
        self.desc = input("Description: ")
        self._response = "Not Yet Provided"
        self._ticketStatus = "Open"
        print("")
        #consider an option that allows the user to add a response in this function
        #makes a ticket that can be filled in, assign variables for each section(?)
        pass

    def respondticket(self):
        if self._ticketStatus == "Open":
            print("---TICKET RESPONSE---")
            self._response = input("Add Response: ")
            print("")
            self._ticketStatus = "Closed"
        else:
            pass

    def reopenticket(self):
        if self._ticketStatus == "Closed":
            self._ticketStatus = "Reopened"
            # newcount = 1
            # return newcount
            # might use newcount from here for updating counter in main file, vs updating counter with a function in main file

    def ticketpassword(self):
        if "Password change" in self.desc:
            self._response = (f"Generated new password: {self.staffID[0:2]}{self.ticketCr[0:3]}")
            self._ticketStatus = "Closed"
        else:
            pass
    #consider an autoscan that checks for password before running a manual ticket response in one method
    # def respondticket(self):
    #     if "Password change" in self.desc:
    #         self._response = (f"Generated new password: {self.staffID[0:2]}{self.ticketCr[0:3]}")
    #         self._ticketStatus = "Closed"
    #     else:
    #         print("---TICKET RESPONSE---")
    #         self._response = input("Add Response: ")
    #         self._ticketStatus = "Closed"

    def reopenticket(self):
        self._ticketStatus = "Open"
        #do -1 on closed tickets, +1 on open tickets

    def display(self):
        print("---TICKET DETAILS---")
        print("Ticket Number:", self.ticketNo)
        print("Ticket Creator:", self.ticketCr)
        print("Staff ID:", self.staffID)
        print("Email Address:", self.email)
        print("Description:", self.desc)
        print("Response:", self._response)
        print("Ticket Status:", self._ticketStatus)
        print("")