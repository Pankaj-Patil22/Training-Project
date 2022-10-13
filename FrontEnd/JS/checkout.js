import Routes from "./routes.js";

async function renderSummary() {
  console.log(localStorage.getItem("item_placed"));
  console.log(localStorage.getItem("firstname"));
  console.log(localStorage.getItem("firstname12"));
  let transData = localStorage.getItem("item_placed");
  let summary = document.getElementById("summary");


  let table_number = document.createElement("p");
  table_number.innerHTML = "Table Number: " + localStorage.getItem("choosentables");
  summary.appendChild(table_number);
  let table_time_slot = document.createElement("p");
  table_time_slot.innerHTML = "Time Slot: " + localStorage.getItem("choosenTimeSlotTime");
  summary.appendChild(table_time_slot);
  let table_date = document.createElement("p");
  table_date.innerHTML = "Date: " + localStorage.getItem("choosenDate");
  summary.appendChild(table_date);
  let table_total_price = document.createElement("p");
  table_total_price.innerHTML = "Totatl Table Price: " + localStorage.getItem("totalPriceOfTable");
  summary.appendChild(table_total_price);


  console.log(transData);
  console.log(Object.values(transData));
  // convert a json text to a js object
  let a = JSON.parse(transData);
  console.log(a);
  transData = JSON.parse(transData);
  let items_ordered = document.createElement("div");
  let totalDishesPrice = 0;
  Object.values(transData).forEach((element) => {
    let item = document.createElement("p");
    item.innerHTML =
      "Item Name: " +
      element.name +
      " Quantity: " +
      element.quantity +
      " Price: " +
      element.price +
      " Total Price: " +
      element.quantity +
      " X " +
      element.price +
      " = " +
      element.totalPrice;
      totalDishesPrice += parseInt(element.totalPrice);
    items_ordered.appendChild(item);
    
  });
  summary.appendChild(items_ordered);
  localStorage.setItem("totalDishesPrice", totalDishesPrice);
  let totalPrice = document.createElement("p");
  totalPrice.innerHTML = "Total Price: " + (parseInt(localStorage.getItem("totalDishesPrice")) + parseInt(localStorage.getItem("totalPriceOfTable")));
  summary.appendChild(totalPrice);
}

async function postData(url = "", data = {}) {
  // Default options are marked with *
  console.log(Routes.transactionData)
  let responseJson = ''
  const response = await fetch(Routes.transactionData, {
    method: "POST",
    mode: "cors",
    credentials: "omit",
    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
      responseJson =  data;
      if (data == "success") {
        console.log("success Boss");
        localStorage.clear();
        window.location.href = "status.html";
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      console.log("Error:");
    });
  // return response.json(); // parses JSON response into native JavaScript objects
  return responseJson;
}

document.getElementById("payBtn").addEventListener("click", () => {
  
  postData(Routes.transactionData, makeThePostData()).then(
    (data) => {
      console.log(data); // JSON data parsed by `data.json()` call
    }
  );
});

document.getElementById("tempBtn").addEventListener("click", () => {
  console.log(localStorage.getItem("item_placed"));
  let dataToPost = makeThePostData();
  console.log("the dataToPost",dataToPost);
});

function makeThePostData() {
  let dataToPost = {
    items: Object.values(JSON.parse(localStorage.getItem("item_placed"))),
    table_number: localStorage.getItem("choosentables"),
    table_time_slot: localStorage.getItem("choosenTimeSlotTime"),
    table_time_slot_id: localStorage.getItem("choosenTimeSlot"),
    table_date: localStorage.getItem("choosenDate"),
    table_total_price: localStorage.getItem("totalPriceOfTable"),
    total_dishes_price: localStorage.getItem("totalDishesPrice"),
  }
  return dataToPost;
}

renderSummary();
