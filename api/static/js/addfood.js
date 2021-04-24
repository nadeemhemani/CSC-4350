const form = document.querySelector('#AddFood');

form.addEventListener('submit', e => {

    e.preventDefault();

    let payload = {
        name : form.name.value,
        quantity : form.quantity.value,
        calories : form.calories.value,
        expiration : new Date(form.expiration.value).toLocaleDateString(),
        //get store id ?
        store : sessionStorage.getItem('storeid')

    }
    console.log(payload)


    fetch('/food', {
        method: 'POST',
        body: JSON.stringify(payload),
        headers: {
            "Content-Type" : " application/json",
        }
    })
    .then(response => response.json())
    .then(data => {
        
        window.location.replace('/food_management');
    })
    .catch(err => console.log(err));
})

var x = document.getElementById("AddFood");
      var y = document.getElementById("btn");