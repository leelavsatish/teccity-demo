const backendURL = "http://4.240.93.124:5000"; // update this

async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const msg = document.getElementById("msg");

  const response = await fetch(`${backendURL}/api/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await response.json();
  msg.innerText = data.message;

  if (response.ok) {
    localStorage.setItem("user", username);
    window.location.href = "dashboard.html";
  }
}

async function loadDashboard() {
  const user = localStorage.getItem("user");
  if (!user) {
    window.location.href = "login.html";
    return;
  }

  const response = await fetch(`${backendURL}/api/visits/${user}`);
  const data = await response.json();
  document.getElementById("info").innerText = `${user} visited ${data.visits} times`;
}

function logout() {
  localStorage.removeItem("user");
  window.location.href = "login.html";
}

// Auto-run dashboard fetch if on that page
if (window.location.pathname.endsWith("dashboard.html")) {
  loadDashboard();
}

