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
            $('#country').empty();

            for(var i = 0; i<response.data.length; i++){
                
                var newOption = $('<option value="'+response.data[i]['name']+'">'+response.data[i]['name']+'</option>');
                $('#country').append(newOption);
            }
        }
    })
    
})