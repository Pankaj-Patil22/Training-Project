console.log("You have connected...");

yourGlobalVariable = [];

tablePrices = {};

tableSessions = {};

async function getTablePrices() {
  await fetch("http://127.0.0.1:5000/getTablePrices")
    .then((Response) => Response.json())
    .then((data) => {
      console.log(data);
      localStorage.setItem("tablePrices", JSON.stringify(data));
      tablePrices = data;
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
  if (checkbox.checked == true) {
    yourGlobalVariable.push(checkbox.id);
    // document.getElementById("submit").removeAttribute("disabled");
  } else {
    yourGlobalVariable = yourGlobalVariable.filter(
      (item) => item !== checkbox.id
    );
    // document.getElementById("submit").setAttribute("disabled", "disabled");
  }

  console.log(yourGlobalVariable, "this is the data generation");
  localStorage.setItem("choosentables", JSON.stringify(yourGlobalVariable));
  totalPrice = 0;
    yourGlobalVariable.forEach((element) => {
        totalPrice += tablePrices[element];
    });
  localStorage.setItem("totalPriceOfTable", totalPrice);
  
  if (yourGlobalVariable.length != 0) {
  }
}

function getAvailableTables() {
  var url = new URL("http://127.0.0.1:5000/Tables");
  if (localStorage.getItem("choosenTimeSlot") == null || localStorage.getItem("choosenDate") == null){
    return;
  }
  url.searchParams.append("choosenTimeSlot", localStorage.getItem("choosenTimeSlot"));
  url.searchParams.append("choosenDate", localStorage.getItem("choosenDate"));
  console.log(url);
  fetch(url)
    .then((Response) => Response.json())
    .then((data) => {
      console.log(data);
      Object.entries(data.table_reservation).forEach(([key, value]) => {
        if (value == 0) {
          document.querySelector("." + key).removeAttribute("disabled", "");
        } else if (value == 1) {
          document.querySelector("." + key).setAttribute("disabled", "");
        }
      });
    });
}

function getDateMin() {
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth() + 1; //January is 0!
  var yyyy = today.getFullYear();

  if (dd < 10) {
    dd = "0" + dd;
  }

  if (mm < 10) {
    mm = "0" + mm;
  }

  today = yyyy + "-" + mm + "-" + dd;
  document.getElementById(" ").setAttribute("min", today);
}

function getAvailableTimmings() {
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth() + 1; //January is 0!
  var yyyy = today.getFullYear();
  var hour = today.getHours();

  if (dd < 10) {
    dd = "0" + dd;
  }

  if (mm < 10) {
    mm = "0" + mm;
  }

  today = yyyy + "-" + mm + "-" + dd;

  const notes = document.querySelectorAll(".time");

  if (document.getElementById("datefield").value == today) {
    console.log("today");
    notes.forEach((note) => {
      if (hour < note.classList[1]) {
        document
          .getElementById("time-" + note.classList[1])
          .removeAttribute("disabled", "");
      } else if (hour >= note.classList[1]) {
        document
          .getElementById("time-" + note.classList[1])
          .setAttribute("disabled", "");
      }
    });
  } else {
    console.log("not today");
    notes.forEach((note) => {
      document
        .getElementById("time-" + note.classList[1])
        .removeAttribute("disabled", "");
    });
  }

  localStorage.setItem(
    "choosenDate",
    document.getElementById("datefield").value
  );
  getAvailableTables();
  console.log("choosen date", localStorage.getItem("choosenDate"));
}

function changeTimeSlot() {
  localStorage.setItem(
    "choosenTimeSlot",
    document.getElementById("timeSlots").value
  );
  localStorage.setItem(
    "choosenTimeSlotTime",
    tableSessions[document.getElementById("timeSlots").value]
    );
  console.log("choosen time slot", localStorage.getItem("choosenTimeSlot"));
  getAvailableTables();
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
