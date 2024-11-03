const url ='http://localhost:8888/submit'

async function sentData(data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),  
        });

        if (!response.ok) {
            throw new Error('Network response was not ok: ' + response.statusText);
        }

        const res = await response.text();
        console.log('Добавленное обращение:', res);
        return res
    } catch (error) {
        console.error('Произошла ошибка при добавлении обращения:', error);
    }
}

async function formSubmit(e) {
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
    await sentData(messageObj)

    const $form = document.getElementById("mainForm")
    $form.reset()
}

const $form = document.getElementById("mainForm")
$form.addEventListener("submit", (e) => formSubmit(e))