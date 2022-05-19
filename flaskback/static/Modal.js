$(document).ready ( function () {
    var id 
    $(".btn-product").click(function(){
        $("#ModalProducto").modal( "show");
    });
    //Marca la opcion seleccionada
    $(".select").change(function(){
        id = $(this).children(":selected").attr("id");
        //añadir producto a tabla
    });
    $("#btnConfirmarAgregarProducto").click(function(){
        var datosjs = $("#"+id).val();
        var regExp = /\(([^)]+)\)/;
        var matches = regExp.exec(datosjs);
        var datos = matches[1].split(",");
        var id_prod = datos[0];
        var nombre = datos[1];
        var descripcion = datos[2];
        var precio = datos[3];
        var cantidad = $("#Cantidad").val();
        var total = precio * cantidad;
        var html = "<tr><td>"+id_prod+"</td><td>"+nombre+"</td><td>"+descripcion+"</td><td>"+precio+"</td><td>"+cantidad+"</td><td>"+total+"</td><td><button class='btn btn-danger btn-sm btn-eliminar-producto'><i class='fa fa-trash material-icons'>&#xE872;</i></button></td></tr>";
        //recibe Json con datos
        $("#tabla-productos").append(html);
        //reiniciar valores 
        $("#Cantidad").val("");
        $("#ModalProducto").modal( "hide");
    });
    //Eliminar producto de la tabla
    $(document).on("click",".btn-eliminar-producto",function(){
        $(this).closest("tr").remove();
    });
});

