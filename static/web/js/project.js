$('#category').change(function(){
    var categoryId=$(this).val()
    var data = {
        'category':categoryId,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    }
    $.ajax({
        url:'/get-countries/',
        type:'POST', 
        data:data,
        success:function(response){
            $("#prdctName").val(response['category'])
            $('#country').empty();
            var newOption = $('<option value="">--select--</option>');
            $('#country').append(newOption);
            for(var i = 0; i<response.data.length; i++){
                var newOption = $('<option value="'+response.data[i]['name']+'">'+response.data[i]['name']+'</option>');
                $('#country').append(newOption);
            }
        }
    })
    
})




$('#country').change(function(){
    var countryId=$(this).val()
    var categoryId=$('#category').val()
    var data = {
        'country':countryId,
        'category':categoryId,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    }
    $.ajax({
        url:'/get-price/',
        type:'POST', 
        data:data,
        success:function(response){
            $("#price").val(response.price)
            $("#productprice").val(response.price)
            
            
        }
    })
    
})



$('#quantity').change(function(){
    
    var quantity=$(this).val()
    var price=$("#productprice").val()
    var data = {
        'quantity':quantity,
        'price':price,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    }
    $.ajax({
        url:'/get-totalprice/',
        type:'POST', 
        data:data,
        success:function(response){
            console.log(response)
            $("#price").val(response.totalPrice)
            
        }
    })

})

var data =[]
$('#forms').submit(function(e){
    var datas = $('#forms').serializeArray()
  
    
    dataObj = {};
    console.log(data)
    $(datas).each(function(i, field){
      dataObj[field.name] = field.value;
    });
    data.push(dataObj)
    console.log(data)
    console.log(dataObj['category'])
    $('#forms').trigger("reset")
    var row = $("<tr />")
    $("#table").append(row);
    row.append($("<td>" + dataObj.prdctName + "</td>"));
    row.append($("<td>" + dataObj.country + "</td>"));
    row.append($("<td>" + dataObj.quantity + "</td>"));
    row.append($("<td>" + dataObj.price + "</td>"));
    return false;

});




$('#whatsapp-form').submit(function () {

    var phone = '+919539438918';
    var name = $('#name').val()
    var companyName = $('#cmpnyname').val()
    var companyAddr = $('#cmpnyadrs').val()
    var email = $('#email').val()
    var mobile = $('#mob').val()
    

    const text = [
        'Name:' + name,
        'Company Name: ' + companyName,
        'Company Address: ' + companyAddr,
        'Email Id:' + email,
        'Mobile:' + mobile,

    ].join("\n")
    // console.log(data)
    // var product = []
    // for(var i=0; i<data.length; i++){
    //     product.push([
    //         'product:' + data[i].prdctName,
    //     ]).join("\n") 
    // }
   

    console.log(data)
    // change to what you want sep to be
    
    const action = "https://wa.me/" + phone + "?text=" + encodeURIComponent(text)+"?text="+encodeURIComponent(product);
    window.location.href = action;

    return false
})



