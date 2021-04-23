const form = document.querySelector(#AddFood)

form.addEventListener('submit', e => {

    e.preventDefault();

    let payload = {
        name : from.name.value,
        quantity : from.quantity.value,
        calories : from.calories.value,
        expiration : from.expiration.value,
        //get store id ?
        store : data.record.id 

    }


    fetch('/food', {
        method 'POST',
        body: JSON.stringify(payload),
        headers: {
            "Content-Type" : " application/json",
        }
    })
    .then(response => response.json())
    .then(data => {
        alert ('Food creation completed.');
        window.location.replace('/');
    })
    /catch

})