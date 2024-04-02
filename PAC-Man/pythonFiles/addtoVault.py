def addtoVault(username, password, website, vault):
    
    #Check if the login/website has already been entered
    if website in vault:
        vault[website] = (username, password)
        print(f"Login information for {website} updated successfully")
    else:
        vault[website] = (username, password)
        print(f"Login information for {website} has been added to the vault")

#test
vault1 = {}
addtoVault("User", "pass", "website", vault1)
addtoVault("user1", "pass1", "website1", vault1)
print(vault1)