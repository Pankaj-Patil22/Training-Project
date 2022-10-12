// import Routes from "./routes.js";
// // const routes = require('routes');
let menuData = [];


async function fetchMenuData() {
    let url = 'http://127.0.0.1:5000/getMenu/';
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
    let html = '';
    menuData.forEach(item => {
        let htmlSegment = `<div class="card" id="item-${item.item_id}">
                            <img src="${item.image}" >
                            <h2>${item.name}</h2>
                            <p>${item.description}</p>
                            <p>${item.price}</p>
                            <button onclick="moveToPlacedSelection()">Add to Cart</button>
                        </div>`;

        html += htmlSegment;
    });

    let container = document.querySelector('.container');
    container.innerHTML = html;
}

function moveToPlacedSelection(){

}

renderMenuData();