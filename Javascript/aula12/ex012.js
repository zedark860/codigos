var agora = new Date()
var hora = agora.getHours()
console.log(`Agora são ${hora} horas.`)
if (hora < 12){
    if (hora < 6){
        console.log('Boa madrugada')
    } else {
        console.log('Bom dia')
    }
} else if (hora <= 18){
    console.log('Boa Tarde')
} else {
    console.log('Boa noite')
}