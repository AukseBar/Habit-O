$(document).ready(function(){
   /* Toggles day value */
   $('.day').click(function(){
      var day = $(this);
      var day_id = $(this).attr('id');
      day_id = day_id.substr(day_id.indexOf('_') + 1);
      var habit_slug = $(this).parents('#xTable').attr('data-slug');
      
      $.ajax({
         type: "GET",
         url: "/habits/update_habit/toogle_day/", 
         data: {slug: habit_slug, day_id: day_id},
         success: function(result){
            day.html(result);
         },
         error: function(xhr, ajaxOptions, thrownError){
            return;
         }
      });
   });
});

