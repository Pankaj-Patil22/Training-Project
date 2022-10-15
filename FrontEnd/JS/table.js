console.log("You have connected...");

yourGlobalVariable = [];

tablePrices = {};

tableSessions = {
};

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

function updateTable(date, timeslot) {
  // considering date is given in format yyyy-mm-dd
  dateArr = date.split("-");
  url =
    "http://127.0.0.1:5000/tables/" +
    dateArr[0] +
    "/" +
    dateArr[1] +
    "/" +
    dateArr[2] +
    "/" +
    timeslot;
  console.log("fetching url", url);
  fetch(url)
    .then((Response) => Response.json())
    .then((data) => {
      console.log("inside date change", data);
      Object.entries(data.table_reservation).forEach(([key, value]) => {
        if (value == 1) {
          document.querySelector("." + key).removeAttribute("disabled", "");
          console.log("inside date change remove disabled", key);
        } else if (value == 0) {
          document.querySelector("." + key).setAttribute("disabled", "");
          console.log("inside date change set disabled", key);
        }
      });
    });
}

function getDateInFormat(date) {
  var dd = date.getDate();
  var mm = date.getMonth() + 1; //January is 0!
  var yyyy = date.getFullYear();
  if (dd < 10) {
    dd = "0" + dd;
  }
  if (mm < 10) {
    mm = "0" + mm;
  }

  return yyyy + "-" + mm + "-" + dd;
}

function handleChange(checkbox) {
  totalPrice = 0;
  if (checkbox.checked == true) {
    yourGlobalVariable.push(checkbox.id);
  } else {
    yourGlobalVariable = yourGlobalVariable.filter(
      (item) => item !== checkbox.id
    );
  }
  if (yourGlobalVariable.length != 0) {
    console.log(yourGlobalVariable, "this is the data generation");
    localStorage.setItem("choosentables", JSON.stringify(yourGlobalVariable));
    yourGlobalVariable.forEach((element) => {
      totalPrice += tablePrices[element - 1];
      document.getElementById("totalPriceInfo").innerText =
        "Total Amount: " + totalPrice;
      localStorage.setItem("totalPriceOfTable", totalPrice);
    });
    document.getElementById("tableInfo").innerText =
      "Table No. Selected: " + yourGlobalVariable;
    document.getElementById("tableSubmit").removeAttribute("disabled", "");
  } else {
    document.getElementById("tableInfo").innerText = "No tables selected!";
    document.getElementById("totalPriceInfo").innerText = "";
    document.getElementById("tableSubmit").setAttribute("disabled", "");
  }
}

function updateData() {
  localStorage.setItem(
    "choosenDate",
    document.getElementById("datefield").value
  );
  console.log("choosen date", localStorage.getItem("choosenDate"));

  localStorage.setItem(
    "choosenTimeSlot",
    document.getElementById("selectTS").value
  );
  console.log(
    "choosen time slot id",
    localStorage.getItem("choosenTimeSlotTime")
  );

  localStorage.setItem(
    "choosenTimeSlotTime",
    tableSessions[document.getElementById("selectTS").value]
  );
  console.log("choosen time slot ", localStorage.getItem("choosenTimeSlot"));

  updateTable(
    document.getElementById("datefield").value,
    document.getElementById("selectTS").value
  );
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

let date = new Date();
document.getElementById("datefield").value =
  date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate();

document
  .getElementById("datefield")
  .setAttribute(
    "min",
    date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate()
  );


getTablePrices();
getTableSessions();
updateData();