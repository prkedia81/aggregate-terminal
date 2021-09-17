// Hide the CAGR on load
document.getElementById("answer").style.display = "none";
document.getElementById("reset").style.display = "none";

// Clicking the button calls our SIP function
document.getElementById("calculate").onclick = function () {
  calculateSIP();
};

// CAGR Function
function calculateSIP() {
  // Store the data of inputs
  let investmentAmount = document.getElementById("investment-amount").value;
  let yearlyRateOfReturn =
    document.getElementById("rate-of-return").value / 100;
  let rateOfReturn = yearlyRateOfReturn / 12;
  let tenure = document.getElementById("tenure").value * 12;

  if(investmentAmount == 0 || yearlyRateOfReturn == 0 || tenure == 0) {
    window.alert("Please fill in all the values!")
    return;
  }

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

  let sip =
    investmentAmount *
    (Math.pow(1 + rateOfReturn, tenure) - 1) *
    ((1 + rateOfReturn) / rateOfReturn);
  sip = sip.toFixed(2);

  let amountInvested = investmentAmount * tenure;
  amountInvested = amountInvested.toFixed(2);

  let gains = sip - amountInvested;
  gains = gains.toFixed(2);

  // Display the tip!
  document.getElementById("answer").style.display = "block";
  document.getElementById("returns").innerHTML = sip;
  document.getElementById("invested").innerHTML = amountInvested;
  document.getElementById("gain").innerHTML = gains;
  document.getElementById("reset").style.display = "block";
}

// Clicking the reset button
document.getElementById("reset").onclick = function () {
  reset();
};

function reset() {
  location.reload();
}
