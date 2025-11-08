// Login function for login.html
function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  fetch("/api/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  })
    .then(res => res.json())
    .then(data => {
      if (data.status === "success") {
        localStorage.setItem("username", username);
        window.location.href = "/dashboard";
      } else {
        document.getElementById("message").innerText = data.message;
      }
    });
}

// Dashboard logic for dashboard.html
document.addEventListener("DOMContentLoaded", () => {
  const visitsElement = document.getElementById("visits");
  const logoutBtn = document.getElementById("logoutBtn");
  const username = localStorage.getItem("username");

  if (visitsElement && username) {
    fetch(`/api/visits/${username}`)
      .then(res => res.json())
      .then(data => {
        visitsElement.innerText =
          `Hello ${data.username}, you have visited ${data.visits} times.`;
      });
  }

  if (logoutBtn) {
    logoutBtn.addEventListener("click", () => {
      localStorage.removeItem("username");
      window.location.href = "/";
    });
  }
});

