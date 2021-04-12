document.addEventListener('DOMContentLoaded', () => {
    if (sessionStorage.getItem('access_token') === null) {
        window.location.replace('/');
    }
});

const logout = () => {
    sessionStorage.removeItem('access_token');
    sessionStorage.removeItem('storeid');
    window.location.replace('/');
}