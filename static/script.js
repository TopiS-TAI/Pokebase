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