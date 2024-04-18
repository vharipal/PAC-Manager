from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/addToVault', methods=['POST'])
def addToVault(website, username, password, ID, vault):
    
    #Check if the login/website has already been entered
    if ID in vault:
        editVault(website, username, password, ID, vault)
        print("Rerouting to edit information \n")
        #redirects to edit
    else:
        vault[ID] = (website, username, password)
        print(f"Login information for {website} has been added to the vault")
        #Adds new information into the vault

@app.route('/editVault', methods=['POST'])
def editVault(website, username, password, ID, vault):
    vault[ID] = (website, username, password)
    print("Login information updated successfully")
    #Updates previously entered information
    print("Editing vault:", request.json)
    return jsonify({"message": "Information edited in the vault"})

@app.route('/deleteFromVault', methods=['POST'])
def deleteFromVault(website, username, password, ID, vault):
    if ID in vault:
        del vault[ID]
        print("Entry deleted successfully.")
    else:
        print("Invalid Entry ID Provided")

if __name__ == '__main__':
    app.run(debug=True)


