$( function() {

  $( "#active" ).sortable({
  });
  $( "#active" ).disableSelection();

  $( "#done" ).sortable({
  });

  $( "#done" ).disableSelection();

  $( "#active" ).on( "sortupdate", function( event, ui ) {
          var activelist = $("#active").sortable('toArray')
          var donelist = $("#done").sortable('toArray')

          if (typeof donelist !== 'undefined' && donelist.length > 0) {
            var list = activelist.concat(donelist)
          } else {
            var list = activelist
          }

          

          var jsonlist = JSON.stringify(list)

          $.ajax({
            url: '/updatepriority',
            type: 'post',
            data: {id:jsonlist},
            dataType: 'json',
            success: function (data) {}
          });
  } );

  $( "#done" ).on( "sortupdate", function( event, ui ) {
          var donelist  = $("#done").sortable('toArray')
          var activelist = $("#active").sortable('toArray')
          
          if (typeof activelist !== 'undefined' && activelist.length > 0) {
            var list = activelist.concat(donelist)
          } else {
            var list = donelist
          }

          var jsonlist = JSON.stringify(list)

          $.ajax({
            url: '/updatepriority',
            type: 'post',
            data: {id:jsonlist},
            dataType: 'json',
            success: function (data) {}
          });
  });
});