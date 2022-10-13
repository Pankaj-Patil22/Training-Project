import Routes from "./routes.js";

let menuData = [];
let items_placed = {};

function moveToPlacedSelection(item_id, price, name) {
  items_placed[item_id] = {
    itemId: 1,
    quantity: 1,
    price: price,
    name: name,
    totalPrice: price
  };

  let item = document.getElementById("item-" + item_id);
  item.remove();

  let quantityComp = document.createElement("p");
  quantityComp.setAttribute("id", "quantity-" + item_id);
  quantityComp.innerHTML = 1;

  item.appendChild(quantityComp);
  let plusBtn = document.createElement("button");
  plusBtn.addEventListener("click", () => {
    increaseQuantity(item_id);
    document.getElementById("quantity-" + item_id).innerHTML = items_placed[
        item_id
        ].quantity;
    document.getElementById("price-" + item_id).innerHTML = items_placed[
        item_id
        ].totalPrice;
    });
    plusBtn.innerHTML = "+";

  let minusBtn = document.createElement("button");
  minusBtn.addEventListener("click", () => {
    let success = decreaseQuantity(item_id);
    if (success) {
      document.getElementById("quantity-" + item_id).innerHTML = items_placed[
          item_id
          ].quantity;
      document.getElementById("price-" + item_id).innerHTML = items_placed[
          item_id 
          ].totalPrice;
      }
    });
    minusBtn.innerHTML = "-";

  item.appendChild(plusBtn);
  item.appendChild(minusBtn);
  let placedContainer = document.getElementById("placedConatiner");
  placedContainer.appendChild(item);
  let a = document.getElementById(item_id)
  a.remove();
}

async function fetchMenuData() {
  let url = Routes.menu;
  try {
    let res = await fetch(url);
    return await res.json();
  } catch (error) {
    console.log(error);
  }
}

async function renderMenuData() {
  menuData = await fetchMenuData();
  console.log(menuData);
  let html = "";
  for (let item of menuData) {
    let htmlSegment = `<div class="card" id="${"item-" + item.item_id}">
        <img class="card-img-top" src="${item.image}">
        <h2>${item.name}</h2>
                        <p>${item.description}</p>
                        <p id="${"price-" + item.item_id}">Price: ${item.price}</p>
                        <button id='${item.item_id}'>Add to Cart</button>
                        </div>`;
    html += htmlSegment;
  }    

  let container = document.getElementById("notPlacedConatiner");
  container.innerHTML = html;
  for (let item of menuData) {
    document.getElementById(item.item_id).addEventListener("click", () => {
      moveToPlacedSelection(item.item_id, item.price, item.name);
    });
  }
}

function increaseQuantity(item_id) {
  items_placed[item_id].quantity += 1;
  items_placed[item_id].totalPrice =
    items_placed[item_id].price * items_placed[item_id].quantity;
}

function decreaseQuantity(item_id) {
  if (items_placed[item_id].quantity > 1) {
    items_placed[item_id].quantity -= 1;
    items_placed[item_id].totalPrice = items_placed[item_id].price * items_placed[item_id].quantity;
    return true
  } else {
    delete items_placed[item_id];
    let item = document.getElementById("item-" + item_id);
    item.remove();
    let container = document.getElementById("notPlacedConatiner");
    container.appendChild(item);
    return false;
  }
}

function proceedToCheckout() {
  localStorage.setItem("item_placed", JSON.stringify(items_placed));
  localStorage.setItem("firstname12", "Alen");
  window.location.href = "checkout.html";
}

document.getElementById("proceedToCheckoutID").addEventListener("click", () => {
  proceedToCheckout();
});

renderMenuData();
localStorage.setItem("firstname", "Alen");