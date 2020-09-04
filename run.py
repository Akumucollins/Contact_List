from contact import Contact

# Creating a Contact
def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

# Save contacts
def save_contacts(contact):
    
    '''
    Function to save contact
    '''
    
    contact.save_contact()
    
# Delete contact    
def del_contact(contact):
   
    '''
    Function to delete a contact
    '''
   
    contact.delete_contact()
    
# Finding a contact    
def find_contact(number):
    
    '''
    Function that finds a contact by number and returns the contact
    '''
    
    return Contact.find_by_number(number)

# Check if a contact exists
def check_existing_contacts(number):
   
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
   
    return Contact.contact_exist(number)

# Displaying all contacts
def display_contacts():
    
    '''
    Function that returns all the saved contacts
    '''
    
    return Contact.display_contacts()

# Copying a contact email
def copy_email(number):
    '''
    Function that returns copied email
    '''
    return Contact.copy_email(number)

def main():
    print("Hello Welcome to your contact list. What is your name?")
    
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new contact, dc - display contacts, de - delete a contact, fc -find a contact, ce -copy email, ex -exit the contact list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("-"*10)

                    print ("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Phone number ...")
                    p_number = input()

                    print("Email address ...")
                    e_address = input()


                    save_contacts(create_contact(f_name,l_name,p_number,e_address))
                    print ('\n')
                    print(f"New Contact {f_name} {l_name} created")
                    print ('\n')
                    
            elif short_code == 'de':

                    print("Enter the number of the contact you want to delete")
                    
                    search_number = input()
                    if check_existing_contacts(search_number):
                             print ('\n')
                             search_contact = find_contact(search_number)
                             del_contact(search_contact)
                             
                             print(f"Contact is successfully deleted")
                             print ('\n')
                    else:
                             print("That contact you want to delete does not exist")
                                
            elif short_code == 'dc':

                    if display_contacts():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for contact in display_contacts():
                                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the number you want to search for")

                    search_number = input()
                    if check_existing_contacts(search_number):
                            search_contact = find_contact(search_number)
                            print(f"{search_contact.first_name} {search_contact.last_name}")
                            print('-' * 20)

                            print(f"Phone number.......{search_contact.phone_number}")
                            print(f"Email address.......{search_contact.email}")
                    else:
                            print("That contact does not exist")
                            
            elif short_code == 'ce':

                    print("Enter the number of the contact email you want to copy")
                
                    search_number = input()
                    if check_existing_contacts(search_number):
                           print ('\n')
                           
                           search_contact = find_contact(search_number)
                           copy_email(search_number)
                           
                           print(f"Contact copied to clipboard")
                           print ('\n')
                    else:
                           print("That contact you want to copy a contact email from does not exist")
               

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")
                            
if __name__ == '__main__':

    main()