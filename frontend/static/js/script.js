function classifyEmail() {
    let emailText = document.getElementById("emailText").value;

    if (!emailText) {
        alert("Please enter some text!");
        return;
    }

    fetch("http://127.0.0.1:8000/api/classify/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email_text: emailText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Classification: " + data.classification;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = "Error processing request.";
    });
}