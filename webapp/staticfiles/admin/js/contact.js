function closePopup() {
    document.getElementById("contactModal").style.display = "none";
  }
  
  window.onload = function () {
    setTimeout(() => {
      document.getElementById("contactModal").style.display = "flex";
    }, 3000);
  
    document.getElementById("closeModalBtn").onclick = closePopup;
  
    window.onclick = function (event) {
      const modal = document.getElementById("contactModal");
      if (event.target === modal) {
        closePopup();
      }
    };
  };
  
  









  
  