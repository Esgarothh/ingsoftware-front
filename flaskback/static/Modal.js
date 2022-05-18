//Get Modal
var modal = document.getElementById('ModalProducto');
// Get the button that opens the modal
var btn = document.getElementById("myBtn");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
// When the user clicks the button, open the modal
btn.onclick = function() {
    console.log("click");
    modal.style.display = "block";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Set the time
var today = new Date();

      var dd = today.getDate();
      var mm = today.getMonth()+1; //January is 0!
      var yyyy = today.getFullYear();

      if(dd<10) {
          dd = '0'+dd
      } 

      if(mm<10) {
          mm = '0'+mm
      } 

      // today = yyyy + '/' + mm + '/' + dd;
       today = yyyy + '-' + mm + '-' + dd;
       //document.getElementById('date').value = today;

//Agregar producto a la factura
var btnConfirmarAgregarProducto = document.getElementById("btnConfirmarAgregarProducto");