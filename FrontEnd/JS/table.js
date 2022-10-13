console.log('You have connected...')
yourGlobalVariable=[]

function handleChange(checkbox) {
    totalPrice = 0;
    if(checkbox.checked == true){
        yourGlobalVariable.push(checkbox.id)
        // document.getElementById("submit").removeAttribute("disabled");
    }else{
        yourGlobalVariable = yourGlobalVariable.filter(item => item !== checkbox.id)
        // document.getElementById("submit").setAttribute("disabled", "disabled");
   }
   if(yourGlobalVariable.length != 0){
        yourGlobalVariable.forEach((element) => {
            fetch("http://127.0.0.1:5000/tables/price")
    .then(Response => Response.json())
    .then(data => {
        totalPrice += data.prices[element -1]
        document.getElementById("totalPriceInfo").innerText="Total Amount: "+totalPrice
        prices = totalPrice
    })
        })
        document.getElementById("tableInfo").innerText = "Table No. Selected: "+yourGlobalVariable
   }
   else{
    document.getElementById("tableInfo").innerText="No tables selected!"
    document.getElementById("totalPriceInfo").innerText=""
   }
}

function getAvailableTables(){
    document.getElementById("tableInfo").innerText="No tables selected!"
    document.getElementById("totalPriceInfo").innerText=""

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
    getAvailableTimmings()

    if(hour >= 8 && hour <= 20){
        document.getElementById("datefield").setAttribute("min", today);
        fetch("http://127.0.0.1:5000/tables/"+yyyy+"/"+mm+"/"+dd+"/"+(hour-7))
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
if(hour<8)
{
    fetch("http://127.0.0.1:5000/tables/"+yyyy+"/"+mm+"/"+dd+"/1")
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
if(hour>20)
{
    var day = new Date();
    var nextDay = new Date(day);
    nextDay.setDate(day.getDate() + 1);

    passNextdayDD = nextDay.getDate()
    passNextdayMM =nextDay.getMonth() + 1

    if (passNextdayDD < 10) {
        passNextdayDD = '0' + passNextdayDD;
    }

    if (passNextdayMM < 10) {
        passNextdayMM = '0' + passNextdayMM;
    } 

    passNextDay = nextDay.getFullYear() + '-' + passNextdayMM + '-' + passNextdayDD
    document.getElementById("datefield").setAttribute("min", passNextDay);
    document.getElementById('datefield').value = passNextDay
    getAvailableTimmings()

    fetch("http://127.0.0.1:5000/tables/"+nextDay.getFullYear()+"/"+nextDay.getMonth()+"/"+nextDay.getDate()+"/1")
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

    for (let note of notes){
        if(document.getElementById("time-"+note.classList[1]).disabled == false){
            document.getElementById("selectTS").value = document.getElementById("time-"+note.classList[1]).value;
            break;
        } 
        else{
            document.getElementById("selectTS").value = "--"
        }
    }
}