$(document).ready ( function () {
    $(".edit").click(function (){
        $("#editCotizacionModal").modal( "show");
        $("#edit_id").val($(this).closest('tr').children()[0].textContent);
        $("#edit_cliente").val($(this).closest('tr').children()[1].textContent);
        $("#edit_descripcion").val($(this).closest('tr').children()[2].textContent);
        $("#edit_monto").val($(this).closest('tr').children()[3].textContent);
        //$("#txtstock").val($(this).closest('tr').children()[5].textContent);
    });
    $(".delete").click(function (){
        $("#deleteCotizaciontModal").modal( "show");
        $("#delete_id").val($(this).closest('tr').children()[0].textContent);
    });
    
});