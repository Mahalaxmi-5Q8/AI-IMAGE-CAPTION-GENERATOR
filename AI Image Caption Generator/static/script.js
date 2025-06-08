document.getElementById("uploadForm").addEventListener("submit", async function(e) {
  e.preventDefault();

  const input = document.getElementById("imageInput");
  const file = input.files[0];
  if (!file) {
    alert("Please select an image.");
    return;
  }

  const formData = new FormData();
  formData.append("image", file);

  document.getElementById("caption").textContent = "Generating caption...";
  const reader = new FileReader();
  reader.onload = () => {
    const img = document.getElementById("preview");
    img.src = reader.result;
    img.style.display = "block";
  };
  reader.readAsDataURL(file);

  try {
    const response = await fetch("/caption", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    if (data.caption) {
      document.getElementById("caption").textContent = "Caption: " + data.caption;
    } else {
      document.getElementById("caption").textContent = "Error: " + (data.error || "Unknown error");
    }
  } catch (err) {
    console.error(err);
    document.getElementById("caption").textContent = "Something went wrong!";
  }
});
