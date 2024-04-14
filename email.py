### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
        # Declare the class variable, with default value, for emails. 
    email_contains = "@"
    has_been_read = False
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content, has_been_read):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = has_been_read
        self.read_status = has_been_read

    def __str__(self) -> str:
        return f"Sender: {self.email_address}, \nSubject: {self.subject_line}, \nContent: {self.email_content}, \nRead status: {self.has_been_read}\n"
        # pass

    def show_read_status(self):
        if self.has_been_read != False:
            return self.subject_line + " has been read."
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        if self.has_been_read == False:
            self.has_been_read = True
            

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = [] 
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
        # Create 3 sample emails and add it to the Inbox list. 
    email_0 = Email("example@hypdv.com", "Welcome to HyperionDev!", "A very warm welcome to your new course!", False)
    email_1 = Email("bootcamp@email.com", "Great work on the Bootcamp!", "Your work has been outstanding!", False)
    email_2 = Email("marksbot@email.com", "Your excellent marks!", "The best marks we've ever seen!", False)

    inbox.append(email_0) 
    inbox.append(email_1) 
    inbox.append(email_2) 


def list_emails():
        # Create a function which prints the email’s subject_line, along with a corresponding number.
    for i, email in enumerate(inbox, start=1):
        print(f"email number {i}: {email.subject_line}")
        


def read_email():
    
    for k in inbox:
        # k = inbox[k]
        print(f"\nEmail:\n{k}")
        # mark_as_read()
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

populate_inbox()
# --- Email Program --- #
print("Welcome to the email program.\n\nHere are your emails: ")
list_emails()

# Call the function to populate the Inbox for further use in your program.


# new_email = inbox.append[]

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        print("Select an email:")
        for i, email in enumerate(inbox, start=1):
            print(f"{i}. {email.subject_line}")

        selected_email = int(input("Enter the number corresponding to the email you'd like to read: "))

        if 1 <= selected_email <= len(inbox):
            print(f"You selected: {inbox [selected_email - 1]}")
            # Email.read_status = True
            # Email.mark_as_read(has_been_read = True)
        
        else:
            print("Invalid choice. Please select a valid option.")


    elif user_choice == 2:
        # add logic here to view unread emails
        # for e in inbox:
            # if not Email.read_status:
                read_email()

    elif user_choice == 3:
        # add logic here to quit appplication
        print("Thank You and Goodbye.")
        exit()

    else:
        print("Oops - incorrect input.")

