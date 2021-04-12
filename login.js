const form = document.querySelector('.input-group');


// youtube JavaScript Fetch API (Async JavaScript)
form.addEventListener('submit', e => {

    e.preventDefault();

    console.log(form.email.value);
    console.log(form.password.value);

    let payload = {
        email : form.email.value,
        password : form.password.value
    }

    const URL = "https://team-um6.herokuapp.com/auth";

    fetch(URL, {
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
            "Content-Type" : " application/json"
        }
    })
    .then(response => response.json())
    .then(data =>  {
        console.log(data);
        sessionStorage.setItem('access_token', data.access_token);
       // str = JSON.stringify(data);
        str = JSON.stringify(data, null, 4); // (Optional) beautiful indented output.
        console.log(str); // Logs output to dev tools console.
        alert(str); 
    })
    .catch(err => console.log(err));


});
