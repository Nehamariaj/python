movie_selection=int(input("Movie List:\n1.Rekhachitram\n2.Identity\n3.Marco\nWhich Movie Do You Want To Watch: "))
ticket_no=int(input("No of tickets: "))
print(f"No of tickets: {ticket_no}")
ticket_type=int(input("1.Premium Ticket (cost=300)\n2.Normal Ticket(cost=150)\nChoose Your Ticket Type: "))
show_time=int(input("Show Times:\n1.10.00am\n2.2pm\n3.6pm\n4.10pm\nChoose your timing: "))
print(f"Timing: {show_time}")
print("-----------------------------------------------------")
match movie_selection:
    case 1:
        print("Movie: Rekhachitram")
    case 2:
        print("Movie: Identity")
    case 3:
        print("Movie: Marco") 
    
match show_time:
    case 1:
        print("Timing: 10.00am")
    case 2:
        print("Timing: 2.00pm")
    case 3:
        print("Timing: 6.00pm")
    case 4:
        print("Timing: 10.00pm")

match ticket_type:
    case 1:
        print("Ticket Type: Premium Ticket")
        cost=(ticket_no*300)
        if ticket_no>5:
          print("You have received 10% discount")
          cost=cost-(cost*0.1)
        print(f"Total Cost: {cost}")
    case 2:
        print("Ticket Type: Normal Ticket")
        cost=(ticket_no*150)
        if ticket_no>5:
          print("You have received 10% discount")
          cost=cost-(cost*0.1)
        print(f"Total Cost: {cost}")
print("-----------------------------------------------------")
