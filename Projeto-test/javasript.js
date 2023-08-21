var coll = document.getElementsByClassName("descer");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}

  document.getElementById("transicao-suave").addEventListener("click", function(event) {
    event.preventDefault();
    this.classList.toggle("show");
    var dropdownMenu = this.nextElementSibling;
    if (dropdownMenu.style.visibility === "hidden" || dropdownMenu.style.visibility === "") {
      dropdownMenu.style.visibility = "visible";
      dropdownMenu.style.opacity = 1;
      dropdownMenu.style.transform = "translateY(0)";
    } else {
      dropdownMenu.style.visibility = "hidden";
      dropdownMenu.style.opacity = 0;
      dropdownMenu.style.transform = "translateY(-10px)";
    }
  });

  document.addEventListener('DOMContentLoaded', function() {
    const loadingOverlay = document.getElementById('loading-overlay');
    const linksWithLoading = document.querySelectorAll('.link-with-loading');

    linksWithLoading.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            loadingOverlay.style.display = 'flex';
            
            setTimeout(function() {
                window.location.href = link.getAttribute('href');
            }, 1000); // Altere o tempo (em milissegundos) conforme necessário
        });
    });
});