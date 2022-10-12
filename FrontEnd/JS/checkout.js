import Routes from "./routes.js";

async function renderSummary() {
  console.log(localStorage.getItem("item_placed"));
  console.log(localStorage.getItem("firstname"));
  console.log(localStorage.getItem("firstname12"));
  let transData = localStorage.getItem("item_placed");
  let summary = document.getElementById("summary");
  // let table_number = document.createElement("p");
  // table_number.innerHTML = "Table Number: " + transData.table_number;
  // summary.appendChild(table_number);
  // let table_time_slot = document.createElement("p");
  // table_time_slot.innerHTML = "Time Slot: " + transData.table_time_slot;
  // summary.appendChild(table_time_slot);
  // let table_date = document.createElement("p");
  // table_date.innerHTML = "Date: " + transData.table_date;
  // summary.appendChild(table_date);
  // let table_total_price = document.createElement("p");
  // table_total_price.innerHTML = "Totatl Table Price: " + transData.table_total_price;
  // summary.appendChild(table_total_price);
  console.log(transData);
  console.log(Object.values(transData));
  // convert a json text to a js object
  let a = JSON.parse(transData);
  console.log(a);
  transData = JSON.parse(transData);
  let items_ordered = document.createElement("div");
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
    items_ordered.appendChild(item);
  });
  summary.appendChild(items_ordered);
  let totalPrice = document.createElement("p");
  totalPrice.innerHTML = "Total Price: " + transData.totalPrice;
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
  postData(Routes.transactionData, { someData: 23, someOtherData: "42" }).then(
    (data) => {
      console.log(data); // JSON data parsed by `data.json()` call
    }
  );
});

renderSummary();
