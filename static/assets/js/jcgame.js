
  $('#popres').click(function () {
  var $btn = $(this)
  $btn.button('loading');

    jQuery.ajax({
    type:"POST",
    url:"cars/car_counts",
    async:true,
    dataType:"json",
    data:{"multiple":$("#multiple").val()},
    success:function(data){    
      setTimeout(function(){
        $btn.button('reset');
        $('#car_res').html(data.year+'年'+data.month+"月摇中")
        //alert(data.year+'年'+data.month+"月摇中")      
        $('#my-alert').modal("open")
        }, 1000); 
    }
  });
});