$(document).ready ( function () {
    $(".btn-success").click(function(){
        $("#addProductModal").modal( "show");
    });
    $(".edit").click(function (){
        $("#editProductModal").modal( "show");
        $("#edit_id").val($(this).closest('tr').children()[0].textContent);
        $("#edit_nombre").val($(this).closest('tr').children()[1].textContent);
        $("#edit_descripcion").val($(this).closest('tr').children()[3].textContent);
        $("#edit_precio").val($(this).closest('tr').children()[2].textContent);
        //$("#txtstock").val($(this).closest('tr').children()[5].textContent);
    });
    $(".delete").click(function (){
        $("#deleteProductModal").modal( "show");
        $("#delete_id").val($(this).closest('tr').children()[0].textContent);
    });
    
});
