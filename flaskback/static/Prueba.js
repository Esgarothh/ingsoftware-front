$(document).ready ( function () {
    $(".btn-success").click(function(){
        $("#addProductModal").modal( "show");
    });
    $(".edit").click(function (){
        $("#editProductModal").modal( "show");
        $("#txtname").val($(this).closest('tr').children()[1].textContent);
        $("#txtdesc").val($(this).closest('tr').children()[5].textContent);
        $("#txtprice").val($(this).closest('tr').children()[3].textContent);
        $("#txtstock").val($(this).closest('tr').children()[4].textContent);
    });
    $(".delete").click(function (){
        $("#deleteProductModal").modal( "show");
    });
    
});