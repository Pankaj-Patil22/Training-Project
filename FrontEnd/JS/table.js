console.log('You have connected...')

yourGlobalVariable=[]

function handleChange(checkbox) {
    if(checkbox.checked == true){
        yourGlobalVariable.push(checkbox.id)
        // document.getElementById("submit").removeAttribute("disabled");
    }else{
        yourGlobalVariable = yourGlobalVariable.filter(item => item !== checkbox.id)
        // document.getElementById("submit").setAttribute("disabled", "disabled");
   }
   console.log(yourGlobalVariable)
}

function getAvailableTables(){
    fetch("http://127.0.0.1:5000/Tables")
    .then(Response => Response.json())
    .then(data => {
        // data.table_reservation.forEach(element => {
        //     console.log(element)
        // });
        Object.entries(data.table_reservation).forEach(([key,value]) => {  
         if (value == 1){
            document.querySelector("."+key).removeAttribute('disabled','')
         }
         else if(value ==0){
            document.querySelector("."+key).setAttribute('disabled','')
         }
        })
    })
}