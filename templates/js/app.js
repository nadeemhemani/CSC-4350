/*
GET http://localhost:5000/consumer/33.748783/-84.388168/miles HTTP/1.1
Content-Type: application/json
*/

//const URL = "/consumer/33.748783/-84.388168/miles";
const form = document.querySelector('.registration');


// youtube JavaScript Fetch API (Async JavaScript)
form.addEventListener('submit', e => {

    e.preventDefault();

    console.log(form.username.value);
    console.log(form.password.value);

    let payload = {
        email : form.username.value,
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
    })
    .catch(err => console.log(err));


});

/*
    */

