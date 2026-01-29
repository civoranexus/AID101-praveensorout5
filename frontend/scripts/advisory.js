/**
 * AgriAssist AI - Advisory Script
 * Phase 2: Farmer Portal + Dashboard Integration
 *
 * Handles fetching and displaying advisories from backend APIs.
 */

document.addEventListener("DOMContentLoaded", () => {
    const advisoryContainer = document.getElementById("advisoryContainer") || document.getElementById("advisoryList");
    const authForm = document.getElementById("authForm");

    // ---------- Fetch Advisories ----------
    async function fetchAdvisories(farmId) {
        try {
            const response = await fetch(`/api/advisory/${farmId}`);
            if (!response.ok) throw new Error("Failed to fetch advisories");
            const advisories = await response.json();

            if (advisories.length === 0) {
                advisoryContainer.innerHTML = "<p>No advisories available yet.</p>";
                return;
            }

            advisoryContainer.innerHTML = advisories.map(a =>
                `<div class="advisory-card">
                    <strong>[${a.type}]</strong> ${a.message}
                </div>`
            ).join("");
        } catch (err) {
            advisoryContainer.innerHTML = `<p class="error">Error: ${err.message}</p>`;
        }
    }

    // ---------- Handle Registration/Login ----------
    if (authForm) {
        authForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const data = {
                farmer_name: document.getElementById("farmerName").value,
                crop_type: document.getElementById("cropType").value,
                acreage: document.getElementById("acreage").value,
                planting_date: document.getElementById("plantingDate").value,
                soil_type: document.getElementById("soilType").value,
                region: document.getElementById("region").value
            };

            try {
                const response = await fetch("/api/farm-profiles", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });
                if (!response.ok) throw new Error("Failed to register farm profile");
                const result = await response.json();

                advisoryContainer.innerHTML = `<p>Welcome, ${result.profile.farmer_name}! Your farm ID is ${result.profile.id}.</p>`;
                // Fetch advisories immediately after registration
                fetchAdvisories(result.profile.id);
            } catch (err) {
                advisoryContainer.innerHTML = `<p class="error">Error: ${err.message}</p>`;
            }
        });
    }
});
