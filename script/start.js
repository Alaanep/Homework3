var $name=$("#name");

  $(document).ready(function() {
       $('button[type="submit"]').prop('disabled', true);

       $('#name').keyup(function() {
          var disable = false;

          $('#name').each(function() {
            if($(this).val() == '') { disable = true };
          });

          $('button[type="submit"]').prop('disabled', disable);
          $name=$("#name");
       });
  });
