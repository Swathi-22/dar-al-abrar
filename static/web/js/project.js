totalSum = [];

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



$('#quantity').keyup(function(){
    
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
    totalSum.push (dataObj.price)
    console.log(totalSum)
    var total = 0;
    for (var i = 0; i < totalSum.length; i++) {
    total += totalSum[i] << 0;
    }
    console.log(total)
    $("#total").html(total)
    return false;
});




$('#whatsapp-form').submit(function () {

    var name = $('#name').val()
    var companyName = $('#cmpnyname').val()
    var companyAddr = $('#cmpnyadrs').val()
    var email = $('#email').val()
    var mobile = $('#mob').val()
    var total = 0;
    for (var i = 0; i < totalSum.length; i++) {
    total += totalSum[i] << 0;
    }
    details = {
        'name':name,
        'companyname' :companyName,
        'companyaddress':companyAddr,
        'email':email,
        'total':total,
        'mobile':mobile,
        'data':data,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    }
    console.log(details)
    details['data'] = JSON.stringify(details['data'])
    $.ajax({
        url:'/send-whatsapp/',
        type:'POST', 
        data:details,
        success:function(response){
            window.location.href=response['link']
            console.log(response)
           
            
        }
    })
    return false
})






