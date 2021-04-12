const form = document.querySelector('.input-group');
const form1 = document.querySelector('.input-group1');
form1.addEventListener('submit', f => {

    f.preventDefault();
    console.log(form1.email.value);
    console.log(form1.password.value);
    console.log(form1.store.value);
    let payload1 = {
        email : form1.email.value,
        password : form1.password.value,
        store :form1.store.value,
    }
        const URL = "https://team-um6.herokuapp.com/register";

    fetch(URL, {
        method: "POST",
        body: JSON.stringify(payload1),
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
    .catch(err1 => console.log(err1));
})

// youtube JavaScript Fetch API (Async JavaScript)
form.addEventListener('submit', e => {

    e.preventDefault();

    console.log(form.name.value);
    console.log(form.phone.value);
    console.log(form.street.value);
    console.log(form.city.value);
    console.log(form.state.value);
    console.log(form.zipcode.value);
    console.log(form.open.value);
    console.log(form.close.value);

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