def addtoVault(username, password, website, vault):
    
    #Check if the login/website has already been entered
    if website in vault:
        vault[website] = (username, password)
        print(f"Login information for {website} updated successfully")
        #Updates previously entered information
    else:
        vault[website] = (username, password)
        print(f"Login information for {website} has been added to the vault")
        #Adds new information into the vault
