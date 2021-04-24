const form = document.querySelector('#FoodList')

id : sessionStorage.getItemI('storeid')
 const getFoods = () => {
    fetch('/foods/' + id)
    .then(response => response.json())
    .then(foods => console.log(foods))
 }




