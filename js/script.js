let randomNumber = Math.random() * 20
randomNumber = Math.floor(randomNumber)


while(true){
    const userNumber = prompt(' لطفا یک عدد وارد کنید بین ۱ تا ۲۰')
    if (userNumber == randomNumber){
        alert('باریکلا')
        break
    }
    else if (userNumber < randomNumber){
        alert('بزرگتر')
    }
    else{
        alert('کوچکتر')
    }
}

document.write('sghl')