const languageData = {
  az: {
    subscribeSuccess: "Abone oldunuz!",
  },
  en: {
    subscribeSuccess: "You have subscribed!",
  },
  ru: {
    subscribeSuccess: "Вы подписались!",
  },
};

const subscribeForm = document.getElementById("subscribeForm");
const subscribeFormDiv = document.getElementById("subscribe-form-div");
const emailInput = document.getElementById("emailInput");

subscribeForm.addEventListener("submit", function (event) {
  event.preventDefault();

  let email = emailInput.value;

  // Errorlari temizle
  const existingErrorsDiv = subscribeFormDiv.querySelector(".errors");
  if (existingErrorsDiv) {
    existingErrorsDiv.remove();
  }

  // Aktiv dilin alinmasi
  const currentLanguage = window.location.pathname.split("/")[1];

  const URL = `${window.location.origin}/${currentLanguage}/subscribe/`;

  fetch(URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": subscribeForm.csrfmiddlewaretoken.value,
    },
    body: "email=" + encodeURIComponent(email),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log("data", data);
      if (data.success) {
        subscribeFormDiv.textContent = getLocalizedText("subscribeSuccess");
        subscribeFormDiv.style.fontSize = "30px";
        subscribeFormDiv.style.color = "green";
      } else {
        const errorsDiv = document.createElement("div");
        errorsDiv.classList.add("errors", "text-danger");

        // Errorlari goster
        data.email_errors.forEach((error) => {
          const errorNode = document.createElement("p");
          errorNode.textContent = error;
          errorsDiv.appendChild(errorNode);
        });

        subscribeFormDiv.appendChild(errorsDiv);
      }
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });

  return false;
});

function getLocalizedText(key) {
  const currentLanguage = window.location.pathname.split("/")[1] || "az"; // Default dil: AZ
  return languageData[currentLanguage][key] || key;
}
