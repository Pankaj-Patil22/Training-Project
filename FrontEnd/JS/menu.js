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
  quantityComp.innerText = "Quantity: "+1;

  item.appendChild(quantityComp);
  let plusBtn = document.createElement("button");
  plusBtn.setAttribute("id", "plus-" + item_id);
  plusBtn.addEventListener("click", () => {
    increaseQuantity(item_id);
    document.getElementById("quantity-" + item_id).innerText = "Quantity: "+items_placed[
        item_id
        ].quantity;
    document.getElementById("price-" + item_id).innerText= "Price: "+items_placed[
        item_id
        ].totalPrice;
    });
    plusBtn.innerHTML = "+";

  let minusBtn = document.createElement("button");
  minusBtn.setAttribute("id", "minus-" + item_id);
  minusBtn.addEventListener("click", () => {
    let success = decreaseQuantity(item_id);
    if (success) {
      document.getElementById("quantity-" + item_id).innerText = "Quantity: "+items_placed[
          item_id
          ].quantity;
      document.getElementById("price-" + item_id).innerText = "Price: "+items_placed[
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
  document.getElementById("proceedToCheckoutID").removeAttribute('disabled','')
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
    let htmlSegment = `<div class="card gy-5" style="max-width: 18rem;" id="${"item-" + item.item_id}">
        <img src="${item.image}"  width="200" height="200" class="card-img-top" alt="...">
        <h5 class="card-title">${item.name}</h5>
                        <p class="card-text">${item.description}</p>
                        <strong><p id="${"price-" + item.item_id}">Price: ${item.price}</p></strong>
                        <button class="btn btn-dark" id='${item.item_id}'>Add to Cart</button>
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
  document.getElementById("proceedToCheckoutID").removeAttribute('disabled','')
}

function decreaseQuantity(item_id) {
  if (items_placed[item_id].quantity > 1) {
    items_placed[item_id].quantity -= 1;
    items_placed[item_id].totalPrice = items_placed[item_id].price * items_placed[item_id].quantity;
    return true
  } else {
    delete items_placed[item_id];
    let item = document.getElementById("item-" + item_id);
    item.removeChild(document.getElementById("quantity-" + item_id))
    item.removeChild(document.getElementById("plus-" + item_id))
    item.removeChild(document.getElementById("minus-" + item_id))
    let addToCartButton = document.createElement("button");
    addToCartButton.setAttribute("id", item_id);
    addToCartButton.setAttribute("class", "btn btn-dark");
    addToCartButton.innerText = "Add to Cart"
    item.appendChild(addToCartButton)
    item.remove();
    
    let container = document.getElementById("notPlacedConatiner");
    container.appendChild(item);

    let selectedContainerLength = document.getElementById("placedConatiner").childNodes.length
    if(selectedContainerLength == 1){
      document.getElementById("proceedToCheckoutID").setAttribute('disabled','')
    }
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