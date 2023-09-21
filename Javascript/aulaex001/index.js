var mostrarHora = document.getElementById('hora')
var dataAtual = new Date()
var hora = dataAtual.getHours()

function horario(mostrarHora,hora) {
    // Mostrar Manhã
    if (hora > 6 && hora < 12) {
        mostrarHora.innerHTML = `<h2>Agora são ${hora} horas.</h2> <img src="Amanhecer01.jpg">`
        mostrarHora.innerHTML += `<p>Bom dia!</p>`
        document.body.style.backgroundColor = 'burlywood'
    // Mostrar Tarde
    } else if (hora => 12 && hora < 18) {
        mostrarHora.innerHTML = `<h2>Agora são ${hora} horas</h2> <img src="sunset-1688849_640.jpg">`
        mostrarHora.innerHTML += `<p>Boa Tarde!</p>`
        document.body.style.backgroundColor = 'lightsalmon'
    // Mostrar Noite
    } else {
        mostrarHora.innerHTML = `<h2>Agora são ${hora} horas</h2> <img src="depositphotos_32109269-stock-photo-moon-and-clouds-in-the.jpg">`
        mostrarHora.innerHTML += `<p>Bom Noite!</p>`
        document.body.style.backgroundColor = 'dimgray'
    }
}

horario(mostrarHora, hora)