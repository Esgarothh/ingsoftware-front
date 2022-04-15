var inputBox =
	"<label for='casillaInputLote'>Numero del lote</label> \
<input \
    type='text' \
    class='form-control' \
    id='casillaInputLote' \
    value='N° LOTE' \
	required \
/>";

function desplegarBoxes() {
	var valor = document.getElementById("usarplantillacheck");
	if (valor.value == 0) {
		valor.value = 1;
		document.getElementById("box-parrafo-1").innerHTML = "";
		console.log(valor.value);
		return 0;
	}
	valor.value = 0;
	document.getElementById("box-parrafo-1").innerHTML = inputBox;
}
