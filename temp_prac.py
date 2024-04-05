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

    def show_read_status(self):
        if self.has_been_read != False:
            return self.subject_line + " has been read."
    # Create the method to change 'has_been_read' emails from False to True.
        def mark_as_read():
            if self.has_been_read == False:
                self.has_been_read = True
            

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
def populate_inbox():
        # Create 3 sample emails and add it to the Inbox list. 
        inbox.append = Email("example@hypdv.com", "Welcome to HyperionDev!", "A very warm welcome to your new course!", False)
        inbox.append = Email("bootcamp@email.com", "Great work on the Bootcamp!", "Your work has been outstanding!", False)
        inbox.append = Email("marksbot@email.com", "Your excellent marks!", "The best marks we've ever seen!", False)

