const readline = require('readline');

const r1 = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

r1.question('Digite um número para ser feito a tabuada:', (num_str) => {
    const num = parseInt(num_str);

    for(let i=1;i<=10;i++) {
    const multiplicacao=num*i;
    console.log(num + ' x ' + i + ' = ' + multiplicacao);
}

    r1.close();
});