const form = document.querySelector('#AddFood');

form.addEventListener('submit', e => {

    e.preventDefault();

    let payload = {
        name : form.name.value,
        quantity : form.quantity.value,
        calories : form.calories.value,
        expiration : form.expiration.value,
        //get store id ?
        store : sessionStorage.getItem('storeid')

    }


    fetch('/food', {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            "Content-Type" : " application/json",
        }
    })
    .then(response => response.json())
    .then(data => {
        alert ('Food creation completed');
        window.location.replace('/add_food');
    })
    .catch(err => console.log(err));
})

var x = document.getElementById("AddFood");
      var y = document.getElementById("btn");