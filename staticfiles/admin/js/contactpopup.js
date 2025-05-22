function openPopup() {
  const modal = document.getElementById("contactModal");
  if (modal) {
      modal.style.display = "flex";
  }
}

function closePopup() {
  const modal = document.getElementById("contactModal");
  if (modal) {
      modal.style.display = "none";
  }
}

window.onload = function () {
  // Pokazuje popup po 3 sekundach
  setTimeout(openPopup, 3000);

  // Zamknij, jeśli klikniesz na "x"
  const closeBtn = document.getElementById("closeModalBtn");
  if (closeBtn) {
      closeBtn.addEventListener("click", closePopup);
  }

  // Zamknij, jeśli klikniesz poza okienko
  window.addEventListener("click", function (e) {
      const modal = document.getElementById("contactModal");
      if (e.target === modal) {
          closePopup();
      }
  });
};

  