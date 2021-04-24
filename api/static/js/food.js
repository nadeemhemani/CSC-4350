const form = document.querySelector('#Food List')

id = sessionStorage.getItem('storeid')
 const getFoods = () => {
    fetch('/foods/' + id, {
       method : 'GET',
       headers: {"Authorization": `JWT ${sessionStorage.getItem('access_token')}`},
    })
    .then(response => response.json())
    .then(foods => {
      const tBody =  document.querySelector('#tableBody')
      let html = '<tBody>'

       foods.foods.forEach(item => {
          html += `
          <tr>
            <th scope="row">${item.name}</th>
            <td>${item.quantity}</td>
            <td>${item.calories}</td>
            <td>${new Date(item.expiration).toLocaleDateString()}</td>
         </tr>`          
       })
       html += '</tBody>'
       tBody.innerHTML = html
    })
 }

 getFoods()





