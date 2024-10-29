
function formSubmit(e) {
    e.preventDefault()

    const name1 = document.getElementById("name1").value
    const name2 = document.getElementById("name2").value
    const name3 = document.getElementById("name3").value
    const phone = document.getElementById("phone").value
    const message = document.getElementById("message").value

    const messageObj = {
        name1,
        name2,
        name3,
        phone,
        message
    }
    console.log(messageObj)

    const $form = document.getElementById("mainForm")
    $form.reset()
}

const $form = document.getElementById("mainForm")
$form.addEventListener("submit", (e) => formSubmit(e))