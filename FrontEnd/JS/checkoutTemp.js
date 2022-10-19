import Routes from "./routes.js";
let imageData = {}

async function renderSummary() {
    await fetch("http://127.0.0.1:5000/getMenu/")
      .then((Response) => Response.json())
      .then((data) => {
        imageData = data;
      });
    console.log(imageData);
  console.log(localStorage.getItem("item_placed"));
  console.log(localStorage.getItem("firstname"));
  console.log(localStorage.getItem("firstname12"));
  let transData = localStorage.getItem("item_placed");
  document.getElementById("tablesSelectedText").innerText=localStorage.getItem("choosentables").replace(/[[""\]]/g,' ');
  document.getElementById("tableSubtotalId").innerText=localStorage.getItem("totalPriceOfTable")
  
  let totalDishesPrice = 0;
  let allOrderedFoodContainer = document.getElementById('summary');

  transData = JSON.parse(transData);
  Object.values(transData).forEach((element) => {
    totalDishesPrice += parseInt(element.totalPrice);

    let orderedFoodContainer = document.createElement("div")
    orderedFoodContainer.classList.add('row', 'd-flex', 'justify-content-center', 'border-top');
    orderedFoodContainer.id = "item"+element.itemId
    orderedFoodContainer.setAttribute('style','background-color: #FFFAFA; border-radius:20px')
    let foodImageContainer = document.createElement("div")
    foodImageContainer.classList.add('col-5')
    let foodImageRow = document.createElement("div")
    foodImageRow.classList.add('row', 'd-flex')
    let foodBookDiv = document.createElement("div")
    foodBookDiv.classList.add('book')
    let foodImage = document.createElement('img')
    foodImage.classList.add('book-img')
    foodImage.srcset = imageData[element.itemId -1]['image'];
    foodBookDiv.appendChild(foodImage)
    let foodNameContainer = document.createElement('div')
    foodNameContainer.classList.add('my-auto', 'flex-column', 'd-flex', 'pad-left')
    let foodNameText = document.createElement('h6')
    foodNameText.classList.add('mob-text')
    foodNameText.innerText = element.name
    foodNameContainer.appendChild(foodNameText)
    foodImageRow.appendChild(foodBookDiv)
    foodImageRow.appendChild(foodNameContainer)
    foodImageContainer.appendChild(foodImageRow)
    
    let orderDetails = document.createElement('div')
    orderDetails.classList.add('my-auto', 'col-7')
    let rightOderDetails = document.createElement('div')
    rightOderDetails.classList.add('row', 'text-right')
    let quantityDiv = document.createElement('div')
    quantityDiv.classList.add('col-4')
    let orderQuantityAdjust = document.createElement('div')
    orderQuantityAdjust.classList.add('row', 'd-flex', 'justify-content-end', 'px-3')
    let plusminusDiv = document.createElement('div')
    plusminusDiv.classList.add('d-flex', 'align-items-center', 'plus-minus')
    let divAddBtn = document.createElement('div')
    divAddBtn.classList.add('btn')
    divAddBtn.innerHTML += "<button class='fas fa-plus' onclick='addQuantDish(this)' id='"+element.itemId+"'>+</button>"
    let quantityNumberText = document.createElement('p')
    quantityNumberText.classList.add('mb-0')
    quantityNumberText.id ="cnt"+element.itemId
    quantityNumberText.setAttribute('style','padding:10px ;')
    quantityNumberText.innerText = element.quantity
    let divMinusBtn = document.createElement('div')
    divMinusBtn.classList.add('btn')
    divMinusBtn.innerHTML += "<button class='fas fa-minus' onclick='minusQuantDish(this)' id='"+element.itemId+"'>-</button>"
    plusminusDiv.appendChild(divAddBtn)
    plusminusDiv.appendChild(quantityNumberText)
    plusminusDiv.appendChild(divMinusBtn)
    orderQuantityAdjust.appendChild(plusminusDiv)
    quantityDiv.appendChild(orderQuantityAdjust)

    let divPricePer = document.createElement('div')
    divPricePer.classList.add('col-4')
    let priceTextPer = document.createElement('h6')
    priceTextPer.classList.add('mob-text')
    priceTextPer.id = "pricePerId"+element.itemId
    priceTextPer.innerText = element.price
    divPricePer.appendChild(priceTextPer)
    let divPriceQuant = document.createElement('div')
    divPriceQuant.classList.add('col-4')
    let priceTextQuant = document.createElement('h6')
    priceTextQuant.classList.add('mob-text')
    priceTextQuant.id = "priceQuantId"+element.itemId
    priceTextQuant.innerText = (element.quantity * element.price)
    divPriceQuant.appendChild(priceTextQuant)

    rightOderDetails.appendChild(quantityDiv)
    rightOderDetails.appendChild(divPricePer)
    rightOderDetails.appendChild(divPriceQuant)
    orderDetails.appendChild(rightOderDetails)

    orderedFoodContainer.appendChild(foodImageContainer)
    orderedFoodContainer.appendChild(orderDetails)
    allOrderedFoodContainer.appendChild(orderedFoodContainer)
  })
  localStorage.setItem("totalDishesPrice", totalDishesPrice);
  document.getElementById("menuSubtotalId").innerText=localStorage.getItem("totalDishesPrice")
  document.getElementById("totalPTP").innerText=parseInt(localStorage.getItem("totalPriceOfTable"))+parseInt(localStorage.getItem("totalDishesPrice"))
}

async function postData(url = "", data = {}) {
  // Default options are marked with *
  console.log(Routes.transactionData);
  let responseJson = "";
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
      responseJson = data;
    })
    .catch((error) => {
      console.error("Error:", error);
      console.log("Error:");
    });
  // return response.json(); // parses JSON response into native JavaScript objects
  return responseJson;
}

document.getElementById("checkout").addEventListener("click", () => {
  postData(Routes.transactionData, makeThePostData()).then((data) => {
    console.log(data); // JSON data parsed by `data.json()` call
    if (data.success == true) {
      console.log("success Boss", data);
      localStorage.clear();
      window.location.href = "history.html";
    } else {
      console.log("failed Boss", data);
    }
  });
});

document.getElementById("checkout").addEventListener("click", () => {
  console.log(localStorage.getItem("item_placed"));
  let dataToPost = makeThePostData();
  console.log("the dataToPost", dataToPost);
});

document.getElementById("tempBtn").addEventListener("click", () => {
    console.log(localStorage.getItem("item_placed"));
    let dataToPost = makeThePostData();
    console.log("the dataToPost", dataToPost);
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
  };
  return dataToPost;
}
renderSummary();