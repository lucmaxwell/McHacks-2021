const fs = require('fs') 


export function myFunction(){
    var data = fs.readFileSync('testing.txt', 'utf8');
    data = data.toString(); 
    data = data.split('\n');
        //stringList.forEach(element => console.log(element))
    //console.log(data);
        //return stringList;
    return data;
}
//console.log(myFunction());





