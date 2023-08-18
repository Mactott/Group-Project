
const signIn = () =>
{
    fetch('/request')
        .then(response => response.text())
        .then(data =>
        {
            const modalDiv = document.createElement('div');
            modalDiv.id = "logginDiv";
            modalDiv.innerHTML = data;
            document.body.appendChild(modalDiv);
            $("#optionModal").modal('show');
            $("#optionModal").on('hidden.bs.modal', function (e)
            {
                modalDiv.remove();
            });
        });
};

const byCity = () =>
{
    fetch('/bycity')
        .then(response => response.text())
        .then(data =>
        {
            const page = document.getElementById('page')
            page.innerHTML = data
        });
};



function switchFormR ()
{
    fetch('/switchR')
        .then(response => response.text())
        .then(data =>
        {
            const toSwitch = document.getElementById('to-switch');
            toSwitch.innerHTML = data;
            const title = document.getElementById("optionModalLabel");
            title.innerText = "Register";
            const register = document.getElementById('register');
            register.addEventListener('submit', function (e)
            {
                e.preventDefault();
                formData = new FormData(e.target);
                console.log(formData);
            });
        });
}

function switchFormS ()
{
    fetch('/switchS')
        .then(response => response.text())
        .then(data =>
        {
            const toSwitch = document.getElementById('to-switch');
            toSwitch.innerHTML = data;
            const title = document.getElementById("optionModalLabel");
            title.innerText = "Sign in";
        });
}

