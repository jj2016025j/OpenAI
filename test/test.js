const form = document.querySelector("form");
const message = form.querySelector("input[name='message']").value;

fetch("/message", {
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded",
    },
    body: `message=${message}`,
})
    .then((response) => 
    console.log(response)
    );
    // .then((response) => 
    //     response.text())
    // .then((text) => {
    //     console.log(text);
    // });
