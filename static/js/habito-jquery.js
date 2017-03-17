$(document).ready(function(){
   
   /* EDIT HABIT'S TITLE */
   var editTitleHandler = function(){
      var el = $(this);
      var habit_slug = el.attr('data-slug');
      
      // Removes event handler to prevent double click while editing 
      el.off('dblclick');
      
      var old_title = el.html();
      el.html('<input id="newTitle" type="text" value="' + old_title + '"/>');
      
      // Function executed after changing
      $('#newTitle').focus().on('change', function(){
         var new_title = $(this).val();
         // If there is a new title sends Ajax request
         if(new_title != old_title){
            $.ajax({
               type: "GET",
               url: "/habits/update_habit/edit_title/", 
               data: {slug: habit_slug, new_title: new_title},
               success: function(result){
                  new_title = result;
               },
               error: function(xhr, ajaxOptions, thrownError){
                  new_title = old_title;
               }
            });
         }
         el.html(new_title);
         
         // Resets event handler
         el.on('dblclick', editTitleHandler);
      });
      $('#newTitle').on('blur', function(){
         el.html(old_title);
         el.on('dblclick', editTitleHandler);
      });
   };
   
   // Binds event to the title element
   $('#habitTitle').on('dblclick', editTitleHandler);
   
   /* TOGGLES DAY VALUE */
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

