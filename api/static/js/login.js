const form = document.querySelector('.input-group');

const performUserLogin = async(payload) => {

    let response = await fetch ('/auth', {
        method: "POST",
        body: JSON.stringify(payload),
        headers: {
            "Content-Type" : " application/json"
        }
    });

    const data = await response.json();

    if (data.status_code != 401) {
        // store access token
        sessionStorage.setItem('access_token', data.access_token);

        // get user profile
        let response = await fetch('/user/profile', {
            method: "GET",                
            headers: {"Authorization": `JWT ${sessionStorage.getItem('access_token')}`},
            redirect: 'follow',
        });

        if (response.ok) {
            const userProfile = await response.json();            
            sessionStorage.setItem('storeid', userProfile.store);

            window.location.replace('/home');
        }

    } else {
        alert(data.description);
    }
}

form.addEventListener('submit', e => {

    e.preventDefault();

    console.log(form.email.value);
    console.log(form.password.value);

    let payload = {
        email : form.email.value,
        password : form.password.value
    }

    performUserLogin(payload);
});
