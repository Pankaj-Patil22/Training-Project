console.log('You have connected...')

yourGlobalVariable=[]
seatPrices= {
    1:500,
    2:1000,
    3:500
}

console.log(seatPrices[2])

function handleChange(checkbox) {
    if(checkbox.checked == true){
        yourGlobalVariable.push(checkbox.id)
        // document.getElementById("submit").removeAttribute("disabled");
    }else{
        yourGlobalVariable = yourGlobalVariable.filter(item => item !== checkbox.id)
        // document.getElementById("submit").setAttribute("disabled", "disabled");
   }
   if(yourGlobalVariable.length != 0){
        document.getElementById("tableInfo").innerText = "Table No. Selected: "+yourGlobalVariable
        document.getElementById("totalPriceInfo").innerText="Base Price: "+Baseprice
   }
   else{
    document.getElementById("tableInfo").innerText="No tables selected!"
    document.getElementById("totalPriceInfoo").innerText=""
   }
}

function getAvailableTables(){
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; //January is 0!
    var yyyy = today.getFullYear();
    var hour = today.getHours();

    if (dd < 10) {
        dd = '0' + dd;
    }

    if (mm < 10) {
        mm = '0' + mm;
    } 
    
    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById('datefield').value = today;

    console.log(hour+1)
    fetch("http://127.0.0.1:5000/tables/"+yyyy+"/"+mm+"/"+dd+"/11")
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

function getDateMin(){
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; //January is 0!
    var yyyy = today.getFullYear();

    if (dd < 10) {
        dd = '0' + dd;
    }

    if (mm < 10) {
        mm = '0' + mm;
    } 
    
    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById("datefield").setAttribute("min", today);
}

function getAvailableTimmings(){
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; //January is 0!
    var yyyy = today.getFullYear();
    var hour = today.getHours();

    if (dd < 10) {
        dd = '0' + dd;
    }

    if (mm < 10) {
        mm = '0' + mm;
    } 
    
    today = yyyy + '-' + mm + '-' + dd;

    const notes = document.querySelectorAll('.time');

    if(document.getElementById("datefield").value == today){
        notes.forEach((note) => {
            if(hour < note.classList[1]){
                document.getElementById("time-"+note.classList[1]).removeAttribute('disabled','')
            }
            else if(hour >= note.classList[1]){
                document.getElementById("time-"+note.classList[1]).setAttribute('disabled','')
            }
        });
    }
    else{
        notes.forEach((note) => {
            document.getElementById("time-"+note.classList[1]).removeAttribute('disabled','')
        });
    }
    console.log(document.getElementById("datefield").value)
}