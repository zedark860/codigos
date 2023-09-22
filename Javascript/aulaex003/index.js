var inicio = document.getElementById('inicio')
var fim = document.getElementById('Fim')
var passo = document.getElementById('Passo')
var contar = document.getElementById('Contar')
var mostrarContagem = document.getElementById('Contagem')

mostrarContagem.innerHTML = `<p>Preparando contagem...</p>`

function fazendoContagem() {
    var inicioN = parseInt(inicio.value)
    var fimN = parseInt(fim.value)
    var passoN = parseInt(passo.value)

    mostrarContagem.innerHTML = ""

    if (isNaN(inicioN) || isNaN(fimN) || isNaN(passoN) || passoN <= 0) {
        mostrarContagem.innerHTML = `<p>Por favor, insira valores válidos.</p>`
        return
    } else if (inicioN > fimN) {
        mostrarContagem.innerHTML = `<p>Por favor, Digite novamente uma contagem válida.</p>`
        return
    }

    mostrarContagem.innerHTML = `<p>Contando:</p>`

    for (var i = inicioN; i <= fimN; i+=passoN) {
        mostrarContagem.innerHTML += `${i}👉`
    }
    mostrarContagem.innerHTML += `🏁`
}

contar.addEventListener('click', fazendoContagem)
