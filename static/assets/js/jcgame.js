
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

function like(obj){

  //var id = $(this).attr("id");
  var id = obj.id
  var like_count = parseInt($("[id=like_count][name$='"+id+"']").text())  //点赞的数量
  like_count++   //自加1
  $("[id=like_count][name$='"+id+"']").text(like_count)

  jQuery.ajax({
    type:"POST",
    url:"/blog/like",
    async:true,
    dataType:"json",
    data:{"id":id,"like_count":like_count},
    success:function(data){    
        console.log("赞")
    }
  });
}

// $(function(){

//   $(".am-icon-btn").click(function(){
//   var id = $(this).attr("id");

//   var like_count = parseInt($("[name$='"+id+"']").text())  //点赞的数量
//   like_count++   //自加1
//   $("[name$='"+id+"']").text(like_count)

//   jQuery.ajax({
//     type:"POST",
//     url:"like",
//     async:true,
//     dataType:"json",
//     data:{"id":id,"like_count":like_count},
//     success:function(data){    
//         console.log("赞")
//     }
//   });

// })

// })
