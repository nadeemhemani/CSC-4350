const form = document.querySelector('#StoreRegistration');

form.addEventListener('submit', e => {

    e.preventDefault();

    let payload = {
        name : form.name.value,
        phone : form.phone.value,
        street :form.street.value,
        city :form.city.value,
        state :form.state.value,
        zipcode :form.zipcode.value,
        open : form.open.value,
        close : form.close.value,    
    }

    fetch('/store', {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            "Content-Type" : " application/json",
        }
    })
    .then(response => response.json())
    .then(data => {
        let payload = {
            password: form.password.value,
            email: form.email.value,
            store : data.record.id        
        }

        fetch('/register', {
            method: 'POST',
            body: JSON.stringify(payload),
            headers: {
                "Content-Type" : " application/json",
            }
        })
        .then(response => response.json())
        .then(data => {
            alert ('Store creation completed. Please peform the login now');
            window.location.replace('/');
        })
        .catch(err => console.log(err));

    })
    .catch(err => console.log(err));



/*
    const URL = "http://team-um6.herokuapp.com/store";

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
        str = JSON.stringify(data);
str = JSON.stringify(data, null, 4); // (Optional) beautiful indented output.
console.log(str); // Logs output to dev tools console.
alert(str); 
       // sessionStorage.setItem('access_token', data.access_token);
       
    })
    .catch(err => console.log(err));
    */


});




var x = document.getElementById("StoreRegistration");
      var y = document.getElementById("UserRegistration");
      var z = document.getElementById("btn");
     

      function user(){
          x.style.left = "-2000px";
          y.style.left = "65px";
          z.style.left = "170px";
         
        }
        function store(){
          x.style.left = "65px";
          y.style.left = "490px";
          z.style.left = "0px";
          
        }