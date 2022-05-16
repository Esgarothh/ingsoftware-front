// Select/Deselect checkboxes
document.getElementById('selectAll').onclick = function () {
    var checkboxes = document.getElementsByName('options[]');
    if (this.checked) {
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].checked = true;
        }
    } else {
        for (var i = 0; i < checkboxes.length; i++) {
            checkboxes[i].checked = false;
        }

    }
}
// Get Addproduct Modal 
var modalAddProduct = document.getElementById('addProductModal');
// Get Editproduct Modal
var modalEditProduct = document.getElementById('editProductModal');
// Get Deleteproduct Modal
var modalDeleteProduct = document.getElementById('deleteProductModal');
// Get the button that opens the Addproduct modal
var btnAddProduct = document.getElementById("btnAddProduct");
// Get the button that opens the Editproduct modal
var btnEditProduct = document.getElementById("btnEditProduct");
// Get the button that opens the Deleteproduct modal
var btnDeleteProduct = document.getElementById("btnDeleteProduct");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
// When the user clicks the button, open the Addproduct modal
btnAddProduct.onclick = function () {
    modalAddProduct.style.display = "block";
}
// When the user clicks the button, open the Editproduct modal
btnEditProduct.onclick = function () {
    modalEditProduct.style.display = "block";
}
// When the user clicks the button, open the Deleteproduct modal
btnDeleteProduct.onclick = function () {
    modalDeleteProduct.style.display = "block";
}
// When the user clicks on <span> (x), close the modal Addproduct
span.onclick = function() {
    modalAddProduct.style.display = "none";
}
// When the user clicks on <span> (x), close the modal Editproduct
span.onclick = function() {
    modalEditProduct.style.display = "none";
}
// When the user clicks on <span> (x), close the modal Deleteproduct
span.onclick = function() {
    modalDeleteProduct.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modalAddProduct) {
        modalAddProduct.style.display = "none";
    }
    if (event.target == modalEditProduct) {
        modalEditProduct.style.display = "none";
    }
    if (event.target == modalDeleteProduct) {
        modalDeleteProduct.style.display = "none";
    }
}