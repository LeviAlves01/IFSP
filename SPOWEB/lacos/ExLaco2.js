//exemplo laço continue

let cont = 0;

while(cont<=10){
    cont++;

    if(cont % 2 == 0){
        continue;
    }

    console.log(cont); 
}