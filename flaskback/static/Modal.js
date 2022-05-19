$(document).ready ( function () {
    var id;
    let Lista_final = [];
    $(".btn-product").click(function(){
        $("#ModalProducto").modal( "show");
    });
    //Marca la opcion seleccionada
    $(".select").change(function(){
        id = $(this).children(":selected").attr("id");
        //añadir producto a tabla
    });
    $("#btnConfirmarAgregarProducto").click(function(){
        let nuevo_producto = [];
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
        var html = "<tr><td>"+id_prod+"</td><td>"+nombre+"</td><td>"+descripcion+"</td><td>"+precio+"</td><td>"+cantidad+"</td><td>"+total+"</td><td><button class='btn btn-danger btn-sm btn-eliminar-producto'><i class='fa fa-trash'></i></button></td></tr>";
        nuevo_producto.push(id_prod);
        nuevo_producto.push(cantidad);
        nuevo_producto.push(total);
        Lista_final.push(nuevo_producto);
        var hidden = "<input type='hidden' id='productos_final' name='productos_final' value='"+Lista_final+"'>";
        //recibe Json con datos
        $("#ModalProducto").modal( "hide");
        //reiniciar valores 
        $("#tabla-productos").append(html);
        $("#Cantidad").val("");
        $("#div_productos").html(hidden);
    });
});

