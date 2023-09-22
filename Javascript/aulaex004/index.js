var num = document.getElementById('numero')
var tabuada = document.getElementById('button')
var dados = document.getElementById('dados')

function fazerTabuada() {
    var numero = parseInt(num.value)

    dados.getElementsByTagName('tbody')[0].innerHTML = ""

    if (isNaN(numero)){
        alert('Insira um número válido!')
        return
    }

    for (var i = 1; i <= 10;i++) {
        var resul = numero * i
        var linha = document.createElement('tr')
        var coluna = document.createElement('td')
        coluna.style.textAlign = 'center'
        coluna.textContent = `${numero} x ${i} = ${resul}`
        linha.appendChild(coluna)
        dados.getElementsByTagName('tbody')[0].appendChild(linha)
    }
}

tabuada.addEventListener('click', fazerTabuada)

