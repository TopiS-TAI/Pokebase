document.body.addEventListener('htmx:configRequest', (e) => {
    console.log(e)
    if (e.target.id === 'cell-add') {
        const types = ['name', 'hp', 'attack', 'defense', 's_attack', 's_defense', 'speed']
        for (const type of types) {
            e.detail.parameters[type] = document.getElementById('cell-' + type).innerHTML
        }
        e.detail.parameters.type1 = document.getElementById('type1').value
        e.detail.parameters.type2 = document.getElementById('type2').value
    }
})

document.body.addEventListener('clearForm', (e) => {
    console.log(e)
    const elems = []
    const types = ['name', 'hp', 'attack', 'defense', 's_attack', 's_defense', 'speed']
    for (const type of types) {
        elems.push(document.getElementById('cell-' + type))
    }
    for (const el of elems) {
        el.innerHTML = ''
    }
})

function validateNumbers(e) {
    console.log(e)
    if (
        e.code.slice(0, -1) !== 'Digit' ||
        e.target.innerHTML.length === 3
    ) {
        e.preventDefault()
    }
}

function validateText(e) {
    console.log(e)
    const acceptedKeys = ['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Backspace']
    if (
        e.type === 'keydown' &&
        !acceptedKeys.includes(e.key) &&
        e.target.innerHTML.length > 63
    ) {
        e.preventDefault()
    } else if (e.type === 'paste') {
        const data = e.clipboardData.getData('text')
        const overflow = (e.target.innerHTML.length + data.length) - 64
        if (overflow > 0) {
            e.preventDefault()
            newData = data.slice(0, -overflow)
            e.target.innerHTML += newData
        }
    }
}