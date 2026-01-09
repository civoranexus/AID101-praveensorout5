// script.js

// -----------------------------
// Smooth scroll for navigation
// -----------------------------
document.querySelectorAll("nav a").forEach(link => {
  link.addEventListener("click", function(e) {
    e.preventDefault();
    const targetId = this.getAttribute("href").substring(1);
    const targetSection = document.getElementById(targetId);
    if (targetSection) {
      targetSection.scrollIntoView({ behavior: "smooth" });
    }
  });
});

// Highlight feature on click.
document.querySelectorAll(".feature").forEach(feature => {
  feature.addEventListener("click", () => {
    alert(`You clicked on: ${feature.querySelector("h3").innerText}`);
  });
});

// -----------------------------
// Dynamic footer year
// -----------------------------
const footer = document.querySelector("footer p");
const currentYear = new Date().getFullYear();
footer.innerHTML = `&copy; ${currentYear} Agri Assist. All rights reserved.`;

// -----------------------------
// Toggle contact info
// -----------------------------
const contactSection = document.getElementById("contact");
const toggleBtn = document.createElement("button");
toggleBtn.textContent = "Toggle Contact Info";
toggleBtn.style.marginTop = "1rem";
toggleBtn.style.padding = "0.5rem 1rem";
toggleBtn.style.backgroundColor = "#2e7d32";
toggleBtn.style.color = "#fff";
toggleBtn.style.border = "none";
toggleBtn.style.borderRadius = "5px";
toggleBtn.style.cursor = "pointer";
contactSection.appendChild(toggleBtn);

toggleBtn.addEventListener("click", () => {
  contactSection.querySelectorAll("p").forEach(p => {
    p.style.display = (p.style.display === "none") ? "block" : "none";
  });
});

// -----------------------------
// Crop Advisory Demo Form Logic
// -----------------------------
// (Optional: Add this form in your HTML inside #features or a new section)
//
// <section id="advisory">
//   <h2>Crop Advisory</h2>
//   <form id="advisoryForm">
//     <label for="crop">Enter Crop Name:</label>
//     <input type="text" id="crop" name="crop" required>
//     <button type="submit">Get Advice</button>
//   </form>
//   <div id="adviceOutput"></div>
// </section>

const advisoryForm = document.getElementById("advisoryForm");
if (advisoryForm) {
  advisoryForm.addEventListener("submit", function(e) {
    e.preventDefault();
    const crop = document.getElementById("crop").value.trim().toLowerCase();
    const output = document.getElementById("adviceOutput");

    let advice = "";
    switch (crop) {
      case "wheat":
        advice = "🌾 Wheat grows best in cool climates. Ensure timely irrigation during critical growth stages.";
        break;
      case "rice":
        advice = "🍚 Rice requires standing water. Monitor rainfall and consider alternate wetting and drying for sustainability.";
        break;
      case "maize":
        advice = "🌽 Maize needs well-drained soil. Apply nitrogen fertilizer in split doses for better yield.";
        break;
      case "cotton":
        advice = "🧵 Cotton thrives in warm climates. Watch for pests like bollworms and use integrated pest management.";
        break;
      default:
        advice = "❓ No specific advice found. Please consult local experts or extension services.";
    }

    output.textContent = advice;
    output.style.marginTop = "1rem";
    output.style.fontWeight = "500";
    output.style.color = "#2e7d32";
  });
}
