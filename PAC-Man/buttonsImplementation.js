<!DOCTYPE html>
<html>
<head>
    <title>PAC-Manager</title>
</head>
<body>

<button id="addButton">Add</button>
<button id="editButton">Edit</button>
<button id="deleteButton">Delete</button>
<button id="checkStrength">Check Password Strength</button>
<button id="generatePass">Generate</button>

<script>
    // Event listeners for buttons
    document.getElementById("addButton").addEventListener("click", function() {
        fetch('/addToVault', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({data: "data to add to vault"})
        })
        .then(response => response.json())
        .then(data => console.log(data));
    });

    document.getElementById("editButton").addEventListener("click", function() {
        fetch('/editVault', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({data: "data to edit in vault"})
        })
        .then(response => response.json())
        .then(data => console.log(data));
    });

    document.getElementById("deleteButton").addEventListener("click", function() {
        fetch('/deleteFromVault', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({data: "data to delete from vault"})
        })
        .then(response => response.json())
        .then(data => console.log(data));
    });

    //Need to check function compatibility before officially adding
    document.getElementById("checkStrength").addEventListener("click", function() {
        fetch('/password_check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({password: "password to check"})
        })
        .then(response => response.json())
        .then(data => console.log(data));
    });

    document.getElementById("generatePass").addEventListener("click", function() {
        fetch('/password_gen', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({}) //Might not need
        })
        .then(response => response.json())
        .then(data => console.log(data));
    });

</script>

</body>
</html>
