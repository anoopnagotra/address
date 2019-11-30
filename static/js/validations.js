$(document).ready(function(){
  // Validation
  $.validator.addMethod("noSpace", function(value, element) {
    return value.indexOf(" ") < 0 && value != "";
  }, "Space is not allowed");

  /*
   * Validation for Profile Page
   */
  $.validator.addMethod('validUrl', function (value) {
    var regex = /^(http[s]?:\/\/)?([-\w\d]+)(\.[-\w\d]+)*(\.([a-zA-Z]{2,5}|[\d]{1,3})){1,2}(\/([-~%\.\(\)\w\d]*\/*)*(#[-\w\d]+)?)?$/
    if( regex.test(value)){
      return true
    }else if(value == ''){
      return true
    }else{
      return false
    }
    // return /^(http|https)?:\/\/[a-zA-Z0-9-\.]+\.[a-z]{2,4}/.test(value);
  }, 'Please enter a valid url.');

  $('.inputname').change(function() {
      $(this).val($(this).val().trim());
  });

  $("#contact_page_form").validate({
        rules: {
          url: {
           validUrl:true,
           required: true,
           minlength: 3,
           maxlength: 50
         }
       },
       messages: {
          url: {
            maxlength: "Facebook link should be less than 50 characters"
          }
       }
   });
});