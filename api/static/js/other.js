const body= document.getElementById('body');
const card= document.getElementById('card-body');

const sendHTTPRequest = (method, url, dta) => {
    const promise = new Promise ((resolve, reject ) => {

    const request =  new XMLHttpRequest();
        request.open(method, url);

        request.responseType= 'json';

        request.onload = () => {
           resolve(request.response);

        }
        request.send();

});

return  promise;



    }

const getData = () => {

    sendHTTPRequest ( 'GET' , "http://localhost:5000/food")
    .then(responseData =>{
     console.log (responseData);



    });
}



