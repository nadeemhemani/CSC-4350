const body= document.body
const card= document.card


const sendHTTPRequest = (method, url, dta) => {
 return fetch (url, {
     method:method, 
     body:JSON.stringify(data),
     headers: data ? {'Content-Type': 'application/json'} :  {}
 }) .then(response => {
    if (response.status >= 400) {
        response.json().then(errorResponse =>{
            const error = new Error('not correct');
            error.data= errorResponse; 
            throw error;
        });
    }

        return response.json(); 
    });
}


fetch('/400').then(function(response) {
    if (response.status === 400) {
      return response.json()
    }
  }).then(function(object) {
    console.log(object.type, object.message)
  })




const getData = ()  => {
    sendHTTPRequest ( 'GET' , "http://localhost:5000/foods/1 HTTP/1.1")
    .then(responseData =>{
     console.log (responseData);


    })
}


const sendData = ()  => {
    sendHTTPRequest ( 'GET' , "http://localhost:5000/foods/1 HTTP/1.1")
    .then(responseData =>{
     console.log (responseData);

    })
    .catch (err => { 
        console.log (err);
    });
};
