import Routes from "./routes.js";

async function renderSummary() {
    console.log(localStorage.getItem("item_placed"));
    console.log(localStorage.getItem("firstname"));
    console.log(window.localStorage.getItem("firstname12"));
    let transData = localStorage.getItem("item_placed")
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
    console.log(transData)
    let items_ordered = document.createElement("div");
    Object.values(transData).forEach(element => {
        let item = document.createElement("p");
        item.innerHTML = "Item Name: " + element.name + " Quantity: " + element.quantity + " Price: " + element.price;
        items_ordered.appendChild(item);
    });
    summary.appendChild(items_ordered);

    let totalPrice = document.createElement("p");
    totalPrice.innerHTML = "Total Price: " + transData.totalPrice;
    summary.appendChild(totalPrice);
  }

renderSummary()