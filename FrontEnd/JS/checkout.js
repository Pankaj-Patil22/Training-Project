import Routes from "./routes.js";

async function renderSummary() {
  console.log(localStorage.getItem("item_placed"));
  console.log(localStorage.getItem("firstname"));
  console.log(localStorage.getItem("firstname12"));
  let transData = localStorage.getItem("item_placed");
  let summary = document.getElementById("summary");

  let table_number_boldText = document.createElement("strong");
  table_number_boldText.innerHTML = "Table Number: ";
  let table_number = document.createElement("p");
  table_number.appendChild(table_number_boldText)
  console.log(localStorage.getItem("choosentables"))
  table_number.append(localStorage.getItem("choosentables"));
  summary.appendChild(table_number);

  let table_time_slot_boldText = document.createElement("strong");
  table_time_slot_boldText.innerHTML = "Time Slot: ";
  let table_time_slot = document.createElement("p");
  table_time_slot.appendChild(table_time_slot_boldText)
  table_time_slot.append(localStorage.getItem("choosenTimeSlot"));
  summary.appendChild(table_time_slot);

  let table_date_boldText = document.createElement("strong");
  table_date_boldText.innerHTML = "Date: ";
  let table_date = document.createElement("p");
  table_date.appendChild(table_date_boldText);
  table_date.append(localStorage.getItem("choosenDate"));
  summary.appendChild(table_date);

  let  table_total_price_boldText = document.createElement("strong");
  table_total_price_boldText.innerHTML = "Totatl Table Price: ";
  let table_total_price = document.createElement("p");
  table_total_price.appendChild(table_total_price_boldText);
  table_total_price.append(localStorage.getItem("totalPriceOfTable"));
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
      "<strong> Item Name: </strong>" +
      element.name +
      "<strong> Quantity: </strong>" +
      element.quantity +
      "<strong> Price: </strong>" +
      element.price +
      "<strong> Total Price: </strong>" +
      element.quantity +
      "<strong> X </strong>" +
      element.price +
      "<strong> = </strong>" +
      element.totalPrice;
      totalDishesPrice += parseInt(element.totalPrice);
    items_ordered.appendChild(item);
    
  });
  summary.appendChild(items_ordered);
  localStorage.setItem("totalDishesPrice", totalDishesPrice);
  let totalPrice = document.createElement("p");
  totalPrice.innerHTML = "<strong>Total Price: </strong>" + (parseInt(localStorage.getItem("totalDishesPrice")) + parseInt(localStorage.getItem("totalPriceOfTable")));
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
    specialInstructions: localStorage.getItem("choosenSpecialInstructions"),
  }
  return dataToPost;
}

renderSummary();
