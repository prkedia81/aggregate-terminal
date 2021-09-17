// Hide the CAGR on load
document.getElementById("answer").style.display = "none";
document.getElementById("reset").style.display = "none";

// Clicking the button calls our CAGR function
document.getElementById("calculate").onclick = function () {
  calculateCAGR();
};

// CAGR Function
function calculateCAGR() {
  // Store the data of inputs
  let beginningValue = document.getElementById("beginning-value").value;
  let endingValue = document.getElementById("ending-value").value;
  let time = document.getElementById("time").value;

  if(beginningValue == 0 || endingValue == 0 || time == 0) {
    window.alert("Please fill in all the values!")
    return;
  }

  // Form Validation
  (function () {
    "use strict";

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    let forms = document.querySelectorAll(".needs-validation");

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms).forEach(function (form) {
      form.addEventListener(
        "submit",
        function (event) {            
          if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();        
          }

          form.classList.add("was-validated");          
        },
        false
      );
    });
  })();

  let cagr = Math.pow(endingValue / beginningValue, 1 / time) - 1;
  cagr = (cagr * 100).toFixed(2);

  // Display the tip!
  document.getElementById("answer").style.display = "block";
  document.getElementById("returns").innerHTML = cagr;
  document.getElementById("reset").style.display = "block";
}

// Clicking the reset button
document.getElementById("reset").onclick = function () {
    reset();
  };

function reset() {
    location.reload()
}
