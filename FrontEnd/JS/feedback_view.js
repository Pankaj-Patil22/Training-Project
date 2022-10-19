const feedback_id = localStorage.getItem("feedback_id");
if (feedback_id == null) {
    window.location.href = "http://127.0.0.1:5000/home/"
}

function renderOverallRating(feedback_id) {
    let rating = document.getElementById("overall_rating");
    rating.value = overall_rating;
}

let url = "http://127.0.0.1:5000/get_overall_feedback/" + user_id;

async function getOverallFeedback(feedback_id) {
    fetchData()
}

async function fetchData(url) {
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
} 