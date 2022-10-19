const overall_rating = document.getElementById("overall_rating");

function changeOverallRating() {
  value = document.getElementById("overall_rating").value;
  document.getElementById("overall_rating_value").innerHTML = value;
}

function changeItemRating(item_id) {
  value = document.getElementById(`item_rating_${item_id}`).value;
  document.getElementById(`item_rating_value_${item_id}`).innerHTML = value;
}

function get_items_in_order(order_id) {
  console.log("order_id get_items_in_order", order_id);
  const response = fetch(`http://127.0.0.1:5000/get_items_in_order/${order_id}`)
    .then((response) => response.json())
    .then((data) => {
      return data;
    });
  return response;
}

function create_items(order_id, transaction_id) {
  const items = get_items_in_order(order_id);

  items.then((data) => {
    data.forEach((item) => {
      const item_div = document.createElement("div");
      item_div.className = "item";
      item_div.setAttribute('class',"row justify-content-around")

      item_div.innerHTML = `
<div id=${item.item_id} style ="background-color: #FFFAFA; border-radius:20px; max-width:60%;" class="justify-content-center card gy-5">
    <div class="item-image">
    <div class="item-name"><strong>${item.name}</strong></div>
    <img src="${item.image}" alt="item image" style="width: 300px;height: 350px;"/>
    </div>
    <div class="item-rating">
        <input type="range" id="item_rating_${item.item_id}" name="item_rating" value="0" min="0" max="5" onchange="changeItemRating(${item.item_id})"/>
        <span id="item_rating_value_${item.item_id}">0</span>
    </div>
    <div class="item-review">
        <textarea
        name="item-review"
        id="item_review_${item.item_id}"
        cols="50"
        rows="5"
        placeholder="Write your review here..."
        ></textarea>
    </div>
    </div>`;
      document.getElementById("item_feedback").appendChild(item_div);
    });
  });
}

function submitFeedback(order_id) {
  const overall_rating = document.getElementById("overall_rating").value;
  const overall_review = document.getElementById("overall_review").value;

  items_feedback = [];

  items = get_items_in_order(order_id);

  items.then((data) => {
    data.forEach((item) => {
      items_feedback.push({
        item_id: item.item_id,
        rating: document.getElementById(`item_rating_${item.item_id}`).value,
        review: document.getElementById(`item_review_${item.item_id}`).value,
      });
    });

    const feedback = {
      order_id: order_id,
      overall_rating: overall_rating,
      overall_review: overall_review,
      items_feedback: items_feedback,
      transaction_id: localStorage.getItem("transaction_id"),
    };

    console.log("print feedback", feedback);
    fetch("http://127.0.0.1:5000/feedback/", {
      method: "POST",
      mode: "cors",
      credentials: "omit",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(feedback),
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
  });
}

document.getElementById("submit_feedback_btn").addEventListener("click", () => {
  submitFeedback(localStorage.getItem("order_id"));
});

create_items(
  localStorage.getItem("order_id"),
  localStorage.getItem("transaction_id")
);
