async function checkCrush() {
  const chat = document.getElementById("chatInput").value;
  const resultBox = document.getElementById("resultBox");

  if (chat.trim() === "") {
    resultBox.style.display = "block";
    resultBox.innerText = "Please paste a chat first!";
    return;
  }

  resultBox.style.display = "block";
  resultBox.innerText = "Analyzing...";

  try {
    const res = await fetch("/analyze", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ chat })
    });

    const data = await res.json();
    resultBox.innerText = data.status;
  } catch (err) {
    resultBox.innerText = "Error analyzing chat.";
    console.error(err);
  }
}