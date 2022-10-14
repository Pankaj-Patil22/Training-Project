console.log('You have connected...')

yourGlobalVariable=[]

tablePrices = {};

tableSessions = {
  "1": "8-9",
  "2": "9-10",
  "3": "10-11",
  "4": "11-12",
  "5": "12-13",
  "6": "13-14",
  "7": "14-15",
  "8": "15-16",
  "9": "16-17",
  "10": "17-18",
  "11": "18-19",
  "12": "19-20"
}

async function getTablePrices() {
    await fetch("http://127.0.0.1:5000/tables/price")
      .then((Response) => Response.json())
      .then((data) => {
        console.log(data.prices);
        localStorage.setItem("tablePrices", JSON.stringify(data.prices));
        tablePrices = data.prices;
      });
    console.log(tablePrices);
}
  
async function getTableSessions() {
    await fetch("http://127.0.0.1:5000/getTableSessions")
      .then((Response) => Response.json())
      .then((data) => {
        console.log(data);
        localStorage.setItem("tableSessions", JSON.stringify(data));
        tableSessions = data;
      });
    console.log(tableSessions);
}

function handleChange(checkbox) {
    totalPrice = 0;
    if(checkbox.checked == true){
        yourGlobalVariable.push(checkbox.id)
    }else{
        yourGlobalVariable = yourGlobalVariable.filter(item => item !== checkbox.id)
   }
   if(yourGlobalVariable.length != 0){
        console.log(yourGlobalVariable, "this is the data generation");
        localStorage.setItem("choosentables", JSON.stringify(yourGlobalVariable));
        yourGlobalVariable.forEach((element) => {
            
            totalPrice += tablePrices[element -1]
            document.getElementById("totalPriceInfo").innerText="Total Amount: "+totalPrice
            localStorage.setItem("totalPriceOfTable", totalPrice);
        })
        document.getElementById("tableInfo").innerText = "Table No. Selected: "+yourGlobalVariable
        document.getElementById("tableSubmit").removeAttribute('disabled','')
   }
   else{
    document.getElementById("tableInfo").innerText="No tables selected!"
    document.getElementById("totalPriceInfo").innerText=""
    document.getElementById("tableSubmit").setAttribute('disabled','')
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

    if(hour<8){
        fetch("http://127.0.0.1:5000/tables/"+yyyy+"/"+mm+"/"+dd+"/1")
        .then(Response => Response.json())
        .then(data => {
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

    if(hour>20){
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

    localStorage.setItem("choosenDate", document.getElementById("datefield").value);
    console.log("choosen date", localStorage.getItem("choosenDate"));

    localStorage.setItem("choosenTimeSlot", document.getElementById("selectTS").value);
    console.log("choosen time slot id", localStorage.getItem("choosenTimeSlotTime"));

    localStorage.setItem("choosenTimeSlotTime", tableSessions[document.getElementById("selectTS").value]);
    console.log("choosen time slot ", localStorage.getItem("choosenTimeSlot"));
}

function changeTimeSlot() {
    localStorage.setItem("choosenTimeSlot", document.getElementById("selectTS").value);
    localStorage.setItem("choosenTimeSlotTime", tableSessions[document.getElementById("selectTS").value]);
    console.log("choosen time slot", localStorage.getItem("choosenTimeSlot"));
}

function proocedToMenu() {
    console.log("prooced to menu");
    console.log("choosenDate", localStorage.getItem("choosenDate"));
    console.log("choosenTimeSlot", localStorage.getItem("choosenTimeSlot"));
    console.log("choosentables", localStorage.getItem("choosentables"));
  
      // this doesnt work it takes by default the first date
    if (localStorage.getItem("choosenDate") == null) {
      alert("Please select a date");
      return;
    }
    
    // this doesnt work it takes by default the first time slot
    if (localStorage.getItem("choosenTimeSlot") == null) {
      alert("Please select a time slot");
      return;
    }
    if (
      localStorage.getItem("choosentables") == null ||
      localStorage.getItem("choosentables") == "[]"
    ) {
      alert("Please select a table");
      return;
    }
    window.location.href = "menu.html";
}

getTablePrices();
getTableSessions();