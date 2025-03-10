document.addEventListener("DOMContentLoaded", function () {
    M.AutoInit();

    document.getElementById("search-route").addEventListener("click", function () {
        let address = document.getElementById("address-autocomplete").value;
        if (address) {
            geocodeAddress(address);
        } else {
            alert("Please enter an address.");
        }
    });
});
