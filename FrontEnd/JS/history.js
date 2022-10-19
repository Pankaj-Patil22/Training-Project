console.log("You have connected...");

const user_id = 1

function padTo2Digits(num) {
    return num.toString().padStart(2, '0');
  }

function convertMsToTime(milliseconds) {
    let seconds = Math.floor(milliseconds / 1000);
    let minutes = Math.floor(seconds / 60);
    let hours = Math.floor(minutes / 60);
  
    seconds = seconds % 60;
    minutes = minutes % 60;
  
    return `${padTo2Digits(hours)}:${padTo2Digits(minutes)}:${padTo2Digits(
      seconds,
    )}`;
  }

async function fetchTransactionData() {
    let url = "http://127.0.0.1:5000/getSuccessfullTransactions/" + user_id;
    try {
      let res = await fetch(url);
      return await res.json();
    } catch (error) {
      console.log(error);
    }
  }

async function renderRaj() {
    transactionData = await fetchTransactionData();
    console.log(transactionData);
    for (let transaction of transactionData) {
        let div = document.createElement("div");
        div.classList.add("justify-content-center", "card", "gy-5")
        div.setAttribute('style','max-width: 60%; text-align: center;')
        div.setAttribute("id", "trans-" + transaction.id);
 
        let h5 = document.createElement("h5");
        h5.setAttribute("class", "card-title");
        var d1 = new Date(); //"now"
        var d2 = new Date(transaction.created);  // some date
        diff = convertMsToTime(Math.abs(d1-d2))

        h5.innerText = transaction.created;
        div.appendChild(h5);

        let p = document.createElement("p");
        p.setAttribute("class", "card-text");
        p.innerHTML = "<strong>Table Price: </Strong>" + transaction.table_total + "<strong> Order Price: </strong>" + transaction.order_total;
        div.appendChild(p);

        let timePeriodDiv = document.createElement("div");
        timePeriodDiv.setAttribute("style","text-align:right;")
        timePeriodDiv.classList.add("justify-content-center")
        timePeriodDiv.innerHTML = "<strong>Placed </strong><p>" + diff + " ago</p>"
        div.appendChild(timePeriodDiv)

        let button = document.createElement("button");
            button.setAttribute("class", "btn btn-dark");
            button.setAttribute('style','width: 10%; position:relative')
            button.addEventListener("click", () => {
                localStorage.setItem("order_id", transaction.order_id);
                console.log("order_id: " + transaction.order_id);
                console.log("transaction_id: " + transaction.transaction_id);
                localStorage.setItem("transaction_id", transaction.transaction_id);
                window.location.href = "feedback.html";
            });
        
        if (transaction.feedback_id == null) {
            button.innerText = "Give Feedback"
            button.setAttribute("class", "btn btn-dark");
              
        } else {
            button.innerText = "View Feedback"
            localStorage.setItem("feedback_id", transaction.feedback_id);
            button.setAttribute("class", "btn btn-primary");
        }


        let buttonDiv = document.createElement("div");
        buttonDiv.classList.add("row", "justify-content-center")
        buttonDiv.appendChild(button)
        div.appendChild(buttonDiv);
        document.getElementById("history").appendChild(div);
    }    
}

renderRaj();

