var ano = document.getElementById('Ano')
var sexo = document.getElementsByName('sexo')
var verificar = document.getElementById('verificar')
var anoAtual = new Date()
var Atual = anoAtual.getFullYear()
var mostrar = document.getElementById('mostrar')

verificar.addEventListener('click', verificarIdade)

function verificarIdade() {
    var anoA = parseInt(ano.value)
    var selectedSexo = ""

    if (anoA > Atual || anoA < 1920){
        window.alert('[ERRO] Verique seu ano de nascimento')
        return
    }

    for (var i = 0; i < sexo.length; i++) {
        if (sexo[i].checked) {
            selectedSexo = sexo[i].value
        }
    }

    if (selectedSexo === "") {
        window.alert('Selecione o sexo')
        return
    }

    var idade = Atual - anoA

    switch (selectedSexo){
        case 'M':
            if (idade < 18) {
                mostrar.innerHTML = `<p>Detectamos que você é Homem com ${idade} anos!</p> <img src=''>`
            } else if (idade >= 18) {
                mostrar.innerHTML = `<p>Detectamos que você é Homem com ${idade} anos!</p> <img src=''>`
            } else if (idade > 50){ 
                mostrar.innerHTML = `<p>Detectamos que você é Homem com ${idade} anos!</p> <img src=''>`
            }
        break
        case 'F':
            if (idade < 18) {
                mostrar.innerHTML = `<p>Detectamos que você é Mulher com ${idade} anos!</p> <img src=''>`
            } else if (idade >= 18) {
                mostrar.innerHTML = `<p>Detectamos que você é Mulher com ${idade} anos!</p> <img src=''>`
            } else if (idade > 50){ 
                mostrar.innerHTML = `<p>Detectamos que você é Mulher com ${idade} anos!</p> <img src=''>`
            }
        break
    }
}


